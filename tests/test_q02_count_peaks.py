"""問2 count_peaks のテスト。"""

from solutions import count_peaks


class TestQ2CountPeaks:
    def test_examples(self):
        assert count_peaks([1, 3, 2, 4, 1, 1]) == 2
        assert count_peaks([1, 2, 3, 4, 5]) == 0
        assert count_peaks([1, 5, 1, 5, 1]) == 2
        assert count_peaks([2, 2, 1]) == 0  # 等号は不成立

    def test_additional(self):
        assert count_peaks([1, 2, 2]) == 0  # 右側の等号も不成立
        assert count_peaks([5, 4, 3]) == 0
        assert count_peaks([0, 100, 0]) == 1
        assert count_peaks([-3, -1, -2]) == 1  # 負数でも成立
