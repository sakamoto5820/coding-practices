"""問15 Cache のテスト。"""

import pytest

from solutions import Cache


class TestQ15Cache:
    def test_example_scenario(self):
        c = Cache()
        c.add(1, 100)
        c.add(2, 200)
        assert c.get(1) == 100  # key=1 が「最近アクセス」に
        c.evict()  # key=2 が削除される
        with pytest.raises(KeyError):
            c.get(2)
        assert c.get(1) == 100

    def test_add_overwrites_and_refreshes(self):
        c = Cache()
        c.add(1, 100)
        c.add(2, 200)
        c.add(1, 111)  # 上書き＝アクセス扱い → 最古は key=2
        c.evict()
        with pytest.raises(KeyError):
            c.get(2)
        assert c.get(1) == 111

    def test_remove(self):
        c = Cache()
        c.add(1, 100)
        assert c.remove(1) == 100
        with pytest.raises(KeyError):
            c.remove(1)
        with pytest.raises(KeyError):
            c.get(1)

    def test_evict_order(self):
        c = Cache()
        c.add(1, 10)
        c.add(2, 20)
        c.add(3, 30)
        c.get(1)  # アクセス順: 2, 3, 1
        c.evict()  # 2 が消える
        c.evict()  # 3 が消える
        assert c.get(1) == 10
        with pytest.raises(KeyError):
            c.get(3)

    def test_evict_empty_is_noop(self):
        c = Cache()
        c.evict()  # 例外にならないこと
