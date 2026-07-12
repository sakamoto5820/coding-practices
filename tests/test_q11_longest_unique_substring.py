"""問11 longest_unique_substring のテスト。"""

from solutions import longest_unique_substring


class TestQ11LongestUniqueSubstring:
    def test_examples(self):
        assert longest_unique_substring("abcabcbb") == 3  # "abc"
        assert longest_unique_substring("bbbbb") == 1
        assert longest_unique_substring("pwwkew") == 3  # "wke"
        assert longest_unique_substring("abba") == 2  # 左端が戻らないこと
        assert longest_unique_substring("") == 0

    def test_additional(self):
        assert longest_unique_substring("a") == 1
        assert longest_unique_substring("abcdef") == 6  # 全文字ユニーク
        assert longest_unique_substring("dvdf") == 3  # "vdf"
        assert longest_unique_substring("tmmzuxt") == 5  # "mzuxt"

    def test_brute_force_cross_check(self):
        def brute(s):
            n = len(s)
            best = 0
            for i in range(n):
                for j in range(i, n):
                    sub = s[i : j + 1]
                    if len(set(sub)) == len(sub):
                        best = max(best, len(sub))
            return best

        cases = [
            "abcabcbb",
            "bbbbb",
            "pwwkew",
            "abba",
            "dvdf",
            "tmmzuxt",
            "aab",
            "ohvhjdml",
            "abcadefbg",
        ]
        for s in cases:
            assert longest_unique_substring(s) == brute(s), s
