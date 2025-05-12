# LRU Cache

## Problem Statement

Design a data structure that follows the constraints of a **Least Recently Used (LRU)** cache.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` initializes the cache capacity.
- `int get(int key)` returns the value of the key if the key exists, otherwise -1.
- `void put(int key, int value)` updates or inserts the value.

---

## Example

**Input:**  
`LRUCache cache = new LRUCache(2)`  
`cache.put(1,1)`  
`cache.put(2,2)`  
`cache.get(1) // returns 1`  
`cache.put(3,3)`  
`cache.get(2) // returns -1`

---

## Constraints

- `0 <= key <= 10^4`
- `0 <= value <= 10^5`
- `1 <= capacity <= 3000`
- At most `2 * 10^5` calls will be made

---

## Approach

- Use a doubly linked list and a hashmap for O(1) operations.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(1) for get and put
- **Space Complexity:** O(capacity)
