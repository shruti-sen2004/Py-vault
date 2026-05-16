def add(a, b):
   while b != 0:
       carry = (a & b) # Calculate carry
       a = a ^ b # Add without carry
       b = carry << 1# Update carry
   return a
# Example usage
result = add(5, 3)
print(result) # Output: 8