# InterviewCatコーディングテスト対策問題集

`coding_test_problems.md` の問題を自分で解いて、pytest で答え合わせする uv プロジェクト。

`solutions/` と `sql/` は未実装のスタブになっているので、テストが通るように実装してください。模範解答は `coding_test_solutions.md` にあります。

## 構成(1問1ファイル)

- `solutions/q01_count_right_triangles.py` 〜 `q18_max_square_side.py` — 問1〜問18 の解答欄(TODOスタブ)
- `sql/problem19.sql`, `sql/problem20.sql` — 問19・問20 の解答欄(TODOスタブ)
- `tests/test_q01_*.py` 〜 `test_q18_*.py` — 問題の入出力例＋追加エッジケース
- `tests/test_q19_sql.py`, `tests/test_q20_sql.py` — sqlite3(インメモリ)でSQLを実行して検証

## 進め方

```bash
uv sync          # 初回のみ(pytest, ruffをインストール)
uv run pytest    # 最初は全問FAILする
```

1. `coding_test_problems.md` で問題を読む
2. `solutions/qNN_*.py`(SQLは `sql/problemNN.sql`)の TODO を実装する
3. その問題のテストを実行して確認:

```bash
uv run pytest tests/test_q05_count_aligned.py -v   # 問5だけ
uv run pytest -v -k q17                            # ファイル名の部分一致でも可
uv run pytest tests/test_q19_sql.py tests/test_q20_sql.py -v   # SQLだけ
```

全問通ったら `uv run pytest` が緑になります。

## フォーマット・lint

```bash
uv run ruff format .   # フォーマット
uv run ruff check .    # lintチェック(--fix で自動修正)
```
