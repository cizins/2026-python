"""
Task 2: Student Ranking

Sort students by:
1. Score (high to low)
2. Age (low to high) when scores tied
3. Name (alphabetical) when score and age tied

Return top k students.
"""


def _parse_input(input_data):
    """
    Parse input data into (n, k, students).
    
    Args:
        input_data: String containing the input
    
    Returns:
        Tuple of (n, k, list of (name, score, age) tuples)
    """
    lines = input_data.strip().split('\n')
    first_line = lines[0].split()
    n, k = int(first_line[0]), int(first_line[1])
    
    students = []
    for i in range(1, n + 1):
        parts = lines[i].split()
        name = parts[0]
        score = int(parts[1])
        age = int(parts[2])
        students.append((name, score, age))
    
    return n, k, students


def _sort_by_ranking(students):
    """
    Sort students by ranking criteria:
    1. Score descending
    2. Age ascending (for ties)
    3. Name ascending (for further ties)
    
    Args:
        students: List of (name, score, age) tuples
    
    Returns:
        Sorted list of students
    """
    return sorted(students, key=lambda s: (-s[1], s[2], s[0]))


def rank_students(input_data):
    """
    Rank students according to multi-key sorting rules.
    
    Input format:
        Line 1: n k (number of students, top k to return)
        Lines 2 to n+1: name score age
    
    Output:
        k lines of "name score age" sorted by the rules
    
    Args:
        input_data: String containing the input
    
    Returns:
        String with ranked students (one per line)
    
    Example:
        Input:
            6 3
            amy 88 20
            bob 88 19
            zoe 92 21
            ian 88 19
            leo 75 20
            eva 92 20
        
        Output:
            eva 92 20
            zoe 92 21
            bob 88 19
    """
    n, k, students = _parse_input(input_data)
    sorted_students = _sort_by_ranking(students)
    top_k = sorted_students[:k]
    
    result = []
    for name, score, age in top_k:
        result.append(f"{name} {score} {age}")
    
    return '\n'.join(result) + '\n'


def main():
    """Main function to read input and output ranking"""
    # Read number of students and k
    n, k = map(int, input("Enter n k: ").split())
    
    students = []
    for _ in range(n):
        line = input()
        parts = line.split()
        name = parts[0]
        score = int(parts[1])
        age = int(parts[2])
        students.append((name, score, age))
    
    # Sort
    sorted_students = sorted(students, key=lambda x: (-x[1], x[2], x[0]))
    
    # Output top k
    for i in range(min(k, len(sorted_students))):
        name, score, age = sorted_students[i]
        print(f"{name} {score} {age}")


if __name__ == '__main__':
    main()
