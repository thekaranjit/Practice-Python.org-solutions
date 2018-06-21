'''
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''

input_txt = input("PLease input a word to check if it is a Palindrome: ")


new_str = input_txt[::-1]

if input_txt == new_str:
    print('Entered text ', input_txt ,  ' is a Palindrome')
    
else:
    print('Entered text ',  input_txt ,  ' is not a Palindrome')
    