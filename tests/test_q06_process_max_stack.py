"""問6 process_max_stack のテスト。"""

from solutions import process_max_stack


class TestQ6ProcessMaxStack:
    def test_examples(self):
        assert process_max_stack(["push 3", "max", "push 7", "max", "pop", "max"]) == [
            3,
            7,
            3,
        ]
        assert process_max_stack(["max", "pop", "push 5", "max"]) == [5]
        assert process_max_stack(
            ["push 2", "push 9", "push 4", "max", "pop", "max"]
        ) == [9, 9]

    def test_additional(self):
        assert process_max_stack([]) == []
        assert process_max_stack(["push -3", "push -1", "max", "pop", "max"]) == [
            -1,
            -3,
        ]
        assert process_max_stack(["push 5", "pop", "pop", "max"]) == []
