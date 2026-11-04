# ==============================================================================
# PYTHON NATIVE ARRAYS, CORE ALGORITHMS & FUNDAMENTAL STRUCTURES
# ==============================================================================
# In Python, arrays can be implemented using lists, which allow us to store
# multiple values in a single variable. Python also provides the 'array' module
# for storing elements of strictly homogeneous data types, and NumPy for
# multi-dimensional numeric computing.
#
# Topics covered:
# 1. Array Creation, Access & Iteration
# 2. Algorithm 1: Computing Sum of Elements (Loop-based)
# 3. Algorithm 2: Finding Largest Element (Loop-based)
# 4. Algorithm 3: Insertion (append)
# 5. Algorithm 4: Deletion (remove)
# 6. Algorithm 5: Linear Search (Membership test 'in')
# 7. Algorithm 6: Array Slicing (Subarrays & Reversal)
# 8. Core Data Structures: Lists vs Dictionaries
# 9. Control Flow: Conditional Decision Making (if / elif / else)
# 10. Reusable Functions: Definition, Return Values & Invocations
# ==============================================================================

print("==================================================================")
print("1. ARRAY CREATION, DISPLAY & INDEX ACCESS")
print("==================================================================")

# Create an array implemented via a list
arr = [10, 20, 30, 40, 50]
print("Array elements:", arr)

# Access specific elements by index
print("First element (index 0):", arr[0])
print("Third element (index 2):", arr[2])
print("Last element (index -1):", arr[-1])

# Traversing array elements sequentially
print("\nTraversing array elements with a for loop:")
for i in arr:
    print(f" -> {i}")


print("\n==================================================================")
print("2. ALGORITHM: SUM OF ARRAY ELEMENTS")
print("==================================================================")
# Calculating sum manually without using Python's built-in sum()
arr = [10, 20, 30, 40, 50]
total = 0

for i in arr:
    total = total + i

print(f"Array: {arr}")
print("Sum of array elements:", total)


print("\n==================================================================")
print("3. ALGORITHM: FINDING LARGEST ELEMENT")
print("==================================================================")
# Finding the maximum element manually without using built-in max()
arr_unsorted = [25, 10, 45, 30, 15]
largest = arr_unsorted[0]

for i in arr_unsorted:
    if i > largest:
        largest = i

print(f"Array: {arr_unsorted}")
print("Largest element:", largest)


print("\n==================================================================")
print("4. ARRAY MODIFICATIONS: INSERTION & DELETION")
print("==================================================================")
# Insertion: Adding an element to the end of the array using .append()
arr_modify = [10, 20, 30, 40]
print("Original array:", arr_modify)
arr_modify.append(50)
print("Array after insertion (append 50):", arr_modify)

# Deletion: Removing a specific value using .remove()
arr_modify.remove(30)
print("Array after deletion (remove 30):", arr_modify)


print("\n==================================================================")
print("5. ALGORITHM: LINEAR SEARCH")
print("==================================================================")
# Searching for an element using membership testing
arr_search = [10, 20, 30, 40, 50]

def search_element(target_array, search_key):
    """Searches for search_key in target_array and reports existence and index."""
    if search_key in target_array:
        idx = target_array.index(search_key)
        print(f"Key {search_key}: Element found at index {idx}")
        return True
    else:
        print(f"Key {search_key}: Element not found")
        return False

# Demonstration with existing and non-existing keys
print(f"Target array: {arr_search}")
search_element(arr_search, 30)   # Element found
search_element(arr_search, 99)   # Element not found


print("\n==================================================================")
print("6. ARRAY SLICING: SUBARRAYS & REVERSAL")
print("==================================================================")
arr_slice = [10, 20, 30, 40, 50]
print("Original array:", arr_slice)
print("First three elements (arr[:3]):", arr_slice[:3])
print("Last two elements (arr[-2:]):", arr_slice[-2:])
print("Reversed array (arr[::-1]):", arr_slice[::-1])


print("\n==================================================================")
print("7. CORE PYTHON STRUCTURES: LISTS VS DICTIONARIES")
print("==================================================================")
# Lists: Ordered, mutable collections of items accessed by numeric index
fruits = ["apple", "banana", "cherry"]
print("Lists (Ordered, zero-indexed):")
print("Fruits list:", fruits)
print("First fruit (fruits[0]):", fruits[0])

# Dictionaries: Unordered/insertion-ordered Key-Value pairs for fast O(1) lookups
user_profile = {
    "username": "coder123",
    "score": 95,
    "active": True
}
print("\nDictionaries (Key-Value mappings):")
print("User profile dict:", user_profile)
print("Lookup 'username':", user_profile["username"])
print("Lookup 'score':", user_profile["score"])
print("Lookup 'active':", user_profile["active"])


print("\n==================================================================")
print("8. CONTROL FLOW: CONDITIONAL DECISION MAKING")
print("==================================================================")
# Evaluating conditions with if / elif / else blocks
score = 85

print(f"Student Score: {score}")
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"

print(f"Calculated Grade: {grade}")


print("\n==================================================================")
print("9. REUSABLE FUNCTIONS")
print("==================================================================")
# Functions encapsulate reusable logic with parameters and return values
def greet_user(user_name):
    """Returns a personalized greeting message."""
    message = f"Hello, {user_name}! Welcome to Google Colab & Data Science Lab."
    return message

# Invoking function
welcome_msg = greet_user("Alice")
print(welcome_msg)
print(greet_user("Ravi"))

