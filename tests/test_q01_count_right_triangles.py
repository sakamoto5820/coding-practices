"""問1 count_right_triangles のテスト。"""

from solutions import count_right_triangles


class TestQ1CountRightTriangles:
    def test_examples(self):
        assert count_right_triangles([3, 4, 5, 12, 13, 1]) == 2
        assert count_right_triangles([1, 2, 3]) == 0
        assert count_right_triangles([6, 8, 10, 24, 26]) == 2
        assert count_right_triangles([5, 3, 4]) == 1  # 並び順によらず判定

    def test_additional(self):
        assert count_right_triangles([13, 12, 5]) == 1  # 降順でも成立
        assert count_right_triangles([1, 1, 1]) == 0
        assert count_right_triangles([3, 4, 5, 4, 3]) == 2  # 重なり合う窓
        assert count_right_triangles([7, 24, 25, 1, 1, 1]) == 1
