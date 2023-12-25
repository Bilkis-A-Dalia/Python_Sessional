def separate_even_odd(numbers):
    even = []
    odd = []
    # even = 0
    # odd = 0
    for num in numbers:
        if num%2 == 0:
            even.append(num)
            # even +=1
        else:
            odd.append(num)
            # odd +=1
    return even,odd

numbers = (1,2,3,4,5,6,7,8,9)
even_nums,odd_nums = separate_even_odd(numbers)
print('Even numbers are: ',even_nums)
print('Odd nums are: ',odd_nums)