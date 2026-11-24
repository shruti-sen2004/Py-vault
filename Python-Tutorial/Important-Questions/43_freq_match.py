# Similar to Leetcode 1863. Sum of All Subset XOR Totals

def get_crystal_subset_xor_sum(N: int, C: int, F: list[int]) -> int:
    matched_count = 0
    or_sum = 0
    
    # 1. Filter elements matching the condition and calculate their OR sum
    for x in F:
        if (x & C) > 0:
            matched_count += 1
            or_sum |= x  # Bitwise OR operation
            
    # 2. If no crystals match, the only subset is empty {} which sums to 0
    if matched_count == 0:
        return 0
        
    # 3. Apply the mathematical formula: OR_SUM * 2^(M-1)
    # Using bitwise left shift (1 << (matched_count - 1)) is faster than 2**(matched_count-1)
    # Note: If the platform requires modulo for large numbers, wrap the return like: 
    # return (or_sum * (1 << (matched_count - 1))) % (10**9 + 7)
    return or_sum * (1 << (matched_count - 1))

# --- Test Case ---
# if __name__ == "__main__":
#     N = 3
#     C = 2
#     F = [1, 2, 3]
    
#     print(f"Output: {get_crystal_subset_xor_sum(N, C, F)}")
#     # Output: 6

def run_crystal_tests():
    tests = [
        {"name": "No Matches", "N": 3, "C": 4, "F": [1, 2, 3], "expected": 0},
        {"name": "Single Match", "N": 3, "C": 2, "F": [1, 2, 4], "expected": 2},
        {"name": "All Match", "N": 3, "C": 7, "F": [1, 2, 3], "expected": 12},
        {"name": "Zero Band Mask", "N": 3, "C": 0, "F": [1, 2, 3], "expected": 0},
        {"name": "Array with Zeros", "N": 3, "C": 2, "F": [0, 2, 3], "expected": 6},
        {"name": "Exam Test Case 1", "N":3, "C":2, "F":[1,2,3], "expected":6},
        {"name": "Exam Test Case 2", "N":3, "C":6, "F":[1,5,5], "expected":10}
    ]
    
    for t in tests:
        result = get_crystal_subset_xor_sum(t["N"], t["C"], t["F"])
        status = "✅ PASS" if result == t["expected"] else f"❌ FAIL (Got {result}, Expected {t['expected']})"
        print(f"{t['name'].ljust(20)}: {status}")

if __name__ == "__main__":
    run_crystal_tests()