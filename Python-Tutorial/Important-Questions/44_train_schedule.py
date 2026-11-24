# Code Force #340 Two-Machine Flow Shop Scheduling Problem (Johnson’s Rule)
def get_minimum_travel_time(N: int, A: list[int], B: list[int]) -> int:
    # Helper function to calculate the time using Johnson's Rule
    def get_makespan(a_times: list[int], b_times: list[int]) -> int:
        jobs = []
        for i in range(N):
            jobs.append((a_times[i], b_times[i], i))
            
        # Group 1: Station 1 time < Station 2 time
        group1 = [job for job in jobs if job[0] < job[1]]
        # Group 2: Station 1 time >= Station 2 time
        group2 = [job for job in jobs if job[0] >= job[1]]
        
        # Sort Group 1 by Station 1 time (ascending)
        group1.sort(key=lambda x: x[0])
        # Sort Group 2 by Station 2 time (descending)
        group2.sort(key=lambda x: x[1], reverse=True)
        
        optimal_order = group1 + group2
        
        t1 = 0 # End time at Station 1
        t2 = 0 # End time at Station 2
        
        for a, b, i in optimal_order:
            t1 += a
            t2 = max(t2, t1) + b
            
        return t2

    min_total_time = float('inf')
    
    # 1. Try using the express pass to skip Station 1 for each unit
    for i in range(N):
        original_time = A[i]
        A[i] = 0
        min_total_time = min(min_total_time, get_makespan(A, B))
        A[i] = original_time # Backtrack
        
    # 2. Try using the express pass to skip Station 2 for each unit
    for i in range(N):
        original_time = B[i]
        B[i] = 0
        min_total_time = min(min_total_time, get_makespan(A, B))
        B[i] = original_time # Backtrack
        
    return min_total_time

# --- Test Cases ---
# if __name__ == "__main__":
#     # Example 1
#     N1 = 3
#     A1 = [5, 2, 3]
#     B1 = [1, 10, 5]
#     print(f"Example 1 Output: {get_minimum_travel_time(N1, A1, B1)}") 
#     # Output: 10 (Matches exactly by skipping 10 at Station 2)

#     # Example 2
#     N2 = 4
#     A2 = [2, 2, 2]
#     B2 = [10, 10, 10]
#     print(f"Example 2 Output: {get_minimum_travel_time(N2, A2, B2)}") 
#     # Output: 22

def run_tests():
    tests = [
        {"name": "N=1", "N": 1, "A": [10], "B": [20], "expected": 10},
        {"name": "Station 1 Bottleneck", "N": 3, "A": [100, 100, 100], "B": [1, 1, 1], "expected": 201},
        {"name": "Station 2 Bottleneck", "N": 3, "A": [1, 1, 1], "B": [100, 100, 100], "expected": 201},
        {"name": "Natural Zeros", "N": 3, "A": [0, 5, 10], "B": [10, 0, 5], "expected": 15},
        {"name": "Symmetrical", "N": 4, "A": [10, 10, 10, 10], "B": [10, 10, 10, 10], "expected": 40},
        {"name": "Hidden Critical Path", "N": 3, "A": [10, 1, 10], "B": [1, 20, 1], "expected": 21}, 
        {"name": "Exam Case 1", "N": 3, "A": [5, 2, 3], "B": [1, 10, 5], "expected": 10},
        {"name": "Exam Case 2", "N": 3, "A": [2, 2, 2], "B": [10, 10, 10], "expected": 22}
    ]
    
    for t in tests:
        result = get_minimum_travel_time(t["N"], t["A"][:], t["B"][:])
        status = "✅ PASS" if result == t["expected"] else f"❌ FAIL (Got {result}, Expected {t['expected']})"
        print(f"{t['name'].ljust(25)}: {status}")

if __name__ == "__main__":
    run_tests()