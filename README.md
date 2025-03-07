# IEEE Technical CC Tasks

This repository contains implementations for a series of challenging data structure tasks designed to test and enhance algorithmic skills. The project is divided into four levels of increasing complexity:

- **Level 0:** Basic Data Structure (Doubly Linked List) with basic operations.
- **Level 1:** Custom Data Structure (Stack) with constant-time operations.
- **Level 2:** Composite Data Structure (Interval Merger) for efficiently merging overlapping intervals.
- **Level 3:** Composite Data Structure (Time-Based Cache) that supports key-value storage with automatic expiry.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [References](#references)

---

## Overview

This project is my attempt for the Technical Competitive-Coding round for IEEE-VIT club that focuses on implementing efficient data structures. Each level of the challenge demonstrates a specific technique:
- **Level 0** implements a doubly lnked list that comes with basic operations like insertion of head and tail, traversing through the list (backwards and forwards).
- **Level 1** implements a custom stack that, in addition to standard operations, provides constant-time retrieval of the minimum and maximum elements.
- **Level 2** implements an interval merger that maintains a sorted list of non-overlapping intervals, merging overlapping intervals as they are added.
- **Level 3** sketches a design for a time-based cache that supports fast lookups and automatic removal of expired keys using a min-heap.

---

## Features

- **Double Linked List:** *(Completed)*
  - Supports `insert_head()`, `insert_tail()` in O(1) time and `traverse_forward()`, `traverse_backward()`, `length()` in O(n) time. ✅

- **Custom Stack:** *(Completed)*
  - Supports `push(x)`, `pop()`, `top()`, `getMin()`, and `getMax()` in O(1) time. ✅
  - Uses O(n) space with a tuple-based approach to store data. ✅

- **Interval Merger:** *(Completed)*
  - Maintains a set of non-overlapping intervals. ✅
  - Inserts intervals in O(log n) time. ✅
  - Merges overlapping intervals upon insertion. ✅
  - Provides retrieval of intervals in O(n) time. ✅

- **Time-Based Cache:** *(Partially Complete - A version of test case is not passing which should theoretically pass I guess)*
  - Stores key-value pairs along with an expiration timestamp. ✅
  - Automatically cleans up expired entries. ✅
  - Utilizes a min-heap to efficiently track the key with the nearest expiry. ✅

---

## Technologies Used

- **Python 3** – Primary programming language.
- **SortedContainers** – For efficiently maintaining and sorting intervals in Level 2.
- **Heapq** – Python’s built-in module used for heap operations in Level 3.

---

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Hxzardd/IEEE.git
   cd your-directory-name
   ```

2. **Create and Activate a Virtual Environment (optional but recommended):**
 - Linux/Max:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

 - Windows:
    ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Tests:**
- Execute the individual Python files (e.g., `python level1.py`) to see sample usage and test cases after removing the comments from the end of each code.

---

## References

1. **For DDL** - [Click here](https://www.geeksforgeeks.org/doubly-linked-list/)
2. **For Stack** - [Click here](https://www.geeksforgeeks.org/stack-in-python/)
3. **For O(log n) Sorted Lists** - [Click here](https://www.geeksforgeeks.org/python-sorted-containers-an-introduction/)
4. **For Heaps** - [Click here](https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/)