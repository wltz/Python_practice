#!/usr/bin/env python3
"""
Comprehensive List Use Cases in Python
This file demonstrates various list operations, methods, and practical examples.
"""

def basic_list_operations():
    """Basic list creation and fundamental operations"""
    print("=== BASIC LIST OPERATIONS ===")
    
    # Creating lists
    numbers = [1, 2, 3, 4, 5]
    fruits = ['apple', 'banana', 'cherry']
    mixed = [1, 'hello', 3.14, True]
    empty_list = []
    
    print(f"Numbers: {numbers}")
    print(f"Fruits: {fruits}")
    print(f"Mixed types: {mixed}")
    print(f"Empty list: {empty_list}")
    
    # Accessing elements
    print(f"First fruit: {fruits[0]}")
    print(f"Last number: {numbers[-1]}")
    print(f"Second to fourth numbers: {numbers[1:4]}")
    
    # List methods
    fruits.append('orange')
    print(f"After append: {fruits}")
    
    fruits.insert(1, 'grape')
    print(f"After insert: {fruits}")
    
    fruits.remove('banana')
    print(f"After remove: {fruits}")
    
    popped = fruits.pop()
    print(f"Popped item: {popped}, Remaining: {fruits}")
    
    print(f"Length of numbers: {len(numbers)}")
    print(f"'apple' in fruits: {'apple' in fruits}")
    
    print()


def list_comprehension_examples():
    """List comprehension - Python's elegant way to create lists"""
    print("=== LIST COMPREHENSION EXAMPLES ===")
    
    # Basic comprehension
    squares = [x**2 for x in range(1, 6)]
    print(f"Squares: {squares}")
    
    # With condition
    even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
    print(f"Even squares: {even_squares}")
    
    # String operations
    words = ['hello', 'world', 'python', 'programming']
    upper_words = [word.upper() for word in words]
    print(f"Upper case words: {upper_words}")
    
    # Length filtering
    long_words = [word for word in words if len(word) > 5]
    print(f"Long words: {long_words}")
    
    # Nested comprehension
    matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
    print(f"Multiplication table: {matrix}")
    
    # Dictionary comprehension from list
    word_lengths = {word: len(word) for word in words}
    print(f"Word lengths: {word_lengths}")
    
    print()


def nested_lists_and_2d_operations():
    """Working with nested lists and 2D data structures"""
    print("=== NESTED LISTS AND 2D OPERATIONS ===")
    
    # Creating 2D lists
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(f"3x3 Matrix: {matrix}")
    
    # Accessing elements
    print(f"Element at [1][2]: {matrix[1][2]}")
    print(f"Second row: {matrix[1]}")
    print(f"First column: {[row[0] for row in matrix]}")
    
    # Transposing matrix
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print(f"Transposed: {transposed}")
    
    # Flattening nested list
    flattened = [item for row in matrix for item in row]
    print(f"Flattened: {flattened}")
    
    # Student grades example
    students = [
        ['Alice', [85, 90, 78]],
        ['Bob', [92, 88, 95]],
        ['Charlie', [76, 82, 80]]
    ]
    
    print("\nStudent grades:")
    for student, grades in students:
        avg_grade = sum(grades) / len(grades)
        print(f"{student}: {grades} (Average: {avg_grade:.1f})")
    
    print()


def list_slicing_and_manipulation():
    """Advanced slicing and list manipulation techniques"""
    print("=== LIST SLICING AND MANIPULATION ===")
    
    data = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original data: {data}")
    
    # Basic slicing
    print(f"First 3: {data[:3]}")
    print(f"Last 3: {data[-3:]}")
    print(f"Middle 3: {data[3:6]}")
    print(f"Every 2nd element: {data[::2]}")
    print(f"Reverse: {data[::-1]}")
    
    # Modifying slices
    data_copy = data.copy()
    data_copy[2:5] = [100, 200, 300]
    print(f"Modified slice: {data_copy}")
    
    # Deleting slices
    data_copy = data.copy()
    del data_copy[1:4]
    print(f"After deleting slice: {data_copy}")
    
    # List concatenation and repetition
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined = list1 + list2
    print(f"Combined: {combined}")
    print(f"Repeated: {list1 * 3}")
    
    print()


def sorting_and_filtering():
    """Sorting, filtering, and searching operations"""
    print("=== SORTING AND FILTERING ===")
    
    # Basic sorting
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {numbers}")
    
    sorted_asc = sorted(numbers)
    print(f"Sorted ascending: {sorted_asc}")
    
    sorted_desc = sorted(numbers, reverse=True)
    print(f"Sorted descending: {sorted_desc}")
    
    # In-place sorting
    numbers_copy = numbers.copy()
    numbers_copy.sort()
    print(f"In-place sorted: {numbers_copy}")
    
    # Sorting with key function
    words = ['apple', 'pie', 'banana', 'cherry']
    sorted_by_length = sorted(words, key=len)
    print(f"Sorted by length: {sorted_by_length}")
    
    # Filtering
    even_numbers = [x for x in numbers if x % 2 == 0]
    print(f"Even numbers: {even_numbers}")
    
    # Using filter function
    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
    print(f"Odd numbers: {odd_numbers}")
    
    # Finding elements
    print(f"Index of 25: {numbers.index(25)}")
    print(f"Count of 12: {numbers.count(12)}")
    print(f"Max: {max(numbers)}, Min: {min(numbers)}")
    
    print()


def practical_real_world_examples():
    """Real-world practical examples using lists"""
    print("=== PRACTICAL REAL-WORLD EXAMPLES ===")
    
    # 1. Shopping Cart
    print("1. Shopping Cart Management:")
    cart = []
    cart.extend(['laptop', 'mouse', 'keyboard'])
    print(f"Initial cart: {cart}")
    
    # Add quantities
    cart_with_quantities = [(item, 1) for item in cart]
    print(f"Cart with quantities: {cart_with_quantities}")
    
    # 2. Student Grade Management
    print("\n2. Student Grade Management:")
    student_grades = {
        'Alice': [85, 90, 78, 92],
        'Bob': [88, 76, 95, 89],
        'Charlie': [92, 88, 90, 85]
    }
    
    for student, grades in student_grades.items():
        avg = sum(grades) / len(grades)
        max_grade = max(grades)
        min_grade = min(grades)
        print(f"{student}: Avg={avg:.1f}, Max={max_grade}, Min={min_grade}")
    
    # 3. Data Processing
    print("\n3. Data Processing:")
    sales_data = [120, 150, 180, 200, 160, 140, 190, 210, 170, 130]
    print(f"Sales data: {sales_data}")
    
    # Calculate statistics
    total_sales = sum(sales_data)
    avg_sales = total_sales / len(sales_data)
    above_average = [x for x in sales_data if x > avg_sales]
    
    print(f"Total sales: {total_sales}")
    print(f"Average sales: {avg_sales:.2f}")
    print(f"Days above average: {above_average}")
    
    # 4. Text Processing
    print("\n4. Text Processing:")
    text = "Python is a great programming language for data science"
    words = text.split()
    print(f"Words: {words}")
    
    # Word frequency
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    print(f"Word frequency: {word_freq}")
    
    # Longest word
    longest_word = max(words, key=len)
    print(f"Longest word: {longest_word}")
    
    # 5. Matrix Operations
    print("\n5. Matrix Operations:")
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    
    # Matrix addition
    result = [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] 
              for i in range(len(matrix_a))]
    print(f"Matrix A: {matrix_a}")
    print(f"Matrix B: {matrix_b}")
    print(f"A + B: {result}")
    
    print()


def advanced_list_techniques():
    """Advanced list techniques and optimizations"""
    print("=== ADVANCED LIST TECHNIQUES ===")
    
    # 1. List unpacking
    print("1. List Unpacking:")
    coordinates = [3, 4, 5]
    x, y, z = coordinates
    print(f"Coordinates: x={x}, y={y}, z={z}")
    
    # Unpacking with rest
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    first, second, *rest, last = numbers
    print(f"First: {first}, Second: {second}, Rest: {rest}, Last: {last}")
    
    # 2. List as stack (LIFO)
    print("\n2. List as Stack:")
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print(f"Stack: {stack}")
    
    while stack:
        popped = stack.pop()
        print(f"Popped: {popped}, Remaining: {stack}")
    
    # 3. List as queue (FIFO)
    print("\n3. List as Queue:")
    from collections import deque
    queue = deque()
    queue.append(1)
    queue.append(2)
    queue.append(3)
    print(f"Queue: {list(queue)}")
    
    while queue:
        removed = queue.popleft()
        print(f"Removed: {removed}, Remaining: {list(queue)}")
    
    # 4. List copying techniques
    print("\n4. List Copying:")
    original = [1, 2, [3, 4]]
    
    # Shallow copy
    shallow = original.copy()
    shallow[2][0] = 999
    print(f"Original after shallow copy modification: {original}")
    
    # Deep copy
    import copy
    original = [1, 2, [3, 4]]
    deep = copy.deepcopy(original)
    deep[2][0] = 999
    print(f"Original after deep copy modification: {original}")
    
    # 5. List performance tips
    print("\n5. Performance Tips:")
    # Use list comprehension instead of loops
    import time
    
    # Inefficient way
    start = time.time()
    result1 = []
    for i in range(100000):
        result1.append(i * 2)
    time1 = time.time() - start
    
    # Efficient way
    start = time.time()
    result2 = [i * 2 for i in range(100000)]
    time2 = time.time() - start
    
    print(f"Loop method time: {time1:.4f}s")
    print(f"List comprehension time: {time2:.4f}s")
    print(f"Speed improvement: {time1/time2:.1f}x faster")
    
    print()


def mixed_type_lists_benefits():
    """Demonstrates benefits and use cases of mixed-type lists"""
    print("=== BENEFITS OF MIXED-TYPE LISTS ===")
    
    # 1. Data Records and Structured Information
    print("1. Data Records and Structured Information:")
    # Each sublist represents a person with different data types
    people = [
        ["Alice", 25, 5.6, True, "Engineer"],      # [name, age, height, employed, job]
        ["Bob", 30, 6.0, False, "Student"],
        ["Charlie", 35, 5.9, True, "Manager"]
    ]
    
    print("People data (name, age, height, employed, job):")
    for person in people:
        name, age, height, employed, job = person
        status = "Employed" if employed else "Unemployed"
        print(f"  {name}: {age} years, {height}ft, {status}, {job}")
    
    # 2. Configuration Settings
    print("\n2. Configuration Settings:")
    # Mixed types for different configuration values
    config = [
        "database_host",      # string
        "localhost",          # string
        5432,                 # int (port)
        True,                 # bool (ssl enabled)
        3.5,                  # float (timeout in seconds)
        ["user1", "user2"]    # list (allowed users)
    ]
    
    print("Configuration settings:")
    print(f"  Host: {config[1]} (type: {type(config[1]).__name__})")
    print(f"  Port: {config[2]} (type: {type(config[2]).__name__})")
    print(f"  SSL: {config[3]} (type: {type(config[3]).__name__})")
    print(f"  Timeout: {config[4]}s (type: {type(config[4]).__name__})")
    print(f"  Users: {config[5]} (type: {type(config[5]).__name__})")
    
    # 3. API Response Data
    print("\n3. API Response Data:")
    api_response = [
        "success",                    # status
        200,                         # status_code
        {"user_id": 123, "name": "John"},  # data dict
        ["error1", "error2"],        # errors list
        0.045                        # response_time
    ]
    
    status, code, data, errors, response_time = api_response
    print(f"  Status: {status}")
    print(f"  Code: {code}")
    print(f"  Data: {data}")
    print(f"  Errors: {errors}")
    print(f"  Response time: {response_time}s")
    
    # 4. Mixed Data Processing
    print("\n4. Mixed Data Processing:")
    mixed_data = [
        "temperature", 25.5, "Celsius",
        "humidity", 60, "percent",
        "pressure", 1013.25, "hPa",
        "wind_speed", 15.2, "km/h"
    ]
    
    # Process pairs of (label, value, unit)
    for i in range(0, len(mixed_data), 3):
        label = mixed_data[i]
        value = mixed_data[i + 1]
        unit = mixed_data[i + 2]
        print(f"  {label}: {value} {unit}")
    
    # 5. Benefits Analysis
    print("\n5. Benefits of Mixed-Type Lists:")
    print("  ✓ Flexibility: Store different data types together")
    print("  ✓ Memory efficiency: No need for separate variables")
    print("  ✓ Easy iteration: Process related data as a group")
    print("  ✓ Data structure: Represent complex records simply")
    print("  ✓ API compatibility: Handle varied response formats")
    print("  ✓ Configuration: Store settings of different types")
    
    # 6. When to Use vs When NOT to Use
    print("\n6. When to Use Mixed-Type Lists:")
    print("  ✓ Configuration settings")
    print("  ✓ API responses with varied data")
    print("  ✓ Database records")
    print("  ✓ Log entries with different data types")
    print("  ✓ Command-line arguments")
    
    print("\n  When NOT to use (use alternatives instead):")
    print("  ✗ When you need type safety → Use namedtuples or dataclasses")
    print("  ✗ When data has clear structure → Use dictionaries or classes")
    print("  ✗ When you need validation → Use Pydantic models")
    print("  ✗ When performance is critical → Use NumPy arrays")
    
    # 7. Better Alternatives for Structured Data
    print("\n7. Better Alternatives for Structured Data:")
    
    # Using namedtuple (better for structured data)
    from collections import namedtuple
    Person = namedtuple('Person', ['name', 'age', 'height', 'employed', 'job'])
    
    people_structured = [
        Person("Alice", 25, 5.6, True, "Engineer"),
        Person("Bob", 30, 6.0, False, "Student"),
        Person("Charlie", 35, 5.9, True, "Manager")
    ]
    
    print("Using namedtuple (better for structured data):")
    for person in people_structured:
        print(f"  {person.name}: {person.age} years, {person.height}ft")
        print(f"    Employed: {person.employed}, Job: {person.job}")
    
    # Using dictionary (better for key-value data)
    config_dict = {
        "host": "localhost",
        "port": 5432,
        "ssl_enabled": True,
        "timeout": 3.5,
        "allowed_users": ["user1", "user2"]
    }
    
    print("\nUsing dictionary (better for configuration):")
    for key, value in config_dict.items():
        print(f"  {key}: {value} ({type(value).__name__})")
    
    print()


def list_extend_vs_other_methods():
    """Demonstrates list.extend() and compares it with other list addition methods"""
    print("=== LIST.EXTEND() VS OTHER ADDITION METHODS ===")
    
    # 1. Basic extend() usage
    print("1. Basic list.extend() usage:")
    fruits = ['apple', 'banana']
    more_fruits = ['cherry', 'date', 'elderberry']
    
    print(f"Original fruits: {fruits}")
    print(f"More fruits to add: {more_fruits}")
    
    fruits.extend(more_fruits)
    print(f"After extend(): {fruits}")
    
    # 2. extend() vs append() - Key Difference
    print("\n2. extend() vs append() - The Key Difference:")
    
    # Using append() - adds the entire list as ONE element
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list1.append(list2)
    print(f"After append([4,5,6]): {list1} (length: {len(list1)})")
    print(f"Last element: {list1[-1]} (type: {type(list1[-1])})")
    
    # Using extend() - adds each element individually
    list3 = [1, 2, 3]
    list4 = [4, 5, 6]
    list3.extend(list4)
    print(f"After extend([4,5,6]): {list3} (length: {len(list3)})")
    print(f"Last element: {list3[-1]} (type: {type(list3[-1])})")
    
    # 3. extend() with different iterables
    print("\n3. extend() with different iterables:")
    
    numbers = [1, 2, 3]
    print(f"Original: {numbers}")
    
    # Extend with a string (each character becomes an element)
    numbers.extend("abc")
    print(f"After extend('abc'): {numbers}")
    
    # Extend with a tuple
    numbers.extend((7, 8, 9))
    print(f"After extend((7,8,9)): {numbers}")
    
    # Extend with a set (order may vary)
    numbers.extend({10, 11, 12})
    print(f"After extend({{10,11,12}}): {numbers}")
    
    # Extend with a range
    numbers.extend(range(13, 16))
    print(f"After extend(range(13,16)): {numbers}")
    
    # 4. extend() vs += operator
    print("\n4. extend() vs += operator:")
    
    # Using extend()
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    list_a.extend(list_b)
    print(f"Using extend(): {list_a}")
    
    # Using += (equivalent to extend())
    list_c = [1, 2, 3]
    list_d = [4, 5, 6]
    list_c += list_d
    print(f"Using +=: {list_c}")
    
    # 5. Performance comparison
    print("\n5. Performance comparison:")
    import time
    
    # Method 1: extend()
    start = time.time()
    result1 = []
    for i in range(10000):
        result1.extend([i, i+1, i+2])
    time1 = time.time() - start
    
    # Method 2: append() in loop
    start = time.time()
    result2 = []
    for i in range(10000):
        result2.append(i)
        result2.append(i+1)
        result2.append(i+2)
    time2 = time.time() - start
    
    # Method 3: += operator
    start = time.time()
    result3 = []
    for i in range(10000):
        result3 += [i, i+1, i+2]
    time3 = time.time() - start
    
    # Method 4: List comprehension (for comparison)
    start = time.time()
    result4 = [item for i in range(10000) for item in [i, i+1, i+2]]
    time4 = time.time() - start
    
    print(f"extend() method: {time1:.4f}s")
    print(f"append() in loop: {time2:.4f}s")
    print(f"+= operator: {time3:.4f}s")
    print(f"List comprehension: {time4:.4f}s")
    print(f"extend() is {time2/time1:.1f}x faster than append() in loop")
    
    # 6. Practical use cases for extend()
    print("\n6. Practical use cases for extend():")
    
    # Building a shopping list
    shopping_list = ['milk', 'bread']
    fruits = ['apple', 'banana', 'orange']
    vegetables = ['carrot', 'lettuce']
    
    shopping_list.extend(fruits)
    shopping_list.extend(vegetables)
    print(f"Shopping list: {shopping_list}")
    
    # Processing multiple data sources
    all_data = []
    data_source1 = [1, 2, 3]
    data_source2 = [4, 5, 6]
    data_source3 = [7, 8, 9]
    
    all_data.extend(data_source1)
    all_data.extend(data_source2)
    all_data.extend(data_source3)
    print(f"Combined data: {all_data}")
    
    # 7. When to use extend() vs other methods
    print("\n7. When to use extend() vs other methods:")
    print("Use extend() when:")
    print("  ✓ Adding multiple elements from another iterable")
    print("  ✓ Combining two lists")
    print("  ✓ Adding elements from a loop")
    print("  ✓ Performance is important (faster than multiple appends)")
    
    print("\nUse append() when:")
    print("  ✓ Adding a single element")
    print("  ✓ Adding the entire iterable as one element")
    print("  ✓ Building a list of lists")
    
    print("\nUse += when:")
    print("  ✓ You want concise syntax (equivalent to extend())")
    print("  ✓ Adding elements from another list")
    
    # 8. Common mistakes and gotchas
    print("\n8. Common mistakes and gotchas:")
    
    # Mistake 1: Using extend() with a single element
    print("Mistake 1: extend() with single element")
    wrong_list = [1, 2, 3]
    try:
        wrong_list.extend(4)  # This will cause an error
    except TypeError as e:
        print(f"  Error: {e}")
        print("  Fix: Use append(4) instead of extend(4)")
    
    # Mistake 2: Confusing extend() and append()
    print("\nMistake 2: Confusing extend() and append()")
    list_extend = [1, 2, 3]
    list_append = [1, 2, 3]
    
    list_extend.extend([4, 5])  # Adds 4 and 5 as separate elements
    list_append.append([4, 5])  # Adds [4, 5] as one element
    
    print(f"extend([4,5]): {list_extend}")
    print(f"append([4,5]): {list_append}")
    
    # 9. Advanced extend() techniques
    print("\n9. Advanced extend() techniques:")
    
    # Extending with generator expressions
    numbers = [1, 2, 3]
    squares = (x**2 for x in range(4, 7))  # Generator
    numbers.extend(squares)
    print(f"Extended with generator: {numbers}")
    
    # Extending with filtered data
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = [x for x in data if x % 2 == 0]
    result = [1, 2, 3]
    result.extend(even_numbers)
    print(f"Extended with filtered data: {result}")
    
    # Chaining extend() operations
    final_list = []
    final_list.extend([1, 2, 3])
    final_list.extend([4, 5, 6])
    final_list.extend([7, 8, 9])
    print(f"Chained extends: {final_list}")
    
    print()


def main():
    """Run all list use case examples"""
    print("PYTHON LIST USE CASES DEMONSTRATION")
    print("=" * 50)
    
    basic_list_operations()
    list_comprehension_examples()
    nested_lists_and_2d_operations()
    list_slicing_and_manipulation()
    sorting_and_filtering()
    practical_real_world_examples()
    advanced_list_techniques()
    mixed_type_lists_benefits()
    list_extend_vs_other_methods()
    
    print("=" * 50)
    print("All list use cases completed!")


if __name__ == "__main__":
    main()
