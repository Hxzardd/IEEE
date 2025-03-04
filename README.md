# Competitive Coding Data Structures Challenge

This repository contains implementations for a series of challenging data structure tasks designed to test and enhance algorithmic skills. The project is divided into three levels of increasing complexity:

- **Level 1:** Custom Data Structure (Stack) with constant-time operations.
- **Level 2:** Composite Data Structure (Interval Merger) for efficiently merging overlapping intervals.
- **Level 3:** Composite Data Structure (Time-Based Cache) that supports key-value storage with automatic expiry.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)

---

## Overview

This project is my attempt for the Technical Competitive-Coding round for IEEE-VIT club that focuses on implementing efficient data structures. Each level of the challenge demonstrates a specific technique:
- **Level 1** implements a custom stack that, in addition to standard operations, provides constant-time retrieval of the minimum and maximum elements.
- **Level 2** implements an interval merger that maintains a sorted list of non-overlapping intervals, merging overlapping intervals as they are added.
- **Level 3** sketches a design for a time-based cache that supports fast lookups and automatic removal of expired keys using a min-heap.

---

## Features implemented

- **Custom Stack:**
  - Supports `push(x)`, `pop()`, `top()`, `getMin()`, and `getMax()` in O(1) time.
  - Uses O(n) space with a tuple-based approach to store auxiliary data.

- **Interval Merger:**
  - Maintains a set of non-overlapping intervals.
  - Merges overlapping intervals upon insertion.
  - Provides retrieval of intervals in O(n) time.

- **Time-Based Cache:**
  - Stores key-value pairs along with an expiration timestamp.
  - Automatically cleans up expired entries.
  - Utilizes a min-heap to efficiently track the key with the nearest expiry.

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
   cd competitive-coding-data-structures
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
- Execute the individual Python files (e.g., python level1.py) to see sample usage and test cases after removing the comments from the end of each code.