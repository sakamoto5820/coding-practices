"""問16 is_cubic_happy のテスト。"""

from solutions import is_cubic_happy


class TestQ16IsCubicHappy:
    def test_examples(self):
        assert is_cubic_happy(1) is True
        assert is_cubic_happy(10) is True
        assert is_cubic_happy(2) is False
        assert is_cubic_happy(153) is False  # 1+125+27=153 の自己ループ

    def test_additional(self):
        assert is_cubic_happy(100) is True  # 100 → 1
        assert is_cubic_happy(371) is False  # 371 も自己ループ (27+343+1=371)
        assert is_cubic_happy(1000) is True
        # 全数終了性の確認(小さい範囲)
        for n in range(1, 2000):
            is_cubic_happy(n)  # 無限ループしないこと
