# same word if count from forword to backward and backward to forword

word = input('Enter a word: \n')
# string = 'maam'
half = int(len(word)/2)
first_str = word[:half]
second_str = word[half:]

if first_str == second_str[::-1]:
    print(word,'string is palindrome')
else:
    print(word,'sting in not palindrome')
