# コーディングテスト対策問題集【問題編・Python版】

## 第1部 問題編

---

### 問1. 直角三角形カウント【配列走査／easy】

正の整数の配列 `nums` が与えられる。**連続する3つの要素**を辺の長さとみなしたとき、直角三角形が成立する箇所の個数を返せ。

なお、3辺 `a, b, c`（`a <= b <= c`）が直角三角形を成立させる条件は、ピタゴラスの定理 `a² + b² = c²` が成り立つことである。

```python
def count_right_triangles(nums: list[int]) -> int:
    ...
```

**入出力例:**

```python
count_right_triangles([3, 4, 5, 12, 13, 1])   # => 2   ([3,4,5], [5,12,13])
count_right_triangles([1, 2, 3])              # => 0
count_right_triangles([6, 8, 10, 24, 26])     # => 2   ([6,8,10], [10,24,26])
count_right_triangles([5, 3, 4])              # => 1   (並び順によらず判定)
```

**制約:** `3 <= len(nums) <= 10^5`, `1 <= nums[i] <= 10^4`

---

### 問2. 山型カウント【配列走査／easy】

隣り合う3つの数字のうち、**真ん中の数だけが厳密に最大**（`nums[i] < nums[i+1] > nums[i+2]`）となる箇所の個数を返せ。

```python
def count_peaks(nums: list[int]) -> int:
    ...
```

**入出力例:**

```python
count_peaks([1, 3, 2, 4, 1, 1])    # => 2   ([1,3,2], [2,4,1])
count_peaks([1, 2, 3, 4, 5])       # => 0   (単調増加に山はない)
count_peaks([1, 5, 1, 5, 1])       # => 2
count_peaks([2, 2, 1])             # => 0   (等号は不成立)
```

**制約:** `3 <= len(nums) <= 10^5`

---

### 問3. 手袋ペア判定【Map集計／easy】

`pairs[i] == [hand, size]`。`hand == 0` は右手用、`1` は左手用。**すべてのサイズについて**右手用と左手用の数が一致していれば `True` を返せ。

```python
def gloves_paired(pairs: list[list[int]]) -> bool:
    ...
```

**入出力例:**

```python
gloves_paired([[0, 20], [1, 20], [0, 21], [1, 21]])   # => True
gloves_paired([[0, 20], [1, 20], [1, 20]])            # => False  (サイズ20の左が1つ多い)
gloves_paired([[0, 23], [1, 23], [0, 24]])            # => False
gloves_paired([])                                     # => True   (手袋なしは成立とみなす)
```

**制約:** `0 <= len(pairs) <= 10^5`

---

### 問4. 3要素の種類数判定【条件分岐／easy】

要素数3の配列に対し、3つとも等しければ `0`、ちょうど2つが等しければ `1`、3つとも異なれば `2` を返せ。

```python
def classify(nums: list[int]) -> int:
    ...
```

**入出力例:**

```python
classify([7, 7, 7])    # => 0
classify([5, 3, 5])    # => 1
classify([1, 2, 3])    # => 2
classify([0, 0, 9])    # => 1
```

---

### 問5. ロボットの向き揃えカウント【シミュレーション／medium・最重要】

N台のロボットが全員北向きでスタート。指示文字列 `s` の各文字は `R`（右90度）/ `L`（左90度）/ `A`（180度反転）。ただし `broken` に含まれるインデックスのロボットは `R` と `L` を**逆に解釈**する（`A` は正しく実行）。

**各指示の実行直後に「同じ向きを向いているロボットの最大台数」を数え、その総和を返せ。**（全台の向きが揃っていれば N を加算することになる）

```python
def count_aligned(n: int, broken: list[int], s: str) -> int:
    ...
```

**入出力例:**

```python
count_aligned(3, [2], "RLAARR")    # => 16  (指示ごとに 2+3+3+3+2+3)
count_aligned(2, [], "RLA")        # => 6   (故障なしなら常に全2台が揃う: 2×3)
count_aligned(2, [0, 1], "RRL")    # => 6   (全台故障でも常に揃う: 2×3)
count_aligned(4, [1], "RR")        # => 7   (1回目は正常3台のみ、2回目は全4台が揃う)
count_aligned(4, [1], "AA")        # => 8   (Aは相対角を変えないので常に全4台)
```

**制約:** `1 <= n <= 10^5`, `1 <= len(s) <= 10^5`。**O(n × len(s)) では間に合わない前提で設計せよ**

---

### 問6. Maxスタック記録【スタック／easy-medium】

指示は `"push x"` / `"pop"`（空なら無視）/ `"max"`（その時点の最大値を記録、空なら無視）。記録の配列を返せ。

```python
def process_max_stack(instructions: list[str]) -> list[int]:
    ...
```

**入出力例:**

```python
process_max_stack(["push 3", "max", "push 7", "max", "pop", "max"])
# => [3, 7, 3]

process_max_stack(["max", "pop", "push 5", "max"])
# => [5]           (空スタックへのmax/popは無視)

process_max_stack(["push 2", "push 9", "push 4", "max", "pop", "max"])
# => [9, 9]
```

---

### 問7. カッコ列の最大深さ【状態管理／easy】

`(` と `)` のみからなる文字列のネスト最大深さを返せ。不正な列（途中で深さが負になる／最後に0に戻らない）は `-1`。

```python
def max_depth(s: str) -> int:
    ...
```

**入出力例:**

```python
max_depth("(()(()))")   # => 3
max_depth("()()")       # => 1
max_depth("())(")       # => -1  (途中で負になる)
max_depth("((")         # => -1  (閉じ切らない)
max_depth("")           # => 0
```

---

### 問8. キュー操作シミュレーション【データ構造／easy】

指示は `"enq x"`（末尾追加）/ `"deq"`（先頭を取り除きその値を記録、空なら `-1` を記録）/ `"front"`（先頭の値を記録、空なら `-1`）。記録の配列を返せ。

```python
def process_queue(instructions: list[str]) -> list[int]:
    ...
```

**入出力例:**

```python
process_queue(["enq 1", "enq 2", "front", "deq", "deq", "deq"])
# => [1, 1, 2, -1]

process_queue(["deq", "front", "enq 10", "front"])
# => [-1, -1, 10]

process_queue(["enq 5", "deq", "enq 6", "enq 7", "deq", "front"])
# => [5, 6, 7]
```

---

### 問9. 縦読み結合【文字列／easy】

文字列の配列から、各文字列の1文字目→2文字目→…の順で1文字ずつ取り出して結合する。長さが足りない文字列はスキップ。

```python
def interleave(words: list[str]) -> str:
    ...
```

**入出力例:**

```python
interleave(["abc", "de", "fghi"])   # => "adfbegchi"
interleave(["ab", "cd", "efg"])     # => "acebdfg"
interleave(["hello"])               # => "hello"
interleave(["a", "bcd"])            # => "abcd"
interleave([])                      # => ""
```

---

### 問10. 4で割り切れる部分文字列【数え上げ／easy-medium】

数字のみからなる文字列 `s` の連続部分文字列のうち、整数として4で割り切れるものの個数を返せ。`"0"` 単体は認めるが、`"04"` のような**先頭0の2文字以上の数字は不許可**。

```python
def count_div4_substrings(s: str) -> int:
    ...
```

**入出力例:**

```python
count_div4_substrings("124")    # => 4   (4, 12, 24, 124)
count_div4_substrings("04")     # => 2   ("0" と "4"。"04" は不許可)
count_div4_substrings("8")      # => 1
count_div4_substrings("13")     # => 0
count_div4_substrings("400")    # => 5   (4, 40, 400, 0, 0 の5個。"00" は先頭0のため不許可)
```

---

### 問11. 重複なし最長部分文字列【文字列／medium】

文字列 `s` の**連続する**部分文字列のうち、同じ文字を2回以上含まないものの最大長を返せ。

```python
def longest_unique_substring(s: str) -> int:
    ...
```

**入出力例:**

```python
longest_unique_substring("abcabcbb")   # => 3   ("abc")
longest_unique_substring("bbbbb")      # => 1   ("b")
longest_unique_substring("pwwkew")     # => 3   ("wke"。"pwke" は連続でないため不可)
longest_unique_substring("abba")       # => 2   ("ab" または "ba")
longest_unique_substring("")           # => 0
```

**制約:** `0 <= len(s) <= 10^5`。**O(n²) の全探索では間に合わない前提で設計せよ**

---

### 問12. 文字集合一致カウント【ビットマスク／easy-medium】

単語 `w` と単語リスト `words` が与えられる。使われている**アルファベットの種類の集合**が `w` と完全一致する単語の個数を返せ。

```python
def count_similar(w: str, words: list[str]) -> int:
    ...
```

**入出力例:**

```python
count_similar("dog", ["good", "god", "dot", "dogo", "dg"])
# => 3   (good, god, dogo)

count_similar("love", ["velo", "low", "vole", "lovee", "loved"])
# => 3   (velo, vole, lovee。lowはw含む、lovedはd含むため不一致)

count_similar("aa", ["a", "aaa", "ab"])
# => 2   (a, aaa。集合はどちらも{a})
```

**制約:** `len(words) <= 500,000`。O(合計文字数) を目指せ

---

### 問13. 3桁区切りカンマ挿入【文字列整形／easy-medium】

数値文字列の**整数部分にのみ**3桁区切りの `,` を挿入して返せ。負号・小数部を含む場合がある。

```python
def add_commas(s: str) -> str:
    ...
```

**入出力例:**

```python
add_commas("1234567")         # => "1,234,567"
add_commas("-1234567.891")    # => "-1,234,567.891"
add_commas("100")             # => "100"
add_commas("-0.5")            # => "-0.5"
add_commas("1000000")         # => "1,000,000"
```

---

### 問14. 重複文字種カウント【頻度Map／easy】

2回以上出現する**文字の種類数**を返せ。重複がなければ `0`。

```python
def count_duplicated_kinds(s: str) -> int:
    ...
```

**入出力例:**

```python
count_duplicated_kinds("foobarbaz")     # => 3   (o, b, a)
count_duplicated_kinds("abcdef")        # => 0
count_duplicated_kinds("aabbccdd")      # => 4
count_duplicated_kinds("aaa")           # => 1
```

---

### 問15. evict付きキャッシュ実装【データ構造／medium】

次のインターフェースを持つクラスを実装せよ。`add` と `get` は「アクセス」とみなす。

```python
class Cache:
    def add(self, key: int, value: int) -> None:
        """要素を追加。既存keyなら上書き(アクセス扱い)"""

    def get(self, key: int) -> int:
        """値を返す。なければ KeyError"""

    def remove(self, key: int) -> int:
        """値を返して削除。なければ KeyError"""

    def evict(self) -> None:
        """最後にアクセスされてから最も時間が経った要素を削除"""
```

**入出力例:**

```python
c = Cache()
c.add(1, 100)
c.add(2, 200)
c.get(1)        # => 100  (これでkey=1が「最近アクセス」になる)
c.evict()       # key=2 が削除される(key=1より古い)
c.get(2)        # => KeyError
c.get(1)        # => 100
```

---

### 問16. キュービック・ハッピー数【数値／easy-medium】

正の整数 `n` を「各桁の**3乗**の和」で置き換える操作を繰り返す。`1` に到達すれば `True`、ループすれば `False`。

```python
def is_cubic_happy(n: int) -> bool:
    ...
```

**入出力例:**

```python
is_cubic_happy(1)      # => True
is_cubic_happy(10)     # => True   (10 → 1)
is_cubic_happy(2)      # => False  (2 → 8 → 512 → 134 → 92 → 737 → ... ループ)
is_cubic_happy(153)    # => False  (153 → 153 → ... 自分自身に戻るループ)
```

---

### 問17. 3数の積の最大値【ソート＋エッジケース／easy-medium】

整数リストから3つ選んだ積の最大値を返せ。要素数が3未満なら `-1`。

```python
def max_product_of_three(nums: list[int]) -> int:
    ...
```

**入出力例:**

```python
max_product_of_three([3, 1, 2, 5, 4])         # => 60   (3×4×5)
max_product_of_three([-10, -10, 1, 3, 2])     # => 300  (-10×-10×3)
max_product_of_three([-5, -4, -3, -2])        # => -24  (全て負なら絶対値の小さい3つ)
max_product_of_three([0, -1, -2])             # => 0   (選び方は1通りで 0×(-1)×(-2)=0)
max_product_of_three([1, 2])                  # => -1   (要素数不足)
```

---

### 問18. 正方形の最大辺長【集計／easy】

棒の長さの配列から、**同じ長さの棒4本**で正方形を1つ作る。作れる正方形の辺の最大長を返せ。作れなければ `-1`。

```python
def max_square_side(sticks: list[int]) -> int:
    ...
```

**入出力例:**

```python
max_square_side([3, 5, 5, 3, 5, 5, 3, 3, 3])   # => 5   (5は4本ある→数え直せ)
max_square_side([1, 1, 1, 1, 2, 2])            # => 1
max_square_side([7, 7, 7])                     # => -1  (3本では足りない)
max_square_side([4, 4, 4, 4, 4, 4, 4, 4])      # => 4
```

---

### 問19. SQL: JOIN + 絞り込み + DISTINCT + ORDER【SQL／easy-medium】

```sql
-- employees(id, name, department_id)
-- departments(id, dept_name, location)
-- assignments(employee_id, project_id)  -- 1人が複数行持ちうる
```

「`location = 'Tokyo'` の部署に所属し、**1つ以上のプロジェクトにアサインされている**従業員の `name, dept_name` を、`name` の昇順で**重複なく**取得せよ。」

**サンプルデータと期待結果:**

```
employees:                departments:              assignments:
id | name  | dept_id      id | dept_name | location  emp_id | proj_id
1  | Sato  | 10           10 | Dev       | Tokyo     1      | 100
2  | Kimura| 10           20 | Sales     | Osaka     1      | 101
3  | Abe   | 20                                      3      | 100

期待結果:
name | dept_name
Sato | Dev        ← 2プロジェクトあるが1行のみ
(Kimuraはアサインなし、AbeはOsakaのため対象外)
```

---

### 問20. SQL: JOIN + 集計 + HAVING + ORDER【SQL／medium】

```sql
-- users(id, name, registered_at)
-- orders(id, user_id, amount, ordered_at)
```

「2025年中に**3回以上**注文したユーザーの `name, 注文回数, 合計金額` を、合計金額の降順・同額なら `name` の昇順で取得せよ。」

**サンプルデータと期待結果:**

```
users:               orders:
id | name            id | user_id | amount | ordered_at
1  | Tanaka          1  | 1       | 1000   | 2025-03-01
2  | Suzuki          2  | 1       | 2000   | 2025-05-10
                     3  | 1       | 3000   | 2025-11-20
                     4  | 2       | 9999   | 2025-01-05
                     5  | 1       | 5000   | 2024-12-31  ← 2024年なので対象外

期待結果:
name   | order_count | total_amount
Tanaka | 3           | 6000
(Suzukiは1回のみのため対象外。Tanakaの2024年注文は集計に含めない)
```
