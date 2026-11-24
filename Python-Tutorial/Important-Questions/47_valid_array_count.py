MOD = 10**9 + 7

def count_divisible_arrays(n: int, k: int) -> int:
    if k == 0 or n == 0:
        return 0

    # dp[length][num] = number of valid arrays of length `length`
    # ending with value `num`
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    # Base case: arrays of length 1 ending at any number from 1 to n 
    for num in range(1, n + 1):
        dp[1][num] = 1

    # Build arrays of length 2 up to k 
    for length in range(2, k + 1):
        for num in range(1, n + 1):
            total_ways = dp[length][num]

            # Check divisors d up to sqrt(num) to optimize time complexity 
            d = 1
            while d * d <= num:
                if num % d == 0:
                    # Case 1: previous element is `d`
                    if d < num:
                        total_ways = (total_ways + dp[length - 1][d]) % MOD

                    # Case 2: paired divisor `num // d`
                    paired_d = num // d
                    if paired_d != d and paired_d < num:
                        total_ways = (total_ways + dp[length - 1][paired_d]) % MOD

                d += 1

            dp[length][num] = total_ways

    # Sum all valid arrays of exact length k across all possible ending values
    ans = 0
    for num in range(1, n + 1):
        ans = (ans + dp[k][num]) % MOD

    print(*dp)
    return ans


print(count_divisible_arrays(4, 2))