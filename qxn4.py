
from datetime import datetime
from collections import Counter


def find_peak_usage(logs):

    if not logs:
        # If logs list is empty, return 0 as a default
        return 0

    # Extract the hour from each timestamp
    hours = []
    for timestamp in logs:
        # Parse the ISO format string into a datetime object
        dt = datetime.fromisoformat(timestamp)
        hours.append(dt.hour)

    # Count occurrences of each hour
    hour_counts = Counter(hours)

    # Find the maximum count
    max_count = max(hour_counts.values())

    # Get all hours that have the maximum count, then return the smallest (earliest) hour
    peak_hours = [hour for hour, count in hour_counts.items() if count == max_count]
    return min(peak_hours)


# ============================================================================
# Test the function with sample data
# ============================================================================
if __name__ == "__main__":
    print("=" * 50)
    print("Question 4 - Peak Login Hour Finder")
    print("=" * 50)

    # Test Case 1: Normal scenario with one peak hour
    print("\n--- Test Case 1: Normal Scenario ---")
    sample_logs = [
        "2026-08-04T13:21:18",
        "2026-08-04T14:05:10",
        "2026-08-04T14:45:22",
        "2026-08-04T15:10:05",
        "2026-08-04T14:30:55",
        "2026-08-04T22:15:40",
        "2026-08-04T22:45:12",
        "2026-08-04T22:50:33"
    ]
    print("Sample logs:")
    for log in sample_logs:
        print(f"  {log}")

    peak_hour = find_peak_usage(sample_logs)
    print(f"\nPeak login hour: {peak_hour} (0-23)")

    # Test Case 2: Tie scenario (two hours have same number of logins)
    print("\n--- Test Case 2: Tie Scenario ---")
    tie_logs = [
        "2026-08-04T10:00:00",
        "2026-08-04T10:30:00",
        "2026-08-04T11:00:00",
        "2026-08-04T11:30:00"
    ]
    print("Tie test logs:")
    for log in tie_logs:
        print(f"  {log}")

    peak_hour_tie = find_peak_usage(tie_logs)
    print(f"\nPeak login hour (tie, earliest): {peak_hour_tie} (0-23)")

    # Test Case 3: Empty list
    print("\n--- Test Case 3: Empty List ---")
    empty_logs = []
    print("Empty logs list")
    peak_hour_empty = find_peak_usage(empty_logs)
    print(f"Peak login hour (empty): {peak_hour_empty}")

    # Test Case 4: All logins in same hour
    print("\n--- Test Case 4: All Logins in Same Hour ---")
    same_hour_logs = [
        "2026-08-04T15:10:20",
        "2026-08-04T15:25:45",
        "2026-08-04T15:40:10"
    ]
    print("Same hour logs:")
    for log in same_hour_logs:
        print(f"  {log}")

    peak_hour_same = find_peak_usage(same_hour_logs)
    print(f"\nPeak login hour: {peak_hour_same} (0-23)")