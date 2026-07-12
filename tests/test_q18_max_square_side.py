"""問18 max_square_side のテスト。"""

from solutions import max_square_side


class TestQ18MaxSquareSide:
    def test_examples(self):
        assert max_square_side([3, 5, 5, 3, 5, 5, 3, 3, 3]) == 5  # 5は4本ある
        assert max_square_side([1, 1, 1, 1, 2, 2]) == 1
        assert max_square_side([7, 7, 7]) == -1
        assert max_square_side([4, 4, 4, 4, 4, 4, 4, 4]) == 4

    def test_additional(self):
        assert max_square_side([]) == -1
        assert max_square_side([2, 2, 2, 2, 9, 9, 9, 9]) == 9  # 両方作れるなら最大
        assert max_square_side([1, 2, 3, 4]) == -1
