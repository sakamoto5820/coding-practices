"""問10 count_div4_substrings のテスト。"""

from solutions import count_div4_substrings


class TestQ10CountDiv4Substrings:
    def test_examples(self):
        assert count_div4_substrings("124") == 4  # 4, 12, 24, 124
        assert count_div4_substrings("04") == 2  # "0" と "4"
        assert count_div4_substrings("8") == 1
        assert count_div4_substrings("13") == 0
        assert count_div4_substrings("400") == 5  # 4, 40, 400, 0(位置1), 0(位置2)

    def test_additional(self):
        assert count_div4_substrings("0") == 1
        assert count_div4_substrings("00") == 2  # "0" ×2。"00" は不許可
        assert count_div4_substrings("1") == 0
        assert count_div4_substrings("444") == 6  # 4,44,444,4,44,4
        assert count_div4_substrings("20") == 2  # 20, 0("02"ではなく単体0)
