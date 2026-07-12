"""問19 SQL (JOIN + DISTINCT + ORDER) のテスト。sqlite3(インメモリ)で検証。"""

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
        CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, department_id INTEGER);
        CREATE TABLE departments (id INTEGER PRIMARY KEY, dept_name TEXT, location TEXT);
        CREATE TABLE assignments (employee_id INTEGER, project_id INTEGER);

        INSERT INTO employees VALUES (1, 'Sato', 10), (2, 'Kimura', 10), (3, 'Abe', 20);
        INSERT INTO departments VALUES (10, 'Dev', 'Tokyo'), (20, 'Sales', 'Osaka');
        INSERT INTO assignments VALUES (1, 100), (1, 101), (3, 100);
        """
    )
    yield conn
    conn.close()


def test_expected_result(db):
    rows = db.execute(read_sql("problem19.sql")).fetchall()
    # Satoは2プロジェクトあるが1行のみ。Kimuraはアサインなし、AbeはOsaka。
    assert rows == [("Sato", "Dev")]


def test_ordering_and_dedup_with_more_data(db):
    # Tokyo所属・アサインありの従業員を追加し、name昇順と重複排除を確認
    db.executescript(
        """
        INSERT INTO employees VALUES (4, 'Aoki', 10), (5, 'Watanabe', 10);
        INSERT INTO assignments VALUES (4, 100), (4, 101), (4, 102), (5, 100);
        """
    )
    expected = [("Aoki", "Dev"), ("Sato", "Dev"), ("Watanabe", "Dev")]
    assert db.execute(read_sql("problem19.sql")).fetchall() == expected
