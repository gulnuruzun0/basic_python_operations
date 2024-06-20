
'''
Gülnur Uzun, Alper Tanrıkulu

Q1
Write a Python script that calculates and prints the sum and average of the 
digits in the given string, my_str. (Hint: You can use isdigit() function to 
check each character of the string.)
'''

my_str = 'TR29abcdqxw10Casd1923yhdf23askdjl04ajdfguj19akflk05ssfıj30lkhu08akdf'

digit_count = 0
digit_sum = 0

#We save integer value char.isdigit() == TRUE
#isdigit() checked the my_str string

for char in my_str:
    if char.isdigit(): #If the character is a digit, convert it to an integer and add it to the sum
        digit_count += 1
        digit_sum += int(char)
        
digit_average = digit_sum/digit_count   
print (digit_sum)
print(digit_average)

