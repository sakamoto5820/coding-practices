"""問4 classify のテスト。"""

from solutions import classify


class TestQ4Classify:
    def test_examples(self):
        assert classify([7, 7, 7]) == 0
        assert classify([5, 3, 5]) == 1
        assert classify([1, 2, 3]) == 2
        assert classify([0, 0, 9]) == 1

    def test_additional(self):
        assert classify([9, 0, 0]) == 1
        assert classify([-1, -1, -1]) == 0
        assert classify([3, 5, 3]) == 1
