# cannot remember vividly
def get_minimum_plague_shield_cost(data: list[int]) -> int:
    activation_cost = data[0]
    shields = data[1:]
    
    if not shields:
        return 0
        
    def calculate_cost(shield_list):
        if not shield_list:
            return 0
        # Example logic: activation cost multiplied by max shield strength plus count
        max_shield = max(shield_list)
        return activation_cost * (max_shield + len(shield_list))

    # Option 1: Without decoy (using all shields)
    cost_without_decoy = calculate_cost(shields)
    
    # Option 2: With decoy (removing the maximum shield value)
    max_val = max(shields)
    # Create a new list removing only one instance of the maximum value (the decoy target)
    decoy_shields = list(shields)
    decoy_shields.remove(max_val)
    
    cost_with_decoy = calculate_cost(decoy_shields) if decoy_shields else 0
    
    return min(cost_without_decoy, cost_with_decoy)

# --- Test Cases ---
if __name__ == "__main__":
    # Example 1 mapping: activation_cost = 5, shields = [5, 8, 7, 1, 9, 6]
    ex1 = [5, 5, 8, 7, 1, 9, 6]
    print(f"Example 1 Output: {get_minimum_plague_shield_cost(ex1)}")
    
    # Example 2 mapping: activation_cost = 4, shields = [10, 10, 10, 10]
    ex2 = [4, 10, 10, 10, 10]
    print(f"Example 2 Output: {get_minimum_plague_shield_cost(ex2)}")