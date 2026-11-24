def min_launch_weeks(chapters: list[list[int]], max_hr: int) -> int:
    n = len(chapters)
    weeks = 0
    i = 0

    while i < n:
        cur_hr = 0
        last_valid = -1
        j = i

        # Extend current week as far as possible within max_hr
        while j < n and cur_hr + chapters[j][0] <= max_hr:
            cur_hr += chapters[j][0]
            # Valid end only if it has no cliffhanger or is the very last chapter
            if j == n - 1 or chapters[j][1] == 0:
                last_valid = j
            j += 1

        if last_valid == -1:
            return -1  # No valid batch can start at chapter i

        weeks += 1
        i = last_valid + 1

    return weeks


if __name__ == "__main__":
    test_cases = [
        # (chapters, max_hr, expected_output, description)
        ([[3, 0], [3, 0]], 6, 1, "Example 1: Single week, no cliffhangers"),
        ([[2, 0], [2, 1], [2, 0], [2, 1]], 4, 3, "Example 2: Cliffhanger forces split"),
        ([[3, 0], [3, 1], [3, 0]], 6, 2, "Example 3: Two weeks (assuming max_hr = 6)"),
        ([[3, 0], [7, 0]], 6, -1, "Impossible: Single chapter exceeds max_hr"),
        ([[3, 1], [3, 0]], 5, -1, "Impossible: Cliffhanger cannot be paired within max_hr"),
        ([[2, 1], [2, 1], [2, 1]], 6, 1, "All cliffhangers, but fits in 1 final week"),
        ([[1, 0], [1, 1], [1, 1], [1, 0], [1, 1]], 3, 3, "Cliffhanger block forces backtrack then jump"),
        ([], 5, 0, "Empty chapters list"),
    ]

    for i, (chapters, max_hr, expected, desc) in enumerate(test_cases, 1):
        result = min_launch_weeks(chapters, max_hr)
        assert result == expected, f"Test {i} failed: got {result}, expected {expected}"
        print(f"Test {i} PASSED ({desc}): output = {result}")