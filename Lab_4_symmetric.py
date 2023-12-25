# both half of string will be same

string = 'dada'
half = int(len(string)/2)
first_str = string[:half]
second_str = string[half:]

if first_str == second_str:
    print(string,'string is symmetric')
else:
    print(string,'sting in not symmetric')