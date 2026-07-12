"""問5 count_aligned のテスト。"""

from solutions import count_aligned


class TestQ5CountAligned:
    def test_examples(self):
        assert count_aligned(3, [2], "RLAARR") == 16  # 2+3+3+3+2+3
        assert count_aligned(2, [], "RLA") == 6  # 故障なしなら常に全2台: 2×3
        assert count_aligned(2, [0, 1], "RRL") == 6  # 全台故障でも常に揃う: 2×3
        assert count_aligned(4, [1], "RR") == 7  # 正常3台のみ → 全4台
        assert count_aligned(4, [1], "AA") == 8  # Aは相対角を変えないので常に全4台

    def test_additional(self):
        assert count_aligned(1, [], "RLAR") == 4  # 1台なら常に揃う: 1×4
        assert count_aligned(2, [0], "RRRR") == 6  # 1+2+1+2 (揃うのは偶数回目)
        assert count_aligned(2, [0], "RL") == 3  # 1+2 (2指示目で揃う)
        assert count_aligned(3, [1], "A" * 5) == 15  # Aのみなら常に全3台: 3×5

    def test_group_sizes_matter(self):
        # 台数構成が答えに効くことの確認。揃うのは4指示、揃わないのは2指示。
        # 正常3・故障10: 4×13 + 2×10 = 72
        assert count_aligned(13, list(range(10)), "RLAARR") == 72
        # 正常300・故障20: 4×320 + 2×300 = 1880
        assert count_aligned(320, list(range(20)), "RLAARR") == 1880
