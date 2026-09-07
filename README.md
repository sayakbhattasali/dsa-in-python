# Data Structures & Algorithms in Python 🐍

A structured repository containing solutions to fundamental Data Structures and Algorithms (DSA) problems, common coding interview questions, and algorithmic patterns implemented in Python.

---

## 📁 Repository Architecture

```text
DSA in Py/
│
├── Lists-Tuples-Strings/            # Array & string manipulation, two pointers, prefix sums
│   ├── max-profit.py                # Best Time to Buy & Sell Stock (Greedy / Min-Tracking)
│   ├── maximum-subarray.py          # Kadane's Algorithm (Max Subarray Sum)
│   ├── remove-duplicates-SA.py      # In-place duplicate removal (Two Pointers)
│   ├── remove-duplicates-SA(II).py  # Allow duplicates at most twice (Two Pointers)
│   ├── Running-Sum.py               # Prefix Sum calculation
│   └── sort-array-parity.py         # Even-odd array partitioning (Two Pointers)
│
├── Recursion/                       # Core recursive techniques and divide-and-conquer
│   ├── GCD-of-2nos.py               # Recursive Euclidean Algorithm
│   └── Power-of-2.py                # Recursive Power of Two check
│
└── frequently-reported-problems/    # Frequently asked screening & interview problems
    ├── 1st-non-repeating-char.py    # First unique character (Frequency Hash Map)
    ├── 2nd-largest-array-element.py # Second distinct largest value in an array
    ├── armstrong-number.py          # Armstrong / Narcissistic number check
    ├── divisible-sum-difference.py  # Absolute difference of divisible vs non-divisible sums
    ├── fibonacci-series.py          # Iterative O(N) Fibonacci sequence generation
    ├── GCD-euclidean.py             # Iterative Euclidean Algorithm for GCD
    ├── happy-number.py              # Cycle detection via Hash Set
    ├── max-temperature-decrement.py # Max decrease between consecutive readings
    ├── palindrome.py                # Two-pointer palindrome validation
    ├── rebound-height.py            # Geometric decay calculation after N bounces
    └── team-games.py                # Frequency counting & winner determination
```

---

## 📊 DSA Progress Tracker & Topic Tally

> **Current Progress:** 5 Core Topics Mastered · 1 Topic In Progress · 7 Topics in Roadmap · **19 Problems Solved**

- [x] **1. Arrays & Lists** *(In-place operations, two-pointers, parity partition, subarray manipulation)*
- [x] **2. Strings** *(Palindromes, character frequencies, order-preserving traversals)*
- [x] **3. Prefix Sum & Dynamic Range Tracking** *(Running sum, cumulative differences)*
- [x] **4. Greedy & 1D Dynamic Programming** *(Kadane's algorithm, max profit single transaction)*
- [x] **5. Math & Number Theory** *(Euclidean GCD, Fibonacci series, Armstrong numbers, rebound geometry)*
- [x] **6. Hash Maps & Sets** *(Frequency tracking, non-repeating character, cycle detection in numbers)*
- [ ] **7. Recursion & Backtracking** 🔄 *(Basic recursion completed; Backtracking & N-Queens pending)*
- [ ] **8. Searching & Sorting** *(Binary Search, Two-pointer search, Quick Sort, Merge Sort)*
- [ ] **9. Linked Lists** *(Singly/Doubly linked lists, cycle detection, list reversal)*
- [ ] **10. Stacks & Queues** *(Monotonic stack, valid parentheses, deque sliding window)*
- [ ] **11. Trees & Binary Search Trees (BST)** *(Tree traversals, tree depth, validation)*
- [ ] **12. Heaps & Priority Queues** *(Kth largest element, median finding)*
- [ ] **13. Graphs** *(BFS, DFS, cycle detection in graphs, Dijkstra's algorithm)*
- [ ] **14. Advanced Dynamic Programming** *(2D DP, 0/1 Knapsack, Longest Common Subsequence)*
- [ ] **15. Bit Manipulation** *(Bitwise operations, single number, counting bits)*

---

## 📚 Topics & Problems Covered

### 1. Lists, Tuples & Strings (`/Lists-Tuples-Strings`)
Focuses on sequence manipulation, pointer techniques, and dynamic range tracking.

| Problem File | Concept / Technique | Time Complexity | Space Complexity |
| :--- | :--- | :---: | :---: |
| [`maximum-subarray.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/Lists-Tuples-Strings/maximum-subarray.py) | Kadane's Algorithm (Dynamic Programming / Greedy) | $O(N)$ | $O(1)$ |
| [`max-profit.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/Lists-Tuples-Strings/max-profit.py) | One-pass Min Price Tracking | $O(N)$ | $O(1)$ |
| [`Running-Sum.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/Lists-Tuples-Strings/Running-Sum.py) | Prefix Sum Array | $O(N)$ | $O(N)$ |
| [`remove-duplicates-SA.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/Lists-Tuples-Strings/remove-duplicates-SA.py) | Two Pointers (In-place Array Modification) | $O(N)$ | $O(1)$ |
| [`remove-duplicates-SA(II).py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/Lists-Tuples-Strings/remove-duplicates-SA(II).py) | Two Pointers with Count Limit | $O(N)$ | $O(1)$ |
| [`sort-array-parity.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/Lists-Tuples-Strings/sort-array-parity.py) | In-place Partitioning (Two Pointers) | $O(N)$ | $O(1)$ |

---

### 2. Recursion (`/Recursion`)
Fundamental mathematical and divide-and-conquer recursions.

| Problem File | Description | Time Complexity | Space Complexity |
| :--- | :--- | :---: | :---: |
| [`GCD-of-2nos.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/Recursion/GCD-of-2nos.py) | Recursive Euclidean GCD calculation | $O(\log(\min(A, B)))$ | $O(\log(\min(A, B)))$ |
| [`Power-of-2.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/Recursion/Power-of-2.py) | Recursive power-of-two validation | $O(\log N)$ | $O(\log N)$ |

---

### 3. Frequently Reported Problems (`/frequently-reported-problems`)
Real-world problems frequently encountered in technical interviews and assessment tests.

| # | Problem File | Key Concept | Time Complexity | Space Complexity |
| :-: | :--- | :--- | :---: | :---: |
| 1 | [`2nd-largest-array-element.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/frequently-reported-problems/2nd-largest-array-element.py) | Set Deduplication & Sorting | $O(N \log N)$ | $O(N)$ |
| 2 | [`divisible-sum-difference.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/frequently-reported-problems/divisible-sum-difference.py) | Loop & Modulo Arithmetic | $O(N)$ | $O(1)$ |
| 3 | [`armstrong-number.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/frequently-reported-problems/armstrong-number.py) | Digit Extraction & Power Sum | $O(D)$ | $O(1)$ |
| 4 | [`happy-number.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/frequently-reported-problems/happy-number.py) | Cycle Detection with Hash Set | $O(K)$ | $O(K)$ |
| 5 | [`GCD-euclidean.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/frequently-reported-problems/GCD-euclidean.py) | Iterative Euclidean Algorithm | $O(\log(\min(A, B)))$ | $O(1)$ |
| 6 | [`fibonacci-series.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/frequently-reported-problems/fibonacci-series.py) | Iterative Sequence Generation | $O(N)$ | $O(N)$ |
| 7 | [`palindrome.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/frequently-reported-problems/palindrome.py) | Two Pointers (Left & Right) | $O(N)$ | $O(1)$ |
| 8 | [`1st-non-repeating-char.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/frequently-reported-problems/1st-non-repeating-char.py) | Hash Map Frequency Count (Two-pass) | $O(N)$ | $O(U)$ |
| 9 | [`team-games.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/frequently-reported-problems/team-games.py) | Frequency Counter & Conditional Logic | $O(N)$ | $O(1)$ |
| 10 | [`rebound-height.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/frequently-reported-problems/rebound-height.py) | Geometric Formula Calculation | $O(1)$ | $O(1)$ |
| 11 | [`max-temperature-decrement.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/frequently-reported-problems/max-temperature-decrement.py) | Consecutive Difference Traversal | $O(N)$ | $O(1)$ |

---

## 🛠️ Algorithmic Patterns Used

- **Two Pointers:** In-place modifications and symmetric comparisons ([`palindrome.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/frequently-reported-problems/palindrome.py), [`remove-duplicates-SA.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/Lists-Tuples-Strings/remove-duplicates-SA.py), [`sort-array-parity.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/Lists-Tuples-Strings/sort-array-parity.py)).
- **Kadane's Algorithm:** Optimal $O(N)$ continuous subarray maximum sum ([`maximum-subarray.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/Lists-Tuples-Strings/maximum-subarray.py)).
- **Hash Maps / Dictionaries:** Fast frequency lookups in $O(1)$ time ([`1st-non-repeating-char.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/frequently-reported-problems/1st-non-repeating-char.py)).
- **Cycle Detection:** Infinite loop and state tracking via sets ([`happy-number.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/frequently-reported-problems/happy-number.py)).
- **Euclidean Algorithm:** Logarithmic greatest common divisor computation ([`GCD-euclidean.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/frequently-reported-problems/GCD-euclidean.py)).
- **Prefix Sums:** Running cumulative computations ([`Running-Sum.py`](file:///c:/Users/KIIT0001/Desktop/DSA%20in%20Py/Lists-Tuples-Strings/Running-Sum.py)).

---

## 🚀 Running the Solutions

All solutions are standalone Python 3 scripts with interactive inputs.

```bash
# Example: Run Euclidean GCD
python "frequently-reported-problems/GCD-euclidean.py"

# Example: Run Maximum Subarray
python "Lists-Tuples-Strings/maximum-subarray.py"
```
