# ==============================================================================
# PYTHON SLICING: SEQUENCES, STRINGS & ARRAYS
# ==============================================================================
# Slicing in Python allows extracting a portion (sub-sequence) of an ordered
# sequence (such as strings, lists, or tuples) without modifying the original.
#
# GENERAL SYNTAX:
#   sequence[start : stop : step]
#
# PARAMETERS:
#   - start : Starting index (inclusive). Defaults to 0 (or end if step < 0).
#   - stop  : Stopping index (exclusive). Defaults to len(sequence).
#   - step  : Stride or step count between indices. Defaults to 1.
#             If negative, traversal proceeds right-to-left (backwards).
#
# ==============================================================================
# REFERENCE TABLE: SLICING EXPRESSIONS & MEANINGS
# ==============================================================================
# | Expression | Meaning                                           |
# |------------|---------------------------------------------------|
# | s[:]       | Entire sequence (shallow copy)                    |
# | s[:3]      | First 3 elements (indices 0, 1, 2)                |
# | s[2:]      | From index 2 to the end                           |
# | s[-3:]     | Last 3 elements                                   |
# | s[::2]     | Every second element (step of 2)                  |
# | s[::-1]    | Reverse the sequence                              |
# | s[1:5]     | Elements from index 1 to 4 (5 is excluded)        |
# | s[-1]      | Last element only (single index, not slice)       |
# ==============================================================================

# ------------------------------------------------------------------------------
# POSITIVE VS NEGATIVE INDEXING VISUALIZATION
# ------------------------------------------------------------------------------
# String :    P    Y    T    H    O    N
# Positive:   0    1    2    3    4    5
# Negative:  -6   -5   -4   -3   -2   -1
# ------------------------------------------------------------------------------

print("==================================================================")
print("PYTHON SLICING EXAMPLES & PROGRAMS")
print("==================================================================")


# ------------------------------------------------------------------------------
# Program 1: Extract Substring from Middle (text[1:4])
# ------------------------------------------------------------------------------
# start = 1 ('Y'), stop = 4 ('O' excluded) -> indices 1, 2, 3 -> 'Y', 'T', 'H'
text = "PYTHON"
result1 = text[1:4]
print(f"1. Original: '{text}', Slice text[1:4]: '{result1}'")
# Expected Output: 'YTH'


# ------------------------------------------------------------------------------
# Program 2: Extract Prefix / First N Elements (text[:3])
# ------------------------------------------------------------------------------
# start is omitted -> defaults to 0. Stop = 3 (indices 0, 1, 2)
text = "COMPUTER"
result2 = text[:3]
print(f"2. Original: '{text}', Slice text[:3]: '{result2}'")
# Expected Output: 'COM'


# ------------------------------------------------------------------------------
# Program 3: Extract Suffix / From Index to End (text[4:])
# ------------------------------------------------------------------------------
# start = 4 ('R'), stop is omitted -> continues until the very end
text = "PROGRAMMING"
result3 = text[4:]
print(f"3. Original: '{text}', Slice text[4:]: '{result3}'")
# Expected Output: 'RAMMING'


# ------------------------------------------------------------------------------
# Program 4: Negative Indexing Suffix (text[-3:])
# ------------------------------------------------------------------------------
# start = -3 (third from last), stop is omitted -> last 3 characters
text = "PYTHON"
result4 = text[-3:]
print(f"4. Original: '{text}', Slice text[-3:]: '{result4}'")
# Expected Output: 'HON'


# ------------------------------------------------------------------------------
# Program 5: Reversing a Sequence with Negative Step (text[::-1])
# ------------------------------------------------------------------------------
# start and stop are omitted, step = -1 -> traverses backwards from end to start
text = "PYTHON"
result5 = text[::-1]
print(f"5. Original: '{text}', Slice text[::-1]: '{result5}'")
# Expected Output: 'NOHTYP'


# ------------------------------------------------------------------------------
# Additional Slicing Patterns for Mastery
# ------------------------------------------------------------------------------
print("\n--- Additional Step Patterns ---")

# Every second element (step = 2)
alphabet = "ABCDEFGH"
print(f"alphabet[::2] (Every 2nd char): '{alphabet[::2]}'")  # 'ACEG'

# Slice with custom start, stop, and step
# From index 1 to 7 with step 2: indices 1 ('B'), 3 ('D'), 5 ('F')
print(f"alphabet[1:7:2]: '{alphabet[1:7:2]}'")  # 'BDF'

# Reverse slice from index 5 down to 1
print(f"alphabet[5:1:-1]: '{alphabet[5:1:-1]}'")  # 'FEDC'

# Check if a word is a palindrome using slicing
word = "RACECAR"
is_palindrome = word == word[::-1]
print(f"Is '{word}' a palindrome? {is_palindrome}")

