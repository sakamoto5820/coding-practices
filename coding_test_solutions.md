# コーディングテスト対策問題集【解答・解説編・Python版】

## 第2部 解答・解説編

---

### 問1. 直角三角形カウント【配列走査／easy】

#### 解答

```python
def count_right_triangles(nums: list[int]) -> int:
    count = 0
    for i in range(len(nums) - 2):
        a, b, c = sorted(nums[i:i+3])
        if a * a + b * b == c * c:
            count += 1
    return count
```

#### 解説

問われているのは「連続する3つの要素」の組すべてに対する判定なので、やることは2つに分解できる。①配列から連続3要素の組をすべて取り出す、②その3要素が直角三角形になるか判定する。

①は、先頭から3要素ずつ切り取る枠を1つずつ右にずらしていけばよい。このような「配列の連続した一部分だけを切り取って見る枠」を**ウィンドウ**と呼ぶ:

```
nums = [3, 4, 5, 12, 13, 1]
        [3, 4, 5]              i=0 のウィンドウ → ✓
           [4, 5, 12]          i=1 のウィンドウ → ✗
              [5, 12, 13]      i=2 のウィンドウ → ✓
                 [12, 13, 1]   i=3 のウィンドウ → ✗
```

ウィンドウの左端 `i` は `0` から `len(nums) - 3` まで動くので、ウィンドウは全部で `len(nums) - 2` 個。コードの `for i in range(len(nums) - 2)` がこの「ウィンドウをずらす」操作に対応する。

②の判定は、3要素を `sorted` で昇順にすれば最大辺は必ず `c` に来るため、ピタゴラスの定理 `a² + b² == c²` の1式で済む。

- **なぜソートするか**: ソートしないと「どれが斜辺か」が分からず、`a²+b²==c²` / `a²+c²==b²` / `b²+c²==a²` の3式を書くことになる。式が増えるほど書き漏らし・添字ミスの温床になる。要素数3の固定長ソートはO(1)なので、コストは無視できる。
- **計算量**: ウィンドウの数 n-2 × ウィンドウあたりO(1) = 全体O(n)。制約の 10^5 でも余裕。
- **落とし穴**: `math.sqrt` で斜辺を求めて比較する実装は浮動小数の誤差で壊れうる。整数のまま2乗同士を比較するのが安全。

---

### 問2. 山型カウント【配列走査／easy】

#### 解答

```python
def count_peaks(nums: list[int]) -> int:
    return sum(
        1 for i in range(len(nums) - 2)
        if nums[i] < nums[i+1] > nums[i+2]
    )
```

#### 解説

「真ん中の数だけが厳密に最大」という日本語の条件を、そのまま述語 `nums[i] < nums[i+1] > nums[i+2]` に落とすだけの問題。Pythonは比較演算子を連鎖できるので、条件式が問題文とほぼ同じ形で書けて読み間違いが起きにくい。

`[1,3,2,4,1,1]` のトレース: ウィンドウは `(1,3,2)` ✓、`(3,2,4)` ✗、`(2,4,1)` ✓、`(4,1,1)` ✗ で答えは `2`。

- **等号の扱い**: 「厳密に」なので `<=` にしてはいけない。`[2,2,1]` が0になるのは左側が `2 < 2` を満たさないから。「以上/より大きい」の読み分けはこの種の問題の最頻出ミス。
- **境界**: ウィンドウが3要素なので最後のウィンドウの先頭は `n-3` 番目。`range(len(nums) - 2)` で自然に収まる。
- **計算量**: O(n)、追加メモリO(1)。

---

### 問3. 手袋ペア判定【Map集計／easy】

#### 解答1: 差分カウンタ

```python
from collections import defaultdict

def gloves_paired(pairs: list[list[int]]) -> bool:
    balance = defaultdict(int)
    for hand, size in pairs:
        balance[size] += 1 if hand == 0 else -1
    return all(v == 0 for v in balance.values())
```

素直に持つなら「右手用の辞書」と「左手用の辞書」を別々に作って突き合わせる方法だが、**差分カウンタ1本**に畳むと簡潔になる。サイズごとに右手で `+1`、左手で `-1` すれば「右と左が同数 ⇔ 差が0」なので、最後に全カウンタが0かを見るだけで済む。

- **空入力**: `all()` は空のイテラブルに対して `True` を返すため、`gloves_paired([])` は特別扱いなしで仕様どおり `True` になる。
- **計算量**: 1パスでO(n)、メモリはサイズの種類数に比例。
- **定石**: 「AとBが対になっているか」を問う問題(括弧の対応、入退室ログ、在庫の入出庫など)は、ほぼこの「+1/-1して最後に0か」の形に帰着する。

#### 解答2: Counterで組ごとに数える

`Counter` で `(hand, size)` の組をそのまま数え、各サイズについて右手用と左手用の数が一致するかを確認する方法でも正解。考え方は素直だが、キーが2倍になる分、解答1の差分カウンタの方が無駄がない。

```python
from collections import Counter

def gloves_paired_counter(pairs: list[list[int]]) -> bool:
    c = Counter((hand, size) for hand, size in pairs)
    return all(c[(0, size)] == c[(1, size)] for _, size in pairs)
```

---

### 問4. 3要素の種類数判定【条件分岐／easy】

#### 解答

```python
def classify(nums: list[int]) -> int:
    distinct = len(set(nums))  # 1, 2, 3 のいずれか
    return distinct - 1
```

#### 解説

返り値(0/1/2)を観察すると「3つとも等しい→種類数1」「ちょうど2つ等しい→種類数2」「全部異なる→種類数3」なので、**答え = 種類数 − 1** という対応がそのまま成り立つ。`set` に入れて `len` を取るだけで場合分けが消える。

- **if文で書く場合**: 「3つ等しい(`a == b == c`)」→「どれか2つ等しい(`a == b or b == c or a == c`)」→「それ以外」と、条件の強い順に判定すると漏れ・重複がない。逆順に書くと「2つ等しい」が「3つ等しい」を含んでしまいバグる。

---

### 問5. ロボットの向き揃えカウント【シミュレーション／medium・最重要】

#### 解答

```python
def count_aligned(n: int, broken: list[int], s: str) -> int:
    # 向きを 0=北,1=東,2=南,3=西 で表現
    normal = 0   # 正常ロボット共通の向き
    faulty = 0   # 故障ロボット共通の向き
    n_faulty = len(broken)
    n_normal = n - n_faulty

    total = 0
    for c in s:
        if c == 'R':
            normal = (normal + 1) % 4
            faulty = (faulty - 1) % 4
        elif c == 'L':
            normal = (normal - 1) % 4
            faulty = (faulty + 1) % 4
        else:  # 'A'
            normal = (normal + 2) % 4
            faulty = (faulty + 2) % 4

        if normal == faulty:
            total += n
        else:
            total += max(n_normal, n_faulty)
    return total
```

#### 解説

素直に書くとN台それぞれの向きを配列で持ち、指示のたびに全台更新するO(N×|S|)のシミュレーションになるが、制約(どちらも10^5)では最悪10^10回の更新となりTLEする。**鍵は「正常な全ロボットは常に同じ向き、故障した全ロボットも常に同じ向き」という不変条件に気づくこと**。

- **なぜ同じ向きになるか**: 全ロボットは同じ北向きから始まり、正常なロボット同士は毎回まったく同じ回転を適用される。初期状態が同じで遷移も同じなら、状態は永遠に一致し続ける。故障ロボット同士も同様。つまり存在する向きは高々2種類(正常群の向き・故障群の向き)しかなく、追跡すべき状態は `normal` と `faulty` の2変数だけ。O(|S|)・追加メモリO(1)で解ける。
- **台数の数え方**: 向きが高々2種類しかないので、「同じ向きを向いている最大台数」は、2群が揃っていれば全 `n` 台、揃っていなければ**大きい方の群の台数** `max(n_normal, n_faulty)`。台数は答えに効くが、群ごとの頭数を最初に数えておくだけで、指示ごとの計算はO(1)のまま。
- **端ケースが自然に消える**: 片方の群が空(故障0台/全台故障)の場合、`max(n_normal, n_faulty)` がそのまま `n` になるため、`normal == faulty` かどうかに関係なく正しい値が加算される。特別扱いのガードが不要になるのは、この「maxで数える」設計の副産物。
- **向きの表現**: 0〜3の整数と `% 4` で回転を表すと、`R`=+1、`L`=−1、`A`=+2 が統一的に書ける。Pythonの `%` は負数でも非負を返すので `(x - 1) % 4` がそのまま使える(言語によっては負になるので注意)。

`"RLAARR"`, `broken=[2]`（正常2台・故障1台）のトレース:

| 指示 | normal | faulty | 揃う? | 加算(最大台数) |
|---|---|---|---|---|
| R | 東(1) | 西(3) | ✗ | 2 |
| L | 北(0) | 北(0) | ✓ | 3 |
| A | 南(2) | 南(2) | ✓ | 3 |
| A | 北(0) | 北(0) | ✓ | 3 |
| R | 東(1) | 西(3) | ✗ | 2 |
| R | 南(2) | 南(2) | ✓ | 3 |

合計で答えは `16`。

さらに抽象化すると、揃っているかどうかは2群の**相対角**(normal − faulty)だけで決まる。`A`（反転）は両群に+180度ずつ同じ作用をするので相対角を変えず、`R`/`L` は一方に+90度・他方に−90度なので相対角を±180度動かす。つまり「これまでのR/Lの総数が偶数なら揃っている」ところまで単純化でき、実装の検算に使える。たとえば `count_aligned(4, [1], "RR")` が `7` になるのは、1回目のRで相対角180(正常3台のみ揃い +3)、2回目のRで 180+180=360≡0(全4台が揃い +4)となるから。

---

### 問6. Maxスタック記録【スタック／easy-medium】

#### 解答

```python
def process_max_stack(instructions: list[str]) -> list[int]:
    stack = []      # (値, その時点の最大値) のペアを積む
    result = []
    for inst in instructions:
        if inst.startswith("push"):
            x = int(inst.split()[1])
            cur_max = max(x, stack[-1][1]) if stack else x
            stack.append((x, cur_max))
        elif inst == "pop":
            if stack:
                stack.pop()
        elif inst == "max":
            if stack:
                result.append(stack[-1][1])
    return result
```

#### 解説

各要素に「自分を積んだ時点でのスタック全体の最大値」をペアで持たせるのが定石。これで不変条件「`stack[-1][1]` は常に現在のスタックの最大値」が維持される。

- **計算量**: `push`/`pop`/`max` すべてO(1)。メモリは2倍になるがオーダーはO(n)のまま。
- **愚直解との比較**: `max` のたびに `max(stack)` を走査するO(n)解でも、この制約なら通ることが多い。min stack は `max` を `min` に変えるだけの同型問題。
- **実装の注意**: 指示のパースは `startswith("push")` + `split()` で。空スタックへの `pop`/`max` は「無視」という仕様を読み落とさないこと。

---

### 問7. カッコ列の最大深さ【状態管理／easy】

#### 解答

```python
def max_depth(s: str) -> int:
    depth = max_d = 0
    for c in s:
        depth += 1 if c == '(' else -1
        if depth < 0:
            return -1
        max_d = max(max_d, depth)
    return max_d if depth == 0 else -1
```

#### 解説

スタックを実際に積む必要はなく、「現在の深さ」を表すカウンタ1つで足りる。`(` で+1、`)` で−1しながら、これまでの最大値を記録するだけ。

- **不正の2条件は独立**: ①「途中で深さが負になる」は `")("` のように閉じ括弧が先行するケースで、見つけた瞬間に `-1` を返して打ち切れる。②「最後に深さが0に戻らない」は `"(("` のように開きっぱなしのケースで、走査が終わるまで判定できない。この2つは検出タイミングが違うので、片方だけで済ませようとしないこと。特に①を省いて最後の `depth == 0` だけにすると、`")("`（合計は0）を誤って正当と判定してしまう。
- **空文字列**: ループが回らず `max_d = 0`, `depth = 0` なので自然に `0` が返る。
- **計算量**: O(n)、追加メモリO(1)。
- カッコ検証・ネスト深さ系の問題は、問5と同じ「1文字ずつ読んで状態を更新する」基本形の変種として整理しておくと応用が利く。

---

### 問8. キュー操作シミュレーション【データ構造／easy】

#### 解答

```python
from collections import deque

def process_queue(instructions: list[str]) -> list[int]:
    q = deque()
    result = []
    for inst in instructions:
        if inst.startswith("enq"):
            q.append(int(inst.split()[1]))
        elif inst == "deq":
            result.append(q.popleft() if q else -1)
        elif inst == "front":
            result.append(q[0] if q else -1)
    return result
```

#### 解説

入力例のトレース: `enq 1`, `enq 2` の後、`front→1`（先頭を見るだけで削除しない）, `deq→1`, `deq→2`, 空になってからの `deq→-1` で `[1, 1, 2, -1]`。

- **`deque` を使う理由**: `list.pop(0)` は先頭を削除した後に残りの全要素を1つずつ前へ詰め直すためO(n)。指示が10^5件あると最悪O(n²)になる。`collections.deque` は両端の追加・削除がO(1)なので、Pythonでキューを書くならこれが標準。
- **仕様の細部が得点差になる**: ①指示のパースは `startswith("enq")` で分岐して `split()[1]` を `int` に変換、②`deq`/`front` の空チェックでは例外を投げず `-1` を**記録**する、③`front` は削除しない——アルゴリズムに難所はなく、この写経の正確さが問われている。
- **計算量**: 全体O(指示数)。

---

### 問9. 縦読み結合【文字列／easy】

#### 解答

```python
def interleave(words: list[str]) -> str:
    result = []
    max_len = max(map(len, words)) if words else 0
    for i in range(max_len):
        for w in words:
            if i < len(w):
                result.append(w[i])
    return "".join(result)
```

#### 解説

`["abc", "de", "fghi"]` を列ごとに読むと、1文字目 `a,d,f` → 2文字目 `b,e,g` → 3文字目 `c,h`（`de` は尽きたのでスキップ）→ 4文字目 `i` で **`"adfbegchi"`**。「長さが足りない文字列はスキップ」の一文を `if i < len(w)` という境界チェックに正確に落とせるかが核心で、必ず自分の手でトレースして確認する。

- **ループの設計**: 外側を「文字位置 `i`」、内側を「単語 `w`」にするのが素直(逆にすると出力順が変わる)。終了条件は最長単語の長さ `max_len`。`words` が空だと `max()` が例外を投げるので `if words else 0` のガードが必要——見落としやすいエッジケース。
- **文字列連結のコスト**: ループ内で `result += c` と str に足し込むと、不変オブジェクトの再生成が繰り返され最悪O(n²)。リストに `append` して最後に `"".join()` が保証つきのO(n)。この癖は文字列問題全般で効く。

---

### 問10. 4で割り切れる部分文字列【数え上げ／easy-medium】

#### 解答1: 数値を差分更新するO(n²)全列挙

```python
def count_div4_substrings(s: str) -> int:
    n = len(s)
    count = 0
    for i in range(n):
        if s[i] == '0':
            count += 1          # "0" 単体のみ許可
            continue
        num = 0
        for j in range(i, n):
            num = num * 10 + int(s[j])
            if num % 4 == 0:
                count += 1
    return count
```

開始位置 `i` を固定し、終了位置 `j` を右へ伸ばしながら `num = num * 10 + int(s[j])` と数値を**差分更新**するのがポイント。各部分文字列を `int(s[i:j+1])` と切り出して変換し直すと、変換自体がO(長さ)かかって全体O(n³)に落ちる。差分更新ならO(n²)。

- **先頭0の処理**: 「開始文字が `'0'` なら単体の `"0"` だけカウントし、内側ループに入らず打ち切る」で仕様を満たせる。`"400"` の答えが `5`（`4`, `40`, `400`, 位置1の `0`, 位置2の `0`）になることを手でトレースし、`0` が2箇所それぞれ独立にカウントされる感覚を確認しておくとよい。
- **桁あふれ**: Pythonの `int` は多倍長なのでそのまま伸ばして問題ないが、固定長整数の言語では `num` が溢れる。判定に必要なのは `num % 4` だけなので `num = (num * 10 + d) % 4` と mod を取りながら伸ばせば良い。

#### 解答2: 下2桁判定によるO(n)解

100は4の倍数なので、**4で割り切れるかは下2桁だけで決まる**。これを使うと終了位置 `j` ごとにO(1)で数えられる。

- 長さ1: `s[j]` が `0/4/8` なら +1。
- 長さ2以上: `s[k..j]`（`k <= j-1`）が4の倍数かは末尾2桁 `s[j-1..j]` だけで決まる。この2桁が4の倍数なら、開始位置の候補数「`0..j-1` のうち `s[k] != '0'` の個数」（先頭0の除外）をまとめて加算する。この個数は非 `'0'` 文字の累積カウントを持てばO(1)で引ける。

```python
def count_div4_substrings_linear(s: str) -> int:
    count = 0
    nonzero_prefix = 0  # s[0..j-1] のうち '0' でない文字の数
    for j, c in enumerate(s):
        if int(c) % 4 == 0:                     # 長さ1: "0", "4", "8"
            count += 1
        if j >= 1 and int(s[j-1:j+1]) % 4 == 0:  # 長さ2以上: 下2桁で判定
            count += nonzero_prefix              # 開始位置は 0..j-1 の非'0'文字
        if c != '0':
            nonzero_prefix += 1
    return count
```

---

### 問11. 重複なし最長部分文字列【文字列／medium】

#### 解答1: whileで縮めるスライディングウィンドウ

```python
def longest_unique_substring(s: str) -> int:
    window = set()  # ウィンドウ内にある文字の集合
    left = 0        # ウィンドウ左端
    best = 0
    for right, c in enumerate(s):
        while c in window:
            window.remove(s[left])
            left += 1
        window.add(c)
        best = max(best, right - left + 1)
    return best
```

**スライディングウィンドウ(2ポインタ)** の代表問題。「重複を含まない」という性質は、ウィンドウを縮めれば必ず回復する(単調性がある)ため、左端 `left` と右端 `right` を一方向にしか動かさない設計が成立する。

- **不変条件**: 各周回の終わりで「`s[left..right]` は重複なし」を保つ。右端に文字 `c` を足そうとしたとき、`c` がすでにウィンドウ内にいれば、`c` の古い出現が消えるまで左端から1文字ずつ取り除いて縮める。whileを抜けた時点で重複が解消されているので、安心して `c` を追加できる。
- **なぜO(n)か**: whileが入れ子になっていて一見O(n²)に見えるが、**各文字はウィンドウに高々1回入り、高々1回しか出ない**。追加n回・削除最大n回で合計の仕事量は2nに抑えられる(償却O(1))。この「入れ子ループでも合計回数で数えれば線形」という見方はウィンドウ問題共通の考え方。
- **`"abba"` のトレース**: `a`, `ab` と伸びた後、2つ目の `b` で左端が2まで縮んで `b`、次の `a` は `window = {b}` に無いのでそのまま `ba` に伸びる。答えは2。左端が自然に「戻らない」構造になっているのがこの実装の利点。
- **全探索との比較**: 開始×終了の全組み合わせはO(n²)本あり、重複チェックまで愚直にやるとO(n³)。setで判定を均してもO(n²)で、10^5 では間に合わない。「条件が壊れたときに左端を進めて候補を枝刈りする」のがこの問題の学び。

#### 解答2: ジャンプ版(last_seen辞書)

「文字 → 最後に見た位置」の辞書 `last_seen` を持ち、重複を見つけたら左端を「前回の出現位置+1」まで一気にジャンプさせる実装。1文字ずつ縮める処理が消える代わりに、`last_seen[c] >= left` というガード条件が必要になる。これを忘れると `"abba"` の最後の `a` で左端が1まで**左に戻り**、重複入りのウィンドウを最長と誤認する。解答1にはこの罠が構造的に存在しないため、まずは解答1を確実に書けるようにするのが安全。

```python
def longest_unique_substring_jump(s: str) -> int:
    last_seen = {}  # 文字 -> 最後に見た位置
    left = 0
    best = 0
    for right, c in enumerate(s):
        if c in last_seen and last_seen[c] >= left:
            left = last_seen[c] + 1
        last_seen[c] = right
        best = max(best, right - left + 1)
    return best
```

---

### 問12. 文字集合一致カウント【ビットマスク／easy-medium】

本質は **「使われている文字の集合」を比較しやすい正規形(canonical form)に写してから突き合わせる** こと。正規形の選び方で2通りの解答がある。

#### 解答1: ビットマスク正規形

```python
def count_similar(w: str, words: list[str]) -> int:
    def mask(word):
        m = 0
        for c in word:
            m |= 1 << (ord(c.lower()) - ord('a'))
        return m

    target = mask(w)
    return sum(1 for word in words if mask(word) == target)
```

26種のアルファベットを26bitの整数に畳み込み、単語同士の比較を整数の `==` 1回にする。

- **他の正規形**: `frozenset(word)`（辞書のキーにできる）、`"".join(sorted(set(word)))`（文字列キー）も同じ発想。ソート版は一見O(k log k)だが k≤26 なので実質定数。どれを選んでも「正規化してから比較」という構造は共通で、アナグラム判定で `sorted(word)` や頻度タプルをキーにするのと同型のパターンとして整理しておく。
- **クエリが繰り返される場合の拡張**: 同じ `words` に多数の `w` が来るなら、先に `Counter(mask(word) for word in words)` を作っておけば各クエリは `counts[mask(w)]` で O(len(w)) で答えられる。
- **細部の注意**: `.lower()` を忘れると大文字混在の入力で不一致になる。アルファベット以外の文字が来る可能性がある場合は `ord(c) - ord('a')` が範囲外になるので、入力の前提を最初に確認すること。

#### 解答2: set正規形

```python
def count_similar_set(w: str, words: list[str]) -> int:
    target = set(w.lower())
    return sum(1 for word in words if set(word.lower()) == target)
```

- **正しさは完全に等価**: setの `==` は「要素の集合として一致するか」を見るので、意味論は解答1と同じ。こちらを書いても不正解にはならない。
- **漸近計算量も実は同じ**: どちらも各単語を1回走査するO(合計文字数)。比較コストも、集合の要素数が高々26に抑えられているためset比較はO(26)=O(1)。**オーダーでは差がつかない**。
- **差がつくのは定数倍とメモリ**: set版は単語ごとにsetオブジェクトの生成とハッシュ計算が入るぶん遅く、メモリも多く使う。ビットマスク版は整数演算だけなので、同じO(合計文字数)でも数倍速いことが多い。これができるのは文字の種類が高々26でintのビットに収まるからで、種類が多い場合は素直にsetを使う。

---

### 問13. 3桁区切りカンマ挿入【文字列整形／easy-medium】

#### 解答

```python
def add_commas(s: str) -> str:
    sign = ""
    if s[0] in "+-":
        sign, s = s[0], s[1:]
    int_part, dot, frac = s.partition(".")

    out = []
    for i, c in enumerate(reversed(int_part)):
        if i > 0 and i % 3 == 0:
            out.append(",")
        out.append(c)
    return sign + "".join(reversed(out)) + dot + frac
```

#### 解説

手順は「①符号を退避 → ②小数点で整数部と小数部に分離 → ③整数部だけを右から3桁ごとに区切る → ④符号・小数部を復元」。**加工対象だけを切り出し、加工して、元に戻す**という文字列整形の典型構造で、この分解を最初に言語化できるかが設計力の見せ所。

- **なぜ右から走査するか**: カンマは「右端から3桁ごと」に入るため、左から入れようとすると「先頭ブロックの桁数 = 全体の桁数 mod 3」という場合分けが要る。`reversed` で右から数えれば「3の倍数番目の手前に挿入」だけで済み、場合分けが消える。最後にもう一度 `reversed` で戻す。
- **`partition` の利点**: `s.partition(".")` は小数点がない場合 `(s, "", "")` を返すため、「小数点あり/なし」を同じコードで扱える。`split(".")` だと戻り値の要素数で場合分けが必要になる。
- **エッジケース**: `"100"`（3桁ちょうど・挿入なし）、`"-0.5"`（符号+小数のみ）、`"1000000"`（カンマ複数）、`"+12345"`（正符号）を提出前に手で確認する。

---

### 問14. 重複文字種カウント【頻度Map／easy】

#### 解答

```python
from collections import Counter

def count_duplicated_kinds(s: str) -> int:
    return sum(1 for v in Counter(s).values() if v >= 2)
```

#### 解説

頻度Map（`Counter`）を作り、「出現回数が2以上の**キーの個数**」を数えるだけ。`"foobarbaz"` は `f:1, o:2, b:2, a:3, r:1, z:1` なので、2回以上は `o, b, a` の `3` 種類。

- **「種類数」と「総数」の読み分け**: 問われているのは重複している文字の**種類**であって、重複した文字の延べ出現数ではない。`"aaa"` の答えが `1`（aという1種類）であることを最初に確認して、仕様の解釈を固定してから書き始める。
- **計算量**: `Counter(s)` の構築O(n) + 値の走査O(種類数)。追加メモリもO(種類数)。
- `Counter` を使わなくても、普通の辞書で `d[c] = d.get(c, 0) + 1` と数えるだけ。この問題は1〜2分で書き切り、浮いた時間を問5や問10のような重い問題に回すのが正しい時間配分。

---

### 問15. evict付きキャッシュ実装【データ構造／medium】

#### 解答

```python
from collections import OrderedDict

class Cache:
    def __init__(self):
        self.data = OrderedDict()  # 末尾 = 最近アクセス

    def add(self, key: int, value: int) -> None:
        self.data[key] = value
        self.data.move_to_end(key)

    def get(self, key: int) -> int:
        if key not in self.data:
            raise KeyError(key)
        self.data.move_to_end(key)
        return self.data[key]

    def remove(self, key: int) -> int:
        if key not in self.data:
            raise KeyError(key)
        return self.data.pop(key)

    def evict(self) -> None:
        if self.data:
            self.data.popitem(last=False)  # 先頭 = 最古アクセス
```

#### 解説

「最後にアクセスされてから最も時間が経った要素を消す」= **LRU (Least Recently Used)** の骨格そのもの。必要なのは「キー→値の対応」と「アクセスの新しさ順」という2つの情報を、どちらもO(1)で保つこと。

- **`OrderedDict` での実現**: 順序つき辞書に `move_to_end(key)`（末尾=最新へ移動、O(1)）と `popitem(last=False)`（先頭=最古を削除、O(1)）が揃っているので、「`add`/`get` のたびに `move_to_end`」「`evict` で先頭を落とす」だけでアクセス順管理が完成する。Python 3.7以降は普通の `dict` も挿入順を保つが、既存キーを末尾へ動かす操作がない(いったん `del` して入れ直すことになる)ため、アクセス順の管理には `OrderedDict` が適任。Javaなら `LinkedHashMap(accessOrder=true)` が同じ役割。
- **自作する場合**: **HashMap + 双方向リンクリスト**が標準構成。HashMapでキー→ノードをO(1)で引き、リンクリストの並び順で新しさを表す。アクセスしたノードは前後を繋ぎ替えて末尾へ移動(O(1))、evictは先頭ノードを外すだけ(O(1))。双方向にするのは、任意位置のノードをO(1)で抜くのに前方向のポインタも必要だから。
- **なぜ配列＋タイムスタンプではダメか**: 各要素に最終アクセス時刻を持たせる設計だと、evict時に最小タイムスタンプの線形探索が必要でO(n)。ヒープで管理しようとしても、アクセスのたびに既存要素のキー更新が発生して素朴な実装では崩れる。
- **仕様の細部**: `add` は既存キーの上書きも「アクセス」扱い(順序の更新が必要)、`get`/`remove` は不在キーで `KeyError`、`evict` は空なら何もしない——落ちやすいのはこの辺り。

---

### 問16. キュービック・ハッピー数【数値／easy-medium】

#### 解答

```python
def is_cubic_happy(n: int) -> bool:
    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = sum(int(d) ** 3 for d in str(n))
    return True
```

#### 解説

ハッピーナンバー系の骨格は「①1ステップの変換関数 ②ループ検出」の2部品で、変換が各桁の2乗和でも3乗和でも構造は変わらない。変換は `sum(int(d) ** 3 for d in str(n))` と文字列経由で書くのが手早い(10で割りながら桁を取り出す方法でも良い)。

- **ループ検出**: 訪問済みの値を `set` に貯め、再訪したら `False`。
- **トレース例**: `2 → 8 → 512 → 134 → 92 → 737 → 713 → 371 → 371 → ...` と `371` の自己ループ（`3³+7³+1³ = 371`）に捕まるので `False`。`153` は `1³+5³+3³ = 153` で自分自身に戻る有名な数(アームストロング数)なので即 `False`。

補足: 変換後の値は最大でも `729 × 桁数`（全桁9のとき）にしかならないので、大きい数は必ず縮んで有限の範囲に閉じ込められる。よって「1に到達」か「ループ」のどちらかが有限回で必ず起きる。

---

### 問17. 3数の積の最大値【ソート＋エッジケース／easy-medium】

#### 解答

```python
def max_product_of_three(nums: list[int]) -> int:
    if len(nums) < 3:
        return -1
    nums.sort()
    return max(
        nums[-1] * nums[-2] * nums[-3],   # 最大3つ
        nums[0] * nums[1] * nums[-1],     # 最小2つ(負×負) × 最大1つ
    )
```

#### 解説

「大きい方から3つ」だけでは、`(-10) × (-10) = 100` のような**負×負＝正**の跳ね上がりを取りこぼす。ソート後に候補が2通りへ絞れる理由を整理する:

- 積を最大にする組は必ず最大値 `nums[-1]` を含む(と仮定してよい)。残り2つに必要なのは「ペアとしての積が最大」で、その候補は「大きい正数2つ `nums[-2], nums[-3]`」か「絶対値の大きい負数2つ `nums[0], nums[1]`」のどちらかしかない。中途半端な組み合わせ(負1つ+正1つなど)がこの2つを上回ることはない。
- 全要素が負のケースも、絶対値の小さい上位3つ（例: `[-5,-4,-3,-2]` なら `(-4)×(-3)×(-2) = -24`）が最良で、候補①に自然に含まれる。

よって `max(上位3つの積, 下位2つ × 最大値)` で全ケースを覆える。`[-10, -10, 1, 3, 2]` なら `max(1×2×3, (-10)×(-10)×3) = max(6, 300) = 300`。

- **計算量**: ソートO(n log n)で十分。O(n)にしたければ「最大3つ・最小2つ」を1パスで追跡すれば良いが、変数5本の更新はバグりやすいので本番はソート推奨。
- **実装の注意**: `nums.sort()` は呼び出し元のリストを破壊する。副作用を避けたい場面では `nums = sorted(nums)` にする。要素数チェック(3未満で `-1`)は先頭に置く。

---

### 問18. 正方形の最大辺長【集計／easy】

#### 解答

```python
from collections import Counter

def max_square_side(sticks: list[int]) -> int:
    candidates = [length for length, c in Counter(sticks).items() if c >= 4]
    return max(candidates) if candidates else -1
```

#### 解説

正方形1つに必要なのは「同じ長さの棒が4本以上」なので、頻度Map（`Counter`）で長さごとの本数を数え、「4本以上ある長さ」を候補に集めて最大を返すだけ。候補が空なら `-1`。

- **入力例の確認**: `[3,5,5,3,5,5,3,3,3]` は 3が5本・5が**4本**。どちらも4本以上あるので両方の正方形が作れ、答えは大きい方の `5`。サンプルの本数は数え間違えやすいので、**本番でも問題文の例を鵜呑みにせず自分で数え直す**こと。自分のトレースと期待値が食い違ったら、まず自分の数え間違いを疑い、それでも合わなければ仕様の解釈(「以上」か「ちょうど」かなど)を再確認する。
- **計算量**: Counter構築O(n) + 候補走査O(種類数) = O(n)。
- **仕様の確認ポイント**: 「作るのは正方形1つ」であって「8本あれば2つ作れる」問題ではない。もし「作れる正方形の総数」を問う変種なら各長さの `count // 4` の総和になる。問われているのが「最大辺長」か「個数」かを最初に確定させる。

---

### 問19. SQL: JOIN + 絞り込み + DISTINCT + ORDER【SQL／easy-medium】

このクエリの急所は**1対多のJOINで結果の行数が膨らむこと**。`assignments` は1人につき複数行あり得るため、素直にJOINすると「Satoがプロジェクトの数だけ複数行」出力されてしまう。求められているのは「アサインが1つ以上あるか」という**存在の有無**だけなので、膨らんだ行への対処が2通りの解答を分ける。

#### 解答1: JOIN + DISTINCT

```sql
SELECT DISTINCT
    e.name,
    d.dept_name
FROM employees e
JOIN departments d ON d.id = e.department_id
JOIN assignments a ON a.employee_id = e.id
WHERE d.location = 'Tokyo'
ORDER BY e.name ASC;
```

膨らんだ行を `DISTINCT` で1行に畳む素直な書き方。

- **`DISTINCT` の位置づけ**: `SELECT DISTINCT` は最終的な射影結果(`name, dept_name` の組)に対して働く。JOIN → WHERE → SELECT → DISTINCT → ORDER BY という論理的な評価順序をイメージできると、「どこで重複が生まれ、どこで消えるか」を説明できる。

#### 解答2: EXISTS

```sql
SELECT e.name, d.dept_name
FROM employees e
JOIN departments d ON d.id = e.department_id
WHERE d.location = 'Tokyo'
  AND EXISTS (SELECT 1 FROM assignments a WHERE a.employee_id = e.id)
ORDER BY e.name;
```

「1つ以上存在する」は本来、行を増やす操作ではなく**絞り込み条件**。`EXISTS` サブクエリなら行が膨らまないため `DISTINCT` が不要になり、「存在確認がしたい」という意図もSQLから読み取りやすい。`assignments.employee_id` にインデックスがあれば最初の1件で探索を打ち切れるため、性能面でも有利なことが多い。

---

### 問20. SQL: JOIN + 集計 + HAVING + ORDER【SQL／medium】

#### 解答

```sql
SELECT
    u.name,
    COUNT(*)      AS order_count,
    SUM(o.amount) AS total_amount
FROM users u
JOIN orders o ON o.user_id = u.id
WHERE o.ordered_at >= '2025-01-01'
  AND o.ordered_at <  '2026-01-01'
GROUP BY u.id, u.name
HAVING COUNT(*) >= 3
ORDER BY total_amount DESC, u.name ASC;
```

#### 解説

頻出の落とし穴が3つ詰まった総合問題。

1. **`WHERE` と `HAVING` の使い分け**: `WHERE` はグループ化の**前**に行を絞り、`HAVING` はグループ化の**後**に集計値で絞る。「2025年の注文」は行単位の条件なので `WHERE`、「3回以上」は `COUNT(*)` という集計結果への条件なので `HAVING`。`WHERE COUNT(*) >= 3` は構文エラーになり、逆に年条件を `HAVING` に回すと集計対象に2024年の注文が混ざって答えが変わる(Tanakaの合計が11000になってしまう)。
2. **日付は半開区間で**: `YEAR(ordered_at) = 2025` のように列を関数で包むと、多くのDBで `ordered_at` のインデックスが使えなくなる。`>= '2025-01-01' AND < '2026-01-01'` という**半開区間**なら範囲スキャンが効き、「2025-12-31の23:59:59.999…をどう書くか」というタイムスタンプ境界の悩みも消える。日付範囲は常に「以上・未満」で書く癖をつける。
3. **`GROUP BY u.id, u.name`**: `u.name` だけでグループ化すると同姓同名のユーザーが1グループに混ざり、集計が壊れる。主キーの `u.id` を軸にし、SELECTに出す `u.name` も併記するのが標準SQL準拠で移植性も高い。

仕上げに `ORDER BY total_amount DESC, u.name ASC` の**第2キー**まで指示どおりかを確認する。並び順の第2キー漏れは「動くのに減点される」典型なので、提出前チェックの項目としてルーチン化しておく。
