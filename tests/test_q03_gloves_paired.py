"""問3 gloves_paired のテスト。"""

from solutions import gloves_paired


class TestQ3GlovesPaired:
    def test_examples(self):
        assert gloves_paired([[0, 20], [1, 20], [0, 21], [1, 21]]) is True
        assert gloves_paired([[0, 20], [1, 20], [1, 20]]) is False
        assert gloves_paired([[0, 23], [1, 23], [0, 24]]) is False
        assert gloves_paired([]) is True

    def test_additional(self):
        assert (
            gloves_paired([[0, 20], [0, 20], [1, 20], [1, 20]]) is True
        )  # 同サイズ複数ペア
        assert gloves_paired([[0, 20]]) is False
        assert gloves_paired([[1, 20], [0, 20]]) is True  # 順不同
