from collections import defaultdict

MOD = 10**9 + 7


def count_loading_ways(h: list[int], CA: int, CB: int, D: int) -> int:
    # Early exit if total weight exceeds combined capacity
    if sum(h) > CA + CB:
        return 0

    # dp[diff] = number of ways where (weight_A - weight_B) == diff
    dp = {0: 1}
    total_prev = 0

    for w in h:
        next_dp = defaultdict(int)
        for diff, ways in dp.items():
            wA = (total_prev + diff) // 2
            wB = total_prev - wA

            # Option 1: Load package onto Ship A
            if wA + w <= CA and abs(diff + w) <= D:
                next_dp[diff + w] = (next_dp[diff + w] + ways) % MOD

            # Option 2: Load package onto Ship B
            if wB + w <= CB and abs(diff - w) <= D:
                next_dp[diff - w] = (next_dp[diff - w] + ways) % MOD

        dp = next_dp
        total_prev += w
        if not dp:
            return 0

    return sum(dp.values()) % MOD


if __name__ == "__main__":
    test_cases = [
        # (h, CA, CB, D, expected_output, description)
        ([2, 2, 1], 3, 3, 2, 4, "Standard valid combinations"),
        ([1, 1, 1, 1], 2, 2, 1, 4, "Tight difference D=1 forces alternating"),
        ([5, 2], 4, 4, 10, 0, "Impossible: Single package exceeds capacities"),
        ([3, 3], 6, 6, 2, 0, "Impossible: First package violates D=2"),
        ([2, 2, 2], 4, 2, 2, 2, "Asymmetric capacities (CA=4, CB=2)"),
        ([1] * 30, 30, 30, 30, (2**30) % MOD, "Large count testing MOD = 10^9 + 7"),
        ([], 5, 5, 2, 1, "Empty packages list"),
    ]

    for i, (h, CA, CB, D, expected, desc) in enumerate(test_cases, 1):
        result = count_loading_ways(h, CA, CB, D)
        assert result == expected, f"Test {i} failed: got {result}, expected {expected}"
        print(f"Test {i} PASSED ({desc}): output = {result}")