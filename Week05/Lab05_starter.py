# Week 05 Lab: Recursion & Functions - Starter Code
# COMP2152 - Python Programming

print("=" * 60)
print("WEEK 05 LAB: RECURSION & FUNCTIONS")
print("=" * 60)

# ============================================================
# Question 1: Fibonacci Number (LeetCode #509)
# Concepts: Recursion, base case, recursive case
# ============================================================
print("\n" + "=" * 50)
print("Question 1: Fibonacci Number (#509)")
print("=" * 50)


def fib(n):
    """
    Calculate the nth Fibonacci number using recursion.

    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1

    Parameters:
        n (int): The position in the Fibonacci sequence

    Returns:
        int: The nth Fibonacci number
    """
    # TODO: Base case 1 - If n equals 0, return 0

    # TODO: Base case 2 - If n equals 1, return 1

    # TODO: Recursive case - Return fib(n-1) + fib(n-2)
    pass  # Remove this line when you add your code


# Test cases for Fibonacci
print("Fibonacci Sequence (F(0) to F(10)):")
print("-" * 30)
for i in range(11):
    result = fib(i)
    print("F(" + str(i) + ") = " + str(result))

print("\nAdditional test cases:")
print("F(15) = " + str(fib(15)))
print("F(20) = " + str(fib(20)))


# ============================================================
# Question 2: FizzBuzz (LeetCode #412)
# Concepts: Functions, conditionals, list building
# ============================================================
print("\n" + "=" * 50)
print("Question 2: FizzBuzz (#412)")
print("=" * 50)


def fizz_buzz(n):
    """
    Generate FizzBuzz sequence from 1 to n.

    Rules:
    - Divisible by 3 AND 5: "FizzBuzz"
    - Divisible by 3 only: "Fizz"
    - Divisible by 5 only: "Buzz"
    - Otherwise: the number as a string

    Parameters:
        n (int): The upper limit (inclusive)

    Returns:
        list: List of strings following FizzBuzz rules
    """
    result = []

    # TODO: Loop from 1 to n (inclusive)
    # Hint: Use range(1, n + 1)

        # TODO: Check if divisible by BOTH 3 and 5 FIRST
        # Hint: if i % 3 == 0 and i % 5 == 0

        # TODO: Then check if divisible by 3 only

        # TODO: Then check if divisible by 5 only

        # TODO: Otherwise, append the number as a string
        # Hint: result.append(str(i))

    return result


# Test cases for FizzBuzz
print("\nTest Case 1: n = 3")
result = fizz_buzz(3)
print("Output: " + str(result))
print("Expected: ['1', '2', 'Fizz']")

print("\nTest Case 2: n = 5")
result = fizz_buzz(5)
print("Output: " + str(result))
print("Expected: ['1', '2', 'Fizz', '4', 'Buzz']")

print("\nTest Case 3: n = 15")
result = fizz_buzz(15)
print("Output: " + str(result))
print("Expected: ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']")

print("\nTest Case 4: n = 1")
result = fizz_buzz(1)
print("Output: " + str(result))
print("Expected: ['1']")


# ============================================================
# Question 3: Binary Search (LeetCode #704)
# Concepts: Divide & Conquer, Iterative and Recursive
# ============================================================
print("\n" + "=" * 50)
print("Question 3: Binary Search (#704)")
print("=" * 50)


# Part A: Iterative Solution
def binary_search_iterative(nums, target):
    """
    Search for target in sorted array using iteration.

    Parameters:
        nums (list): Sorted list of integers
        target (int): Value to find

    Returns:
        int: Index of target, or -1 if not found
    """
    # TODO: Initialize left pointer to 0
    left = 0

    # TODO: Initialize right pointer to len(nums) - 1
    right = len(nums) - 1

    # TODO: While left <= right:
    #   - Calculate mid = (left + right) // 2
    #   - If nums[mid] == target, return mid
    #   - If target < nums[mid], search left half: right = mid - 1
    #   - If target > nums[mid], search right half: left = mid + 1

    # TODO: Return -1 if target not found
    return -1


# Part B: Recursive Solution
def binary_search_recursive(nums, target, left, right):
    """
    Search for target in sorted array using recursion.

    Parameters:
        nums (list): Sorted list of integers
        target (int): Value to find
        left (int): Left boundary index
        right (int): Right boundary index

    Returns:
        int: Index of target, or -1 if not found
    """
    # TODO: Base case - If left > right, return -1 (target not found)

    # TODO: Calculate mid = (left + right) // 2

    # TODO: If nums[mid] == target, return mid

    # TODO: If target < nums[mid], recurse on left half
    # Hint: return binary_search_recursive(nums, target, left, mid - 1)

    # TODO: If target > nums[mid], recurse on right half
    # Hint: return binary_search_recursive(nums, target, mid + 1, right)

    pass  # Remove this line when you add your code


# Wrapper function for recursive solution
def search_recursive(nums, target):
    """Wrapper function to call recursive binary search."""
    if len(nums) == 0:
        return -1
    return binary_search_recursive(nums, target, 0, len(nums) - 1)


# Test cases for Binary Search
print("\n--- Part A: Iterative Binary Search ---")
test_cases = [
    ([-1, 0, 3, 5, 9, 12], 9),
    ([-1, 0, 3, 5, 9, 12], 2),
    ([1], 1),
    ([1, 2, 3, 4, 5], 1),
    ([1, 2, 3, 4, 5], 5),
    ([1, 2, 3, 4, 5], 3),
    ([], 5),
]

for nums, target in test_cases:
    result = binary_search_iterative(nums, target)
    print("nums=" + str(nums) + ", target=" + str(target) + " -> index: " + str(result))

print("\n--- Part B: Recursive Binary Search ---")
for nums, target in test_cases:
    result = search_recursive(nums, target)
    print("nums=" + str(nums) + ", target=" + str(target) + " -> index: " + str(result))


# ============================================================
# Verification: Both methods should give same results
# ============================================================
print("\n" + "=" * 50)
print("Verification: Both Methods Should Match")
print("=" * 50)

nums = [-1, 0, 3, 5, 9, 12]
print("Array: " + str(nums))
print("-" * 40)

for target in [-1, 0, 3, 5, 9, 12, 2, 100]:
    iter_result = binary_search_iterative(nums, target)
    rec_result = search_recursive(nums, target)
    match = "PASS" if iter_result == rec_result else "FAIL"
    print("Target " + str(target).rjust(4) + ": Iterative=" + str(iter_result).rjust(2) + ", Recursive=" + str(rec_result).rjust(2) + " " + match)


# ============================================================
# Summary
# ============================================================
print("\n" + "=" * 60)
print("COMPLETE THE TODO SECTIONS ABOVE!")
print("=" * 60)
print("""
Key Concepts to Practice:

1. FIBONACCI (Recursion)
   - Two base cases: F(0)=0, F(1)=1
   - Recursive case: F(n) = F(n-1) + F(n-2)
   - Each call moves toward base case

2. FIZZBUZZ (Functions)
   - Function with parameter and return value
   - Conditional logic (if/elif/else)
   - Building and returning a list
   - Order of conditions matters!

3. BINARY SEARCH (Divide & Conquer)
   - Iterative: while loop with left/right pointers
   - Recursive: base case + recursive calls
   - O(log n) time complexity
   - Array MUST be sorted!

Connection to Grokking Algorithms:
- Binary Search: Chapter 1
- Recursion: Chapter 3
""")
