"""問12 count_similar のテスト。"""

from solutions import count_similar


class TestQ12CountSimilar:
    def test_examples(self):
        assert count_similar("dog", ["good", "god", "dot", "dogo", "dg"]) == 3
        assert count_similar("love", ["velo", "low", "vole", "lovee", "loved"]) == 3
        assert count_similar("aa", ["a", "aaa", "ab"]) == 2

    def test_additional(self):
        assert count_similar("abc", []) == 0
        assert count_similar("z", ["z", "zz", "za"]) == 2
        assert count_similar("ab", ["ba", "aabb", "abc", "a", "b"]) == 2
        assert count_similar("Dog", ["GOD"]) == 1  # 大文字小文字は同一視
