"""問8 process_queue のテスト。"""

from solutions import process_queue


class TestQ8ProcessQueue:
    def test_examples(self):
        assert process_queue(["enq 1", "enq 2", "front", "deq", "deq", "deq"]) == [
            1,
            1,
            2,
            -1,
        ]
        assert process_queue(["deq", "front", "enq 10", "front"]) == [-1, -1, 10]
        assert process_queue(["enq 5", "deq", "enq 6", "enq 7", "deq", "front"]) == [
            5,
            6,
            7,
        ]

    def test_additional(self):
        assert process_queue([]) == []
        assert process_queue(["front"]) == [-1]
        assert process_queue(["enq 1", "enq 2", "enq 3", "deq", "deq", "deq"]) == [
            1,
            2,
            3,
        ]
