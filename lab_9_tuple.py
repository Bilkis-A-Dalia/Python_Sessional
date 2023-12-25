# creates
fruits_basket = ('apple','banana','cherry','date','elderberry')
print(fruits_basket)

# length of tuple
print(len(fruits_basket))

# 3rd element of tuple
print(fruits_basket[2])

# index of date
date_index = fruits_basket.index('date')
print(date_index)

# check if cherry is in the tuple print yes if not print no
if 'cherry' in fruits_basket:
    print('Yes')
else:
    print('No')