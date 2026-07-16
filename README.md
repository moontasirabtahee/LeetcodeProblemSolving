# 🧠 LeetCode Problem Solving

> A collection of **48 LeetCode solutions** in Python, covering **Arrays, Strings, Linked Lists, Binary Trees, Math, and Matrix** problems — with both brute-force and optimized approaches.

---

## 📋 Table of Contents

- [Repository Overview](#-repository-overview)
- [Statistics Dashboard](#-statistics-dashboard)
- [Problem Categories & Solutions](#-problem-categories--solutions)
  - [Arrays](#-arrays-15-problems)
  - [Strings](#-strings-13-problems)
  - [Linked Lists](#-linked-lists-4-problems)
  - [Binary Trees](#-binary-trees-7-problems)
  - [Math & Number Theory](#-math--number-theory-7-problems)
  - [Matrix](#-matrix-3-problems)
- [Techniques & Patterns Used](#-techniques--patterns-used)
- [Solution Highlights](#-solution-highlights)
- [How to Run](#-how-to-run)

---

## 🔬 Repository Overview

```
┌──────────────────────────────────────────────────────────────────────┐
│                   LEETCODE PROBLEM SOLVING                          │
│                                                                      │
│   Language: Python          Total Problems: 48                       │
│   Difficulty: Easy / Medium                                          │
│                                                                      │
│   ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐              │
│   │  Arrays   │ │ Strings  │ │  Trees   │ │  Linked  │              │
│   │    15     │ │    13    │ │    7     │ │  Lists 4 │              │
│   └──────────┘ └──────────┘ └──────────┘ └──────────┘              │
│                                                                      │
│   ┌──────────┐ ┌──────────┐                                         │
│   │   Math   │ │  Matrix  │                                         │
│   │    7     │ │    3     │                                         │
│   └──────────┘ └──────────┘                                         │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 📊 Statistics Dashboard

```
DIFFICULTY DISTRIBUTION                    CATEGORY BREAKDOWN
═══════════════════════                    ══════════════════

  Easy   ████████████████████████  37       Arrays    ██████████████████  15
  Medium ████████████              11       Strings   ████████████████    13
                                            Trees     ████████████        7
                                            Math      ████████████        7
ACCEPTANCE                                  Linked    ██████              4
═══════════                                 Matrix    ██████              3
  ✅ Solved    48
  📝 Multiple  8  (problems with 2+ approaches)
```

### Problems with Multiple Approaches

| # | Problem | Approaches |
|---|---------|------------|
| 26 | Remove Duplicates from Sorted Array | Two-pointer, Set-based |
| 94 | Binary Tree Inorder Traversal | Recursive, Iterative (Stack) |
| 100 | Same Tree | DFS (Value-only, commented), Recursive (Structure-aware) |
| 144 | Binary Tree Preorder Traversal | Recursive, Iterative (Stack) |
| 145 | Binary Tree Postorder Traversal | Recursive, Iterative (Reversed Stack) |
| 189 | Rotate Array | Slicing (3 attempts → optimized) |
| 1108 | Defanging an IP Address | `replace()`, `split()`+`join()` |

---

## 📂 Problem Categories & Solutions

### 📦 Arrays (15 Problems)

```
ARRAY TECHNIQUES WIREFRAME
═══════════════════════════════════════════════════════════

  TWO-POINTER PATTERN              IN-PLACE MODIFICATION
  ─────────────────────            ──────────────────────
  [1, 1, 2, 3, 3]                 [3, 2, 2, 3] val=3
   ↑              ↑                ↑
   slow           fast              i,j scan → overwrite
   → skip dups, compact            → compact non-val items

  PREFIX/SUFFIX PRODUCT            XOR BIT MANIPULATION
  ─────────────────────            ──────────────────────
  [1, 2, 3, 4]                    [4, 1, 2, 1, 2]
  L→ [1, 1, 2, 6]                 4^1^2^1^2 = 4
  R← [24,12, 4, 1]                pairs cancel → single
  ans= L × R per index             number survives
```

| # | Problem | Difficulty | Technique | Key Code |
|---|---------|------------|-----------|----------|
| 26 | Remove Duplicates from Sorted Array | 🟢 Easy | Two Pointers / Set | `sorted(set(nums))` |
| 27 | Remove Element | 🟢 Easy | Two Pointers | In-place overwrite with `i, j` scan |
| 48 | Rotate Image | 🟡 Medium | Transpose + Reverse | `matrix[i][j], matrix[j][i] = swap` then `reverse()` |
| 54 | Spiral Matrix | 🟡 Medium | Boundary Shrinking | *(stub — in progress)* |
| 80 | Remove Duplicates from Sorted Array II | 🟡 Medium | Two Pointers + Counter | Allow `count < 2` duplicates |
| 136 | Single Number | 🟢 Easy | XOR | `miss ^= i` — pairs cancel out |
| 189 | Rotate Array | 🟡 Medium | Slicing | `nums[-k:] + nums[:-k]` with `k % len` |
| 238 | Product of Array Except Self | 🟡 Medium | Prefix/Suffix Product | Left pass → Right pass, O(n) no division |
| 268 | Missing Number | 🟢 Easy | Math (Gauss Sum) | `n*(n+1)//2 - sum(nums)` |
| 442 | Find All Duplicates in an Array | 🟡 Medium | Index Negation | Negate `nums[abs(i)-1]`; if already neg → duplicate |
| 448 | Find All Numbers Disappeared | 🟢 Easy | Set Difference | `set(range) - set(nums)` |
| 1480 | Running Sum of 1d Array | 🟢 Easy | Prefix Sum | Cumulative `sum += nums[i]` |
| 1486 | XOR Operation in an Array | 🟢 Easy | XOR | `ans ^= (start + 2*i)` |
| 1752 | Check if Array Is Sorted and Rotated | 🟢 Easy | Inversion Count | Count `nums[i] > nums[(i+1)%n]`; valid if ≤ 1 |
| 2011 | Final Value After Operations | 🟢 Easy | Simulation | `++X/X++` → +1, `--X/X--` → -1 |

---

### 🔤 Strings (13 Problems)

```
STRING TECHNIQUES WIREFRAME
═══════════════════════════════════════════════════════════

  PALINDROME CHECK                  REVERSED STRING MATCH
  ──────────────────                ──────────────────────
  "A man, a plan..."               "abab" + "abab" = "abababab"
    ↓ lowercase                              ↓ [1:-1]
    ↓ filter alnum                       "babababa"
  "amanaplana..."                    "abab" found in it?
    == reversed? ✓                   → YES = repeated pattern

  PREFIX MATCHING (zip)             WORD REVERSAL
  ─────────────────────             ──────────────────────
  ["flower","flow","flight"]        "  hello world  "
    f l o w e r                       ↓ strip
    f l o w                         "hello world"
    f l i g h t                       ↓ split → reverse
    ─── ───                         ["world", "hello"]
    f l ← common prefix              ↓ join
                                    "world hello"
```

| # | Problem | Difficulty | Technique | Key Code |
|---|---------|------------|-----------|----------|
| 13 | Roman to Integer | 🟢 Easy | Hash Map + Subtraction Rule | If `val[i-1] < val[i]` → subtract |
| 14 | Longest Common Prefix | 🟢 Easy | Zip + Set | `zip(*strs)` → check `len(set(col))==1` |
| 28 | Find First Occurrence in String | 🟢 Easy | Built-in | `haystack.index(needle)` |
| 58 | Length of Last Word | 🟢 Easy | Strip + Split | `s.strip().split()[-1]` |
| 125 | Valid Palindrome | 🟢 Easy | Filter + Reverse | `isalnum()` filter, `s == s[::-1]` |
| 151 | Reverse Words in a String | 🟡 Medium | Split + Reverse + Filter | Strip → split → reverse → filter empty |
| 344 | Reverse String | 🟢 Easy | In-place Slice | `s[:] = s[::-1]` |
| 387 | First Unique Character | 🟢 Easy | Counter | `Counter(s)` → first with `count == 1` |
| 459 | Repeated Substring Pattern | 🟢 Easy | String Doubling | `s in (s+s)[1:-1]` |
| 1108 | Defanging an IP Address | 🟢 Easy | Replace / Split+Join | `.replace(".", "[.]")` |
| 1455 | Prefix of Any Word | 🟢 Easy | startswith | `array[i].startswith(searchWord)` |
| 2062 | Count Vowel Substrings | 🟢 Easy | Brute Force + Set | All substrings → check vowel set equality |
| 2108 | First Palindromic String | 🟢 Easy | Linear Scan | `i == i[::-1]` |

---

### 🔗 Linked Lists (4 Problems)

```
LINKED LIST TECHNIQUES WIREFRAME
═══════════════════════════════════════════════════════════

  REVERSE LINKED LIST                  CYCLE DETECTION
  ────────────────────                 ─────────────────
  1 → 2 → 3 → 4 → None               1 → 2 → 3 → 4
                                                ↑     │
  prev=None, cur=1                              └─────┘
    1 → None                           slow: 1→2→3→4→3
    2 → 1 → None                       fast: 1→3→3→3 ← meet!
    3 → 2 → 1 → None                   fast == slow → CYCLE ✓
    4 → 3 → 2 → 1 → None

  INTERSECTION OF TWO LISTS
  ─────────────────────────
  A: a1 → a2 ↘
              → c1 → c2 → c3
  B: b1 → b2 → b3 ↗

  Pointer a: a1→a2→c1→c2→c3→b1→b2→b3→c1 ← meet!
  Pointer b: b1→b2→b3→c1→c2→c3→a1→a2→c1 ← meet!
```

| # | Problem | Difficulty | Technique | Key Code |
|---|---------|------------|-----------|----------|
| 141 | Linked List Cycle | 🟢 Easy | Floyd's Slow/Fast | `slow = slow.next; fast = fast.next.next` |
| 160 | Intersection of Two Linked Lists | 🟢 Easy | Two-pointer Swap | `a = a.next if a else headB` |
| 206 | Reverse Linked List | 🟢 Easy | Iterative Reversal | `prev ← current ← next` pointer swap |

---

### 🌳 Binary Trees (7 Problems)

```
BINARY TREE TRAVERSAL WIREFRAME
═══════════════════════════════════════════════════════════

  Example Tree:          Traversal Orders:
       1                 ─────────────────
      / \                Preorder  (NLR): [1, 2, 4, 5, 3, 6]
     2   3               Inorder   (LNR): [4, 2, 5, 1, 3, 6]
    / \   \              Postorder (LRN): [4, 5, 2, 6, 3, 1]
   4   5   6             Level Order:     [[1], [2,3], [4,5,6]]

  RECURSIVE vs ITERATIVE (Stack)
  ───────────────────────────────

  RECURSIVE:                    ITERATIVE (Inorder):
  def inorder(node):            stack = []
      if not node: return       while root or stack:
      inorder(node.left)            while root:
      visit(node)                       stack.append(root)
      inorder(node.right)              root = root.left
                                    root = stack.pop()
                                    visit(root)
                                    root = root.right

  SUM ROOT-TO-LEAF NUMBERS           SAME TREE CHECK
  ─────────────────────────           ─────────────────
       1                              p:  1      q:  1
      / \                                / \        / \
     2   3                              2   3      2   3
                                        ↓          ↓
  Path 1→2 = 12                     val match? → recurse left & right
  Path 1→3 = 13
  Total = 25
```

| # | Problem | Difficulty | Technique | Key Code |
|---|---------|------------|-----------|----------|
| 94 | Binary Tree Inorder Traversal | 🟢 Easy | Recursive + Iterative | DFS `L→N→R` / Stack-based |
| 100 | Same Tree | 🟢 Easy | Recursive Comparison | `p.val == q.val` and recurse both subtrees |
| 102 | Binary Tree Level Order Traversal | 🟡 Medium | BFS (Deque) | `deque` → process level-by-level |
| 129 | Sum Root to Leaf Numbers | 🟡 Medium | DFS + Accumulator | `curSum = curSum*10 + node.val` |
| 144 | Binary Tree Preorder Traversal | 🟢 Easy | Recursive + Iterative | DFS `N→L→R` / Stack (push R then L) |
| 145 | Binary Tree Postorder Traversal | 🟢 Easy | Recursive + Iterative | DFS `L→R→N` / Stack + reverse |

---

### 🔢 Math & Number Theory (7 Problems)

```
MATH TECHNIQUES WIREFRAME
═══════════════════════════════════════════════════════════

  GAUSS SUM (Missing Number)          DIGIT MANIPULATION
  ──────────────────────────          ──────────────────────
  nums = [3, 0, 1]                   n = 38
  n = 3                              3 + 8 = 11
  expected = 3×4/2 = 6               1 + 1 = 2  ← single digit
  actual   = 3+0+1 = 4               return 2
  missing  = 6 - 4 = 2 ✓

  ROMAN NUMERAL PARSING              TOURNAMENT MATCHES
  ─────────────────────              ──────────────────────
  "MCMXCIV"                          n=7 teams
  M=1000, C=100, M=1000              Round 1: 7→3 matches, 4 advance
  → C < M → subtract                 Round 2: 4→2 matches, 2 advance
  1000-100+1000-10+100-1+5           Round 3: 2→1 match, 1 winner
  = 1994                             Total = 3+2+1 = 6 = n-1
```

| # | Problem | Difficulty | Technique | Key Code |
|---|---------|------------|-----------|----------|
| 258 | Add Digits | 🟢 Easy | Digit Loop | `sum += n%10; n //= 10` repeat until single digit |
| 268 | Missing Number | 🟢 Easy | Gauss Sum | `n*(n+1)//2 - sum(nums)` |
| 412 | Fizz Buzz | 🟢 Easy | Modulo | `% 3`, `% 5`, `% 15` checks |
| 1281 | Subtract Product and Sum of Digits | 🟢 Easy | Digit Extraction | `product *= digit; sum += digit` |
| 1688 | Count of Matches in Tournament | 🟢 Easy | Simulation | Even: `n/2` matches, Odd: `(n-1)/2 + 1` |
| 2413 | Smallest Even Multiple | 🟢 Easy | Math | `n * (n%2 + 1)` |
| 2427 | Number of Common Factors | 🟢 Easy | Brute Force | Iterate `1..min(a,b)`, check `a%i==0 and b%i==0` |

---

### 🔲 Matrix (3 Problems)

```
MATRIX TECHNIQUES WIREFRAME
═══════════════════════════════════════════════════════════

  ROTATE IMAGE (90° clockwise)           SET MATRIX ZEROES
  ─────────────────────────────           ──────────────────
  Step 1: Transpose                       [1, 1, 1]    [1, 0, 1]
  ┌─────────┐     ┌─────────┐            [1, 0, 1] →  [0, 0, 0]
  │ 1  2  3 │     │ 1  4  7 │            [1, 1, 1]    [1, 0, 1]
  │ 4  5  6 │  →  │ 2  5  8 │
  │ 7  8  9 │     │ 3  6  9 │            Use first row/col as markers
  └─────────┘     └─────────┘            to avoid O(mn) extra space

  Step 2: Reverse each row
  ┌─────────┐
  │ 7  4  1 │
  │ 8  5  2 │  ← Final result
  │ 9  6  3 │
  └─────────┘
```

| # | Problem | Difficulty | Technique | Key Code |
|---|---------|------------|-----------|----------|
| 48 | Rotate Image | 🟡 Medium | Transpose + Reverse | Swap `[i][j]↔[j][i]` then reverse rows |
| 54 | Spiral Matrix | 🟡 Medium | Boundary Traversal | *(stub — in progress)* |
| 73 | Set Matrix Zeroes | 🟡 Medium | First Row/Col Markers | Use matrix edges as zero-flags |

---

### 🧩 Other / Miscellaneous

| # | Problem | Difficulty | Technique | Key Code |
|---|---------|------------|-----------|----------|
| 383 | Ransom Note | 🟢 Easy | Counter Comparison | `Counter(ransomNote)` vs `Counter(magazine)` |
| 771 | Jewels and Stones | 🟢 Easy | Counter Lookup | `Counter(stones)` → sum matches |
| 1812 | Determine Color of Chessboard Square | 🟢 Easy | Parity Check | Column set + digit parity |
| 2469 | Convert the Temperature | 🟢 Easy | Formula | `[celsius+273.15, celsius*1.80+32]` |

---

## 🧩 Techniques & Patterns Used

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                      TECHNIQUE FREQUENCY MAP                                │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Two Pointers       ████████████████  #26 #27 #80 #141 #160 #206            │
│  Hash Map/Counter   ██████████████    #13 #383 #387 #771                    │
│  XOR Bit Tricks     ████████          #136 #1486                            │
│  DFS / Recursion    ████████████████  #94 #100 #129 #144 #145               │
│  BFS (Queue)        ████              #102                                  │
│  Stack (Iterative)  ██████████        #94 #144 #145                         │
│  String Slicing     ████████████████  #125 #151 #344 #459 #2108             │
│  Math Formulae      ████████████      #258 #268 #1281 #2413                 │
│  Prefix/Suffix      ██████            #238 #1480                            │
│  In-place Modify    ████████████      #27 #48 #73 #442                      │
│  Set Operations     ██████            #448 #2062                            │
│  Simulation         ████████          #412 #1688 #2011                      │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Pattern Quick Reference

```
╔══════════════════════╦═══════════════════════════════════════════════════════╗
║ Pattern              ║ When to Use                                          ║
╠══════════════════════╬═══════════════════════════════════════════════════════╣
║ Two Pointers         ║ Sorted arrays, in-place removal, linked list cycles  ║
║ Hash Map / Counter   ║ Frequency counting, anagram checks, lookups         ║
║ XOR                  ║ Finding single/missing elements (pairs cancel)       ║
║ DFS (Recursive)      ║ Tree traversals, path sums, tree comparison         ║
║ BFS (Queue)          ║ Level-order traversal, shortest path                ║
║ Stack (Iterative)    ║ Converting recursive tree traversal to iterative     ║
║ Sliding Window       ║ Substring problems, contiguous subarrays            ║
║ Prefix/Suffix Array  ║ Range product/sum without division                   ║
║ Index Negation       ║ Find duplicates/missing in [1,n] range, O(1) space  ║
║ Math (Gauss, Mod)    ║ Missing number, digit problems, divisibility        ║
╚══════════════════════╩═══════════════════════════════════════════════════════╝
```

---

## 💡 Solution Highlights

### #238 — Product of Array Except Self (O(n), No Division)

```python
# Elegant prefix/suffix product approach
def productExceptSelf(self, nums):
    answer = [1] * len(nums)

    left_product = 1                          # ──── Left pass ────
    for i in range(len(nums)):                #  [1, 1, 2, 6]
        answer[i] *= left_product             #  accumulate product
        left_product *= nums[i]               #  of everything LEFT

    right_product = 1                         # ──── Right pass ────
    for i in reversed(range(len(nums))):      #  [24, 12, 4, 1]
        answer[i] *= right_product            #  multiply by product
        right_product *= nums[i]              #  of everything RIGHT

    return answer  # [24, 12, 8, 6]
```

### #442 — Find All Duplicates (O(n) Time, O(1) Space)

```python
# Clever index-negation trick for [1, n] range arrays
def findDuplicates(self, nums):
    result = []
    for i in nums:
        idx = abs(i) - 1          # Map value → index
        if nums[idx] < 0:         # Already visited?
            result.append(abs(i)) #   → It's a duplicate!
        else:
            nums[idx] = -nums[idx] # Mark as visited by negating
    return result
```

### #459 — Repeated Substring Pattern (One-liner Trick)

```python
# If s is built from repeating pattern, it appears in (s+s)[1:-1]
def repeatedSubstringPattern(self, s):
    return s in (s + s)[1:-1]
    # "abab" → "abababab" → "babababa" → contains "abab"? YES ✓
    # "abc"  → "abcabc"   → "bcabc"    → contains "abc"? NO  ✗
```

### #189 — Rotate Array (Evolution of Attempts)

```python
# Attempt 1: Slicing (28/39 passed — edge case with k > len)
# Attempt 2: Pop & prepend loop (35/39 — TLE on large arrays)
# Attempt 3: Modulo + loop (35/39 — still TLE)
# ✅ Final: Modulo + single slice operation — O(n)
def rotate(self, nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
```

---

## 🚀 How to Run

```bash
# Clone the repository
git clone <repo-url>
cd LeetcodeProblemSolving

# Run any solution directly
python "13. Roman to Integer.py"
python "238. Product of Array Except Self.py"

# Most files include test cases at the bottom
```

### Requirements

- **Python 3.x** (no external dependencies)
- Standard library only: `collections.Counter`, `collections.deque`

---

## 📁 Complete Problem Index

| # | Problem Name | File | Difficulty | Category |
|---|-------------|------|------------|----------|
| 13 | Roman to Integer | `13. Roman to Integer.py` | 🟢 Easy | String |
| 14 | Longest Common Prefix | `14. Longest Common Prefix.py` | 🟢 Easy | String |
| 26 | Remove Duplicates from Sorted Array | `26. Remove Duplicates from Sorted Array.py` | 🟢 Easy | Array |
| 27 | Remove Element | `27. Remove Element.py` | 🟢 Easy | Array |
| 28 | Find the Index of the First Occurrence | `28. Find the Index of the First Occurrence in a String.py` | 🟢 Easy | String |
| 48 | Rotate Image | `48. Rotate Image.py` | 🟡 Medium | Matrix |
| 54 | Spiral Matrix | `54. Spiral Matrix.py` | 🟡 Medium | Matrix |
| 58 | Length of Last Word | `58. Length of Last Word.py` | 🟢 Easy | String |
| 73 | Set Matrix Zeroes | `73. Set Matrix Zeroes.py` | 🟡 Medium | Matrix |
| 80 | Remove Duplicates from Sorted Array II | `80. Remove Duplicates from Sorted Array II.py` | 🟡 Medium | Array |
| 94 | Binary Tree Inorder Traversal | `94. Binary Tree Inorder Traversal.py` | 🟢 Easy | Tree |
| 100 | Same Tree | `100. Same Tree.py` | 🟢 Easy | Tree |
| 102 | Binary Tree Level Order Traversal | `102. Binary Tree Level Order Traversal.py` | 🟡 Medium | Tree |
| 125 | Valid Palindrome | `125. Valid Palindrome.py` | 🟢 Easy | String |
| 129 | Sum Root to Leaf Numbers | `129. Sum Root to Leaf Numbers.py` | 🟡 Medium | Tree |
| 136 | Single Number | `136. Single Number.py` | 🟢 Easy | Array |
| 141 | Linked List Cycle | `141. Linked List Cycle.py` | 🟢 Easy | Linked List |
| 144 | Binary Tree Preorder Traversal | `144. Binary Tree Preorder Traversal.py` | 🟢 Easy | Tree |
| 145 | Binary Tree Postorder Traversal | `145. Binary Tree Postorder Traversal.py` | 🟢 Easy | Tree |
| 151 | Reverse Words in a String | `151. Reverse Words in a String.py` | 🟡 Medium | String |
| 160 | Intersection of Two Linked Lists | `160. Intersection of Two Linked Lists.py` | 🟢 Easy | Linked List |
| 189 | Rotate Array | `189. Rotate Array.py` | 🟡 Medium | Array |
| 206 | Reverse Linked List | `206. Reverse Linked List.py` | 🟢 Easy | Linked List |
| 238 | Product of Array Except Self | `238. Product of Array Except Self.py` | 🟡 Medium | Array |
| 258 | Add Digits | `258. Add Digits.py` | 🟢 Easy | Math |
| 268 | Missing Number | `268. Missing Number.py` | 🟢 Easy | Math |
| 344 | Reverse String | `344. Reverse String.py` | 🟢 Easy | String |
| 383 | Ransom Note | `383. Ransom Note.py` | 🟢 Easy | String |
| 387 | First Unique Character in a String | `387. First Unique Character in a String.py` | 🟢 Easy | String |
| 412 | Fizz Buzz | `412. Fizz Buzz.py` | 🟢 Easy | Math |
| 442 | Find All Duplicates in an Array | `442. Find All Duplicates in an Array.py` | 🟡 Medium | Array |
| 448 | Find All Numbers Disappeared | `448. Find All Numbers Disappeared in an Array.py` | 🟢 Easy | Array |
| 459 | Repeated Substring Pattern | `459. Repeated Substring Pattern.py` | 🟢 Easy | String |
| 771 | Jewels and Stones | `771. Jewels and Stones.py` | 🟢 Easy | Hash Map |
| 1108 | Defanging an IP Address | `1108. Defanging an IP Address.py` | 🟢 Easy | String |
| 1281 | Subtract Product and Sum of Digits | `1281. Subtract the Product and Sum of Digits of an Integer.py` | 🟢 Easy | Math |
| 1455 | Check If Word Occurs As Prefix | `1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence.py` | 🟢 Easy | String |
| 1480 | Running Sum of 1d Array | `1480. Running Sum of 1d Array.py` | 🟢 Easy | Array |
| 1486 | XOR Operation in an Array | `1486. XOR Operation in an Array.py` | 🟢 Easy | Array |
| 1688 | Count of Matches in Tournament | `1688. Count of Matches in Tournament.py` | 🟢 Easy | Math |
| 1752 | Check if Array Is Sorted and Rotated | `1752. Check if Array Is Sorted and Rotated.py` | 🟢 Easy | Array |
| 1812 | Determine Color of Chessboard Square | `1812. Determine Color of a Chessboard Square.py` | 🟢 Easy | Math |
| 2011 | Final Value After Operations | `2011. Final Value of Variable After Performing Operations.py` | 🟢 Easy | Array |
| 2062 | Count Vowel Substrings | `2062. Count Vowel Substrings of a String.py` | 🟢 Easy | String |
| 2108 | First Palindromic String | `2108. Find First Palindromic String in the Array.py` | 🟢 Easy | String |
| 2413 | Smallest Even Multiple | `2413. Smallest Even Multiple.py` | 🟢 Easy | Math |
| 2427 | Number of Common Factors | `2427. Number of Common Factors.py` | 🟢 Easy | Math |
| 2469 | Convert the Temperature | `2469. Convert the Temperature.py` | 🟢 Easy | Math |

---

> **Language:** Python 3 · **Platform:** [LeetCode](https://leetcode.com/) · **Status:** Actively solving
