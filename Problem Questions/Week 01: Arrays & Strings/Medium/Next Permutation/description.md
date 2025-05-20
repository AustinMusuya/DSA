# Next Permutation

**Difficulty:** Medium  
**Topics:** Arrays, Two Pointers  
**Companies:** Multiple

---

## 📝 Problem Description

A **permutation** of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for `arr = [1, 2, 3]`, the following are all the permutations of `arr`:

```text
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
```

The **next permutation** of an array of integers is the next lexicographically greater permutation of its integers.

More formally, if all the permutations of the array are sorted in a container according to their lexicographical order, then the next permutation is the one that follows it in the sorted order.

If such arrangement is **not possible**, the array must be rearranged as the **lowest possible order** (i.e., sorted in ascending order).

You must do this **in-place** and use **only constant extra memory**.

---

## 🔁 Examples

### Example 1

**Input:**

```text
nums = [1, 2, 3]
```

**Output:**

```text
nums = [1, 3, 2]
```

### Example 2

**Input:**

```text
nums = [3, 2, 1]
```

**Output:**

```text
nums = [1, 2, 3]
```

### Example 3

**Input:**

```text
nums = [1, 1, 5]
```

**Output:**

```text
[1, 5, 1]
```
