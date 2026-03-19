"""
Task 1: Sequence Clean

Functions to process sequences:
1. Deduplicate while preserving first occurrence order
2. Sort ascending
3. Sort descending
4. Extract evens while preserving order
"""


def deduplicate_sequence(nums):
    """
    Remove duplicates from sequence, preserving first occurrence order.
    
    Uses hash set to track seen elements for O(n) time complexity.
    
    Args:
        nums: List of integers
    
    Returns:
        List with duplicates removed, first occurrence order preserved
    
    Example:
        deduplicate_sequence([5, 3, 5, 2, 9, 2, 8, 3, 1]) -> [5, 3, 2, 9, 8, 1]
    """
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


def _is_even(num):
    """Check if number is even."""
    return num % 2 == 0


def sort_ascending(nums):
    """
    Sort sequence in ascending order.
    
    Args:
        nums: List of integers
    
    Returns:
        List sorted in ascending order
    
    Example:
        sort_ascending([5, 3, 5, 2, 9, 2, 8, 3, 1]) -> [1, 2, 2, 3, 3, 5, 5, 8, 9]
    """
    return sorted(nums)


def sort_descending(nums):
    """
    Sort sequence in descending order.
    
    Args:
        nums: List of integers
    
    Returns:
        List sorted in descending order
    
    Example:
        sort_descending([5, 3, 5, 2, 9, 2, 8, 3, 1]) -> [9, 8, 5, 5, 3, 3, 2, 2, 1]
    """
    return sorted(nums, reverse=True)


def extract_evens(nums):
    """
    Extract even numbers from sequence, preserving original order.
    
    Args:
        nums: List of integers
    
    Returns:
        List of even numbers in original order
    
    Example:
        extract_evens([5, 3, 5, 2, 9, 2, 8, 3, 1]) -> [2, 2, 8]
    """
    return [num for num in nums if _is_even(num)]


def process_sequence(nums):
    """
    Process sequence and return all four transformations.
    
    Args:
        nums: List of integers
    
    Returns:
        Tuple of (dedupe, asc, desc, evens)
    """
    return (deduplicate_sequence(nums), 
            sort_ascending(nums),
            sort_descending(nums),
            extract_evens(nums))


def main():
    """Main function to process input from command line"""
    # Read input
    line = input("Enter numbers separated by spaces: ")
    nums = list(map(int, line.split()))
    
    # Process
    dedupe = deduplicate_sequence(nums)
    asc = sort_ascending(nums)
    desc = sort_descending(nums)
    evens = extract_evens(nums)
    
    # Output
    print(f"dedupe: {' '.join(map(str, dedupe))}")
    print(f"asc: {' '.join(map(str, asc))}")
    print(f"desc: {' '.join(map(str, desc))}")
    print(f"evens: {' '.join(map(str, evens))}")


if __name__ == '__main__':
    main()
