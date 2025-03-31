# Define two sets with different elements
set1 = {20, 30, 60}
set2 = {10, 20, 30, 40, 50, 60}

# Union of sets
set3 = set1 | set2
print(f"length of union of set1 and set2 is: {len(set3)}")

# Intersection of sets
set4 = set1 & set2
print(f"Intersection of set1 and set2 are: {set4}")

# Symmetric difference
set5 = set1 ^ set2
print(f"symmetric difference between set1 and set2 are:{set5}")

# Add element to set1
set1.add(40)
print(set1)

# Remove element from set2
set2.remove(20)
print(set2)