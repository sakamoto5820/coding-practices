# 問15. evict付きキャッシュ実装
class Cache:
    def __init__(self):
        # TODO: 必要な初期化を書く
        pass

    def add(self, key: int, value: int) -> None:
        """要素を追加。既存keyなら上書き(アクセス扱い)"""
        # TODO: ここに実装を書く

    def get(self, key: int) -> int:
        """値を返す。なければ KeyError"""
        # TODO: ここに実装を書く
        return None

    def remove(self, key: int) -> int:
        """値を返して削除。なければ KeyError"""
        # TODO: ここに実装を書く
        return None

    def evict(self) -> None:
        """最後にアクセスされてから最も時間が経った要素を削除"""
        # TODO: ここに実装を書く
