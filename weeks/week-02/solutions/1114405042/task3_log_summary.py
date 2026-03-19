"""
Task 3: Log Summary

Count user events and find:
1. Total events per user (sorted by count descending, then name ascending)
2. Most frequent action globally

Uses Counter and/or defaultdict for counting.
"""

from collections import Counter, defaultdict


def _parse_logs(input_data):
    """
    Parse log entries from input.
    
    Args:
        input_data: String containing the input
    
    Returns:
        List of (user, action) tuples
    """
    lines = input_data.strip().split('\n')
    m = int(lines[0])
    
    logs = []
    for i in range(1, m + 1):
        parts = lines[i].split()
        user = parts[0]
        action = parts[1]
        logs.append((user, action))
    
    return logs


def _count_user_events(logs):
    """
    Count total events per user.
    
    Args:
        logs: List of (user, action) tuples
    
    Returns:
        Dictionary mapping user to event count
    """
    user_counts = defaultdict(int)
    for user, _ in logs:
        user_counts[user] += 1
    return user_counts


def _count_actions(logs):
    """
    Count occurrence of each action.
    
    Args:
        logs: List of (user, action) tuples
    
    Returns:
        Counter object with action counts
    """
    actions = [action for _, action in logs]
    return Counter(actions)


def _sort_users_by_count(user_counts):
    """
    Sort users by event count (descending), then by name (ascending).
    
    Args:
        user_counts: Dictionary mapping user to count
    
    Returns:
        Sorted list of (user, count) tuples
    """
    return sorted(user_counts.items(), key=lambda x: (-x[1], x[0]))


def summarize_logs(input_data):
    """
    Summarize user activity logs.
    
    Input format:
        Line 1: m (number of log entries)
        Lines 2 to m+1: user action
    
    Output:
        Lines showing users with their event counts (sorted by count desc, name asc)
        Final line: "top_action: action_name count"
    
    Args:
        input_data: String containing the input
    
    Returns:
        String with summary (one user per line, then top_action line)
    
    Example:
        Input:
            8
            alice login
            bob login
            alice view
            alice logout
            bob view
            bob view
            chris login
            bob logout
        
        Output:
            bob 4
            alice 3
            chris 1
            top_action: login 3
    """
    logs = _parse_logs(input_data)
    
    # Handle empty logs
    if not logs:
        return "top_action: 0\n"
    
    # Count users and actions
    user_counts = _count_user_events(logs)
    action_counts = _count_actions(logs)
    
    # Sort users
    sorted_users = _sort_users_by_count(user_counts)
    
    # Find top action
    top_action = action_counts.most_common(1)[0]
    
    # Format output
    result = []
    for user, count in sorted_users:
        result.append(f"{user} {count}")
    
    result.append(f"top_action: {top_action[0]} {top_action[1]}")
    
    return '\n'.join(result) + '\n'


def main():
    """Main function to read input and output summary"""
    m = int(input())
    
    user_counts = defaultdict(int)
    action_counts = Counter()
    
    for _ in range(m):
        line = input()
        parts = line.split()
        user = parts[0]
        action = parts[1]
        
        user_counts[user] += 1
        action_counts[action] += 1
    
    # Sort users
    sorted_users = sorted(user_counts.items(), key=lambda x: (-x[1], x[0]))
    
    # Output
    for user, count in sorted_users:
        print(f"{user} {count}")
    
    # Top action
    if action_counts:
        top_action = action_counts.most_common(1)[0]
        print(f"top_action: {top_action[0]} {top_action[1]}")


if __name__ == '__main__':
    main()
