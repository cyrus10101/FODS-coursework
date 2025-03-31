# Initialize three dictionaries with key-value pairs
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

# Merge all three dictionaries into a single dictionary using dictionary unpacking
nums = {**dict1, **dict2, **dict3}
print(nums)

# Add a new key-value pair to the dictionary
nums[7] = 70
print(nums)

# Update the value for key 3 to 80
nums.update({3: 80})
print(nums)

# Get the third key from the dictionary and remove its corresponding key-value pair
third = list(nums.keys())
nums.pop(third[2])
print(nums)

# Calculate the sum of all keys and values in the dictionary
kys = list(nums.keys())
val = list(nums.values())
value_sum = sum(kys) + sum(val)
print(f'sum of all items: {value_sum}')

# Calculate the product of all key-value pairs in the dictionary
for i, j in nums.items():
    product = i * j
print(f"Product of all items of dicionary is: {product}")

# Find and print the maximum and minimum values in the dictionary
max_val = max(nums.values())
min_val = min(nums.values())
print(f"Maximum value: {max_val}\nMinimun Value: {min_val}")