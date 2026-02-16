# DSA Day 2/250: Two Sum II (LeetCode 167)

**Problem Number:** 167  
**Difficulty:** Medium  
**Topics:** Arrays, Two Pointers  

---

## 🧠 Problem Statement

Given a **1-indexed** array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target`.

Let the two numbers be:
numbers[index1] and numbers[index2]


Where:
1 <= index1 < index2 <= numbers.length


### Requirements

- Exactly one solution exists.
- You may not use the same element twice.
- Your solution must use **constant extra space**.
- Return the indices as a 1-based array:
[index1, index2]


---

## ✨ Examples

### Example 1
**Input**
numbers = [2,7,11,15]
target = 9


**Output**
[1,2]


---

### Example 2
**Input**
numbers = [2,3,4]
target = 6


**Output**
[1,3]


---

### Example 3
**Input**
numbers = [-1,0]
target = -1


**Output**
[1,2]


---

## 📌 Constraints

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order
- `-1000 <= target <= 1000`
- Exactly one solution exists

---

## 🚀 About This Challenge

This is **Day 2** of my **250 Days DSA Challenge**.

Goal:
- Build strong intuition
- Recognize common patterns
- Develop interview-ready thinking

All posts from this challenge are being documented and saved in a single Medium list for easy revision.

---

## 💡 Intuition

The key insight:

> The array is already sorted.

Because of that:

- If the sum is too large → we need a smaller number
- If the sum is too small → we need a larger number

This allows us to use the **Two Pointers** technique efficiently.

Instead of brute force, we:
- Start one pointer at the beginning
- Start one pointer at the end
- Move them intelligently

---

## 🛠️ Approach (Two Pointers)

### Initialization

- `fp` (first pointer) → start of array
- `sp` (second pointer) → end of array

### Rules

1. Compute:
sum = numbers[fp] + numbers[sp]


2. If `sum > target`
- Move `sp` left

3. If `sum < target`
- Move `fp` right

4. If `sum === target`
- Solution found

Because the array is sorted, each movement moves us closer to the correct answer.

---

## 🔄 Step-by-Step Execution

### Input
numbers = [2, 7, 11, 15]
target = 9


---

### Iteration 1

fp = 0 → 2
sp = 3 → 15
sum = 17


Since `17 > 9`, move `sp` left.

---

### Iteration 2

fp = 0 → 2
sp = 2 → 11
sum = 13


Since `13 > 9`, move `sp` left.

---

### Iteration 3

fp = 0 → 2
sp = 1 → 7
sum = 9


Target found.

Indices are 1-based:

[fp + 1, sp + 1] → [1, 2]


---

## ✅ Why This Works

- Sorted array enables directional decisions.
- Moving left decreases sum.
- Moving right increases sum.
- Exactly one solution guarantees termination.
- No extra space is used.

This is a classic **Two Pointers on Sorted Array** pattern.

---

## ⏱️ Complexity Analysis

**Time Complexity:** `O(n)`  
Each element is visited at most once.

**Space Complexity:** `O(1)`  
Only two pointers are used.

---

## 🧩 Code (JavaScript)

```js
var twoSum = function(numbers, target) {
    let fp = 0;
    let sp = numbers.length - 1;

    while (fp < sp) {
        let sum = numbers[fp] + numbers[sp];

        if (sum > target) sp--;
        else if (sum < target) fp++;
        else break;
    }

    return [fp + 1, sp + 1];
};
📚 Key Takeaways
Sorted arrays unlock powerful pointer-based solutions.

Two pointers allow linear time without extra space.

Pointer movement depends on constraints.

Always pay attention to keywords like:

“sorted”

“exactly one solution”

“constant space”

🎯 Pattern Identified
Two Pointers on Sorted Array

This pattern frequently appears in interviews.