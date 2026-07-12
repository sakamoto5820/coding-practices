"""問9 interleave のテスト。"""

from solutions import interleave


class TestQ9Interleave:
    def test_examples(self):
        assert interleave(["abc", "de", "fghi"]) == "adfbegchi"
        assert interleave(["ab", "cd", "efg"]) == "acebdfg"
        assert interleave(["hello"]) == "hello"
        assert interleave(["a", "bcd"]) == "abcd"
        assert interleave([]) == ""

    def test_additional(self):
        assert interleave(["", ""]) == ""
        assert interleave(["", "xy"]) == "xy"
        assert interleave(["ab", "ab"]) == "aabb"
