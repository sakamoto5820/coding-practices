"""問17 max_product_of_three のテスト。"""

from solutions import max_product_of_three


class TestQ17MaxProductOfThree:
    def test_examples(self):
        assert max_product_of_three([3, 1, 2, 5, 4]) == 60
        assert max_product_of_three([-10, -10, 1, 3, 2]) == 300
        assert max_product_of_three([-5, -4, -3, -2]) == -24
        assert max_product_of_three([1, 2]) == -1
        assert max_product_of_three([0, -1, -2]) == 0  # 0×(-1)×(-2)=0 の1通りのみ

    def test_additional(self):
        assert max_product_of_three([0, -1, -2, -3]) == 0  # 0を含む三つ組が最大
        assert max_product_of_three([1, 1, 1]) == 1
        assert max_product_of_three([-1, -2, 3, 4]) == 8  # -1×-2×4
        assert max_product_of_three([]) == -1

    def test_brute_force_cross_check(self):
        from itertools import combinations

        def brute(nums):
            if len(nums) < 3:
                return -1
            return max(a * b * c for a, b, c in combinations(nums, 3))

        cases = [
            [3, 1, 2, 5, 4],
            [-10, -10, 1, 3, 2],
            [-5, -4, -3, -2],
            [0, -1, -2],
            [0, 0, 0, 1],
            [-7, 0, 3, 3, -7],
            [2, -3, 4, -5, 6, -7],
        ]
        for nums in cases:
            assert max_product_of_three(list(nums)) == brute(nums), nums
