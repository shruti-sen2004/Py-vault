def max_flag_pieces(strips: list[int], L: int, K: int) -> int:
    pieces = 0
    exact_multiples = []
    extra_pieces = 0

    for s in strips:
        if s < L:
            continue
        elif s == L:
            pieces += 1  # Exact length needs 0 cuts
        elif s % L == 0:
            exact_multiples.append(s // L)
        else:
            extra_pieces += s // L  # Non-multiples cost 1 cut per piece

    # Finish smaller exact multiples first to get the last-cut bonus piece sooner
    exact_multiples.sort()

    for m in exact_multiples:
        cuts_needed = m - 1
        if K >= cuts_needed:
            K -= cuts_needed
            pieces += m
        else:
            pieces += K  # Partial cuts yield 1 piece per cut
            K = 0
            break

    # Spend any remaining cuts on non-multiple strips
    if K > 0:
        pieces += min(K, extra_pieces)

    return pieces


if __name__ == "__main__":
    test_cases = [
        # (strips, L, K, expected_output, description)
        ([5], 5, 0, 1, "Example 1: Exact length, 0 cuts"),
        ([10, 7], 3, 5, 5, "Example 2: Non-multiples using all cuts"),
        ([9, 6], 3, 2, 3, "Example 3: Exact multiples with limited cuts"),
        ([9, 6], 3, 1, 2, "Greedy order matters (pick 6 over 9)"),
        ([1, 2, 4], 5, 10, 0, "All strips shorter than L"),
        ([5, 10, 5, 3], 5, 0, 2, "Zero cuts allowed with mixed strips"),
        ([6, 7], 3, 100, 4, "More cuts than total available pieces"),
        ([4, 8, 12, 10], 4, 3, 6, "Mix of exact, multiples, and non-multiples"),
        ([], 3, 5, 0, "Empty strips list"),
    ]

    for i, (strips, L, K, expected, desc) in enumerate(test_cases, 1):
        result = max_flag_pieces(strips, L, K)
        assert result == expected, f"Test {i} failed: got {result}, expected {expected}"
        print(f"Test {i} PASSED ({desc}): output = {result}")