"""問7 max_depth のテスト。"""

from solutions import max_depth


class TestQ7MaxDepth:
    def test_examples(self):
        assert max_depth("(()(()))") == 3
        assert max_depth("()()") == 1
        assert max_depth("())(") == -1
        assert max_depth("((") == -1
        assert max_depth("") == 0

    def test_additional(self):
        assert max_depth("()") == 1
        assert max_depth(")(") == -1
        assert max_depth("((((()))))") == 5
        assert max_depth("()(())") == 2
