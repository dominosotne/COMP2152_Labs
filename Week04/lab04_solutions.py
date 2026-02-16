# Lab 04: Loops and Functions Practice
# Complete Solutions
# COMP2152 - Python Programming

print("=" * 60)
print("LAB 04: LOOPS AND FUNCTIONS PRACTICE - SOLUTIONS")
print("=" * 60)

# ============================================================
# Question 1: Robot Return to Origin (LeetCode #657)
# Concepts: for loop, if/elif, state tracking, functions
# ============================================================
print("\n" + "=" * 50)
print("Question 1: Robot Return to Origin")
print("=" * 50)


def robot_returns_to_origin(moves):
    """
    Check if robot returns to origin (0,0) after all moves.

    Parameters:
        moves (str): String of moves (U, D, L, R)

    Returns:
        bool: True if robot returns to origin, False otherwise
    """
    # Initialize starting position
    x = 0
    y = 0

    # Loop through each move and update position
    for move in moves:
        if move == "U":
            y += 1
        elif move == "D":
            y -= 1
        elif move == "R":
            x += 1
        elif move == "L":
            x -= 1

    # Return True if back at origin (both x and y are 0)
    return x == 0 and y == 0


# Test cases
test_moves = ["UD", "LL", "UDLR", "LDRRLRUULR"]

for moves in test_moves:
    result = robot_returns_to_origin(moves)
    print("Moves '" + moves + "': Returns to origin? " + str(result))


# ============================================================
# Question 2: Two Sum (LeetCode #1)
# Concepts: Nested loops, dictionary lookup, functions
# ============================================================
print("\n" + "=" * 50)
print("Question 2: Two Sum")
print("=" * 50)


# Part A: Brute Force with Nested Loops
def two_sum_brute_force(numbers, target):
    """
    Find two numbers that add up to target using nested loops.

    Parameters:
        numbers (list): List of integers
        target (int): Target sum

    Returns:
        tuple: Indices of the two numbers, or None if not found
    """
    # Outer loop: go through each number
    for i in range(len(numbers)):
        # Inner loop: check every number after i
        for j in range(i + 1, len(numbers)):
            # Check if this pair adds up to target
            if numbers[i] + numbers[j] == target:
                return (i, j)

    # No pair found
    return None


# Part B: Optimized with Dictionary
def two_sum_optimized(numbers, target):
    """
    Find two numbers that add up to target using dictionary lookup.

    Parameters:
        numbers (list): List of integers
        target (int): Target sum

    Returns:
        tuple: Indices of the two numbers, or None if not found
    """
    seen = {}  # Dictionary to store {number: index}

    for i in range(len(numbers)):
        # Calculate what number we need to reach target
        needed = target - numbers[i]

        # Check if we've seen the needed number before
        if needed in seen:
            return (seen[needed], i)

        # Store current number and its index
        seen[numbers[i]] = i

    # No pair found
    return None


# Test cases
test_cases = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
    ([1, 5, 3, 8, 2], 10)
]

print("\n=== Part A: Brute Force (Nested Loops) ===")
for numbers, target in test_cases:
    result = two_sum_brute_force(numbers, target)
    print("Numbers: " + str(numbers) + ", Target: " + str(target))
    print("Result: " + str(result))
    if result is not None:
        print("  -> " + str(numbers[result[0]]) + " + " + str(numbers[result[1]]) + " = " + str(target))
    print()

print("=== Part B: Optimized (Dictionary) ===")
for numbers, target in test_cases:
    result = two_sum_optimized(numbers, target)
    print("Numbers: " + str(numbers) + ", Target: " + str(target))
    print("Result: " + str(result))
    if result is not None:
        print("  -> " + str(numbers[result[0]]) + " + " + str(numbers[result[1]]) + " = " + str(target))
    print()


# ============================================================
# Question 3: Shuffle the Array (LeetCode #1470)
# Concepts: List slicing, for loop, range(), append()
# ============================================================
print("\n" + "=" * 50)
print("Question 3: Shuffle the Array")
print("=" * 50)


def shuffle_array(nums, n):
    """
    Interleave first half and second half of array.

    Parameters:
        nums (list): List of 2n elements
        n (int): Half the length of the list

    Returns:
        list: Shuffled list [x1, y1, x2, y2, ...]
    """
    # Step 1: Split into two halves using slicing
    first_half = nums[:n]    # Elements from index 0 to n-1
    second_half = nums[n:]   # Elements from index n to end

    # Step 2: Create empty result list
    result = []

    # Step 3: Interleave using a for loop
    for i in range(n):
        result.append(first_half[i])   # Add from first half
        result.append(second_half[i])  # Add from second half

    return result


# Test cases
test_cases = [
    ([2, 5, 1, 3, 4, 7], 3),
    ([1, 2, 3, 4, 4, 3, 2, 1], 4),
    ([1, 1, 2, 2], 2)
]

for nums, n in test_cases:
    print("Original: " + str(nums))
    print("n = " + str(n))

    # Show the slices
    print("First half (nums[:" + str(n) + "]): " + str(nums[:n]))
    print("Second half (nums[" + str(n) + ":]): " + str(nums[n:]))

    # Get result
    result = shuffle_array(nums, n)
    print("Shuffled: " + str(result))
    print()


# ============================================================
# Question 4: First Unique Character (LeetCode #387)
# Concepts: Dictionary counting, helper functions, two-pass
# ============================================================
print("\n" + "=" * 50)
print("Question 4: First Unique Character")
print("=" * 50)


# Helper function: Count all characters in a string
def count_characters(s):
    """
    Count occurrences of each character in a string.

    Parameters:
        s (str): Input string

    Returns:
        dict: Dictionary with character counts
    """
    counts = {}

    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts


# Main function: Find first unique character
def first_unique_character(s):
    """
    Find the index of the first non-repeating character.

    Parameters:
        s (str): Input string

    Returns:
        int: Index of first unique character, or -1 if none
    """
    # Step 1: Get character counts using helper function
    char_counts = count_characters(s)

    # Step 2: Loop through string with index to find first unique
    for i in range(len(s)):
        if char_counts[s[i]] == 1:
            return i

    # Step 3: Return -1 if no unique character found
    return -1


# Test cases
test_strings = ["leetcode", "loveleetcode", "aabb", "python", "aabbcc"]

for s in test_strings:
    index = first_unique_character(s)

    if index != -1:
        print("First unique character in '" + s + "': index " + str(index) + " (character: '" + s[index] + "')")
    else:
        print("First unique character in '" + s + "': index -1 (no unique character)")

    # Show the character counts for understanding
    counts = count_characters(s)
    print("  Character counts: " + str(counts))
    print()


# ============================================================
# BONUS: Alternative Solutions
# ============================================================
print("\n" + "=" * 60)
print("BONUS: ALTERNATIVE SOLUTIONS")
print("=" * 60)

# Alternative Q1: Using count method
print("\n--- Q1 Alternative: Using count() ---")


def robot_returns_to_origin_v2(moves):
    """Alternative: Count U/D and L/R pairs."""
    # Robot returns if equal ups/downs AND equal lefts/rights
    return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")


print("Testing 'UDLR' with count method: " + str(robot_returns_to_origin_v2("UDLR")))
print("Testing 'LLRR' with count method: " + str(robot_returns_to_origin_v2("LLRR")))


# Alternative Q3: Using zip
print("\n--- Q3 Alternative: Using zip() ---")


def shuffle_array_v2(nums, n):
    """Alternative: Use zip to pair elements."""
    first_half = nums[:n]
    second_half = nums[n:]
    result = []

    # zip pairs up elements from both halves
    for x, y in zip(first_half, second_half):
        result.append(x)
        result.append(y)

    return result


print("Shuffle [2,5,1,3,4,7] with zip: " + str(shuffle_array_v2([2, 5, 1, 3, 4, 7], 3)))


# Alternative Q4: Using get() method
print("\n--- Q4 Alternative: Using dict.get() ---")


def count_characters_v2(s):
    """Alternative: Use get() to simplify counting."""
    counts = {}
    for char in s:
        # get() returns 0 if key doesn't exist, then we add 1
        counts[char] = counts.get(char, 0) + 1
    return counts


print("Count 'hello' with get(): " + str(count_characters_v2("hello")))


# ============================================================
# Summary
# ============================================================
print("\n" + "=" * 60)
print("ALL SOLUTIONS COMPLETE!")
print("=" * 60)
print("""
Concepts Practiced:
- Q1: for loops, if/elif conditionals, state tracking
- Q2: Nested loops (brute force) vs Dictionary (optimized)
- Q3: List slicing ([:n], [n:]), loop with range()
- Q4: Dictionary for counting, helper functions, two-pass algorithm

Key Takeaways:
1. Functions make code reusable and easier to test
2. Nested loops check all pairs but are slower (O(n^2))
3. Dictionaries enable fast lookups (O(1))
4. Slicing extracts portions of lists easily
5. Breaking problems into helper functions improves readability
""")
