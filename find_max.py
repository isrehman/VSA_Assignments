#!/usr/bin/env python3
"""
Find the maximum element in a list using linear search — O(n) time, O(1) space.

Requires Python 3.13+
"""

# PEP 695 type alias (Python 3.12+, preferred in 3.13+)
type Number = int | float


def find_max(arr: list[Number]) -> Number | None:
    """
    Return the maximum element in arr.

    Args:
        arr: A list of integers or floats.

    Returns:
        The maximum element, or None (with a warning) if arr is empty.
    """
    if not arr:
        print("Warning: empty array provided.")
        return None

    max_val: Number = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num

    return max_val


if __name__ == "__main__":
    test_cases: list[tuple[list[Number], Number | None]] = [
        ([3, 1, 4, 1, 5, 9, 2, 6], 9),
        ([-10, -3, -7, -1, -5],    -1),
        ([42],                      42),
        ([0],                        0),
        ([-1, -2, -3],              -1),
        ([1.5, 3.7, 2.2],          3.7),
        ([],                        None),
    ]

    all_passed = True
    for arr, expected in test_cases:
        result = find_max(arr)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"{status}  find_max({arr!r}) = {result!r}  (expected {expected!r})")

    print()
    print("All tests passed." if all_passed else "Some tests FAILED.")
