# DSA Day 1/250: Move Zeroes (LeetCode 283)

**Problem Number:** 283  
**Difficulty:** Easy  
**Topics:** Arrays, Two Pointers  

---

## 🧠 Problem Statement

Given an integer array `nums`, move all `0`s to the end of it while maintaining the relative order of the non-zero elements.

**Important Constraints**
- The operation must be **in-place**
- Do **not** make a copy of the array

---

## ✨ Examples

### Example 1
**Input**
nums = [0, 1, 0, 3, 12]


**Output**
[1, 3, 12, 0, 0]


### Example 2
**Input**
nums = [0]


**Output**
[0]


---

## 📌 Constraints

- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

---

## 🚀 About This Challenge

I’m starting a **250 Days DSA Challenge**, where I solve one problem every day with a focus on:

- Intuition
- Common patterns
- Interview-ready thinking

This problem is a great starting point because it tests:
- Array traversal
- In-place updates
- Pointer coordination

All of these appear frequently in coding interviews.

---

## 💡 Intuition

Key observations:

- **Non-zero elements must keep their relative order**
- **Zeroes don’t need special handling**
- Instead of pushing zeroes to the end, we **pull non-zero elements forward**

This naturally leads to the **Two Pointers (Fast–Slow)** pattern.

---

## 🛠️ Approach

We use two pointers:

- `i` → Fast pointer that scans the array
- `start` → Slow pointer that tracks where the next non-zero should go

### Rules

- If `nums[i] !== 0`
  - Swap `nums[i]` with `nums[start]`
  - Increment `start`
- If `nums[i] === 0`
  - Do nothing
  - Just move forward

### Why this works

- Non-zero elements are placed in correct order
- Zeroes naturally drift to the end
- Everything happens **in-place**

---

## 🔄 Step-by-Step Walkthrough

### Input
nums = [0, 1, 0, 3, 12]
start = 0


### Iteration 1
- `i = 0`, `nums[i] = 0`
- No swap
- `start = 0`

### Iteration 2
- `i = 1`, `nums[i] = 1`
- Swap with `nums[start]`
[1, 0, 0, 3, 12]

- `start = 1`

### Iteration 3
- `i = 2`, `nums[i] = 0`
- No swap
- `start = 1`

### Iteration 4
- `i = 3`, `nums[i] = 3`
- Swap with `nums[start]`
[1, 3, 0, 0, 12]

- `start = 2`

### Iteration 5
- `i = 4`, `nums[i] = 12`
- Swap with `nums[start]`
[1, 3, 12, 0, 0]


---

## ✅ Final Output
[1, 3, 12, 0, 0]


---

## 🧪 Complexity Analysis

- **Time Complexity:** `O(n)`
  - Single pass through the array
- **Space Complexity:** `O(1)`
  - In-place modification

---

## 🧩 Code Implementation (JavaScript)

```js
var moveZeroes = function(nums) {
    let start = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            let temp = nums[i];
            nums[i] = nums[start];
            nums[start] = temp;
            start++;
        }
    }
};
📚 Key Takeaways
Two pointers don’t always mean opposite ends

Fast–Slow pointer pattern is extremely common

Focus on where elements should go, not on removing others

Simple problems often test clarity more than complexity