"""問14 count_duplicated_kinds のテスト。"""

from solutions import count_duplicated_kinds


class TestQ14CountDuplicatedKinds:
    def test_examples(self):
        assert count_duplicated_kinds("foobarbaz") == 3
        assert count_duplicated_kinds("abcdef") == 0
        assert count_duplicated_kinds("aabbccdd") == 4
        assert count_duplicated_kinds("aaa") == 1

    def test_additional(self):
        assert count_duplicated_kinds("") == 0
        assert count_duplicated_kinds("a") == 0
        assert count_duplicated_kinds("aA") == 0  # 大文字小文字は別の文字
