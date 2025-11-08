from collections import Counter

def max_pairs(shoes):
    shoe_counts = Counter(shoes) # stores frequency of each element
    total_pairs = 0

    print(shoe_counts)

    unique_size = set(shoe[:-1] for shoe in shoes) # extracts size i.e. 7 from 7l 

    for size in unique_size:
        left = size + "L"
        right = size +"R"

        count_l = shoe_counts[left]
        count_r = shoe_counts[right]

        pair = min(count_l, count_r)
        total_pairs += pair
    return total_pairs

s_collection_1 = ["7L", "10R", "7R", "7L", "10L", "8R", "7R"]
s_collection_2 = ["5L", "5L", "5R", "6R"]
print(max_pairs(s_collection_2))