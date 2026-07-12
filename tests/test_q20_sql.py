"""問20 SQL (JOIN + 集計 + HAVING + ORDER) のテスト。sqlite3(インメモリ)で検証。"""

import sqlite3
from pathlib import Path

import pytest

SQL_DIR = Path(__file__).parent.parent / "sql"


def read_sql(name: str) -> str:
    return (SQL_DIR / name).read_text()


@pytest.fixture
def db():
    conn = sqlite3.connect(":memory:")
    conn.executescript(
        """
        CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, registered_at TEXT);
        CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, amount INTEGER, ordered_at TEXT);

        INSERT INTO users VALUES (1, 'Tanaka', '2024-01-01'), (2, 'Suzuki', '2024-06-01');
        INSERT INTO orders VALUES
            (1, 1, 1000, '2025-03-01'),
            (2, 1, 2000, '2025-05-10'),
            (3, 1, 3000, '2025-11-20'),
            (4, 2, 9999, '2025-01-05'),
            (5, 1, 5000, '2024-12-31');  -- 2024年なので対象外
        """
    )
    yield conn
    conn.close()


def test_expected_result(db):
    rows = db.execute(read_sql("problem20.sql")).fetchall()
    # Suzukiは1回のみ対象外。Tanakaの2024年注文は集計に含めない。
    assert rows == [("Tanaka", 3, 6000)]


def test_ordering_and_tiebreak(db):
    # 合計金額の降順、同額なら name 昇順を確認
    db.executescript(
        """
        INSERT INTO users VALUES (3, 'Yamada', '2024-02-01'), (4, 'Ito', '2024-03-01');
        -- Yamada: 3回で計6000 (Tanakaと同額 → name昇順で Tanaka が先)
        INSERT INTO orders VALUES
            (6, 3, 1000, '2025-02-01'),
            (7, 3, 2000, '2025-06-15'),
            (8, 3, 3000, '2025-12-31'),
        -- Ito: 4回で計10000 (最上位)
            (9, 4, 2500, '2025-01-01'),
            (10, 4, 2500, '2025-04-01'),
            (11, 4, 2500, '2025-07-01'),
            (12, 4, 2500, '2025-10-01');
        """
    )
    rows = db.execute(read_sql("problem20.sql")).fetchall()
    assert rows == [
        ("Ito", 4, 10000),
        ("Tanaka", 3, 6000),
        ("Yamada", 3, 6000),
    ]


def test_year_boundary(db):
    # 2026-01-01 の注文は対象外(半開区間の右端)
    db.execute("INSERT INTO orders VALUES (6, 1, 100, '2026-01-01')")
    rows = db.execute(read_sql("problem20.sql")).fetchall()
    assert rows == [("Tanaka", 3, 6000)]
