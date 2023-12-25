# create set
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1, set2)

# intersection of sets
# intersection() method
intersection_set = set1.intersection(set2)
print(intersection_set)
#  &method
intersection_set = set1 & set2
print(intersection_set)


# union sets
set = set1.union(set2)
print(set)

# difference
set = set1.difference(set2)
print(set)
set = set2.difference(set1)
print(set)

# add 6 in set1
set1.add(6)
print(set1)

# remove 4 from se12
set2.remove(4)
print(set2)