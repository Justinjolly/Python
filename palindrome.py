x = input("Enter a word: ")
y = x[::-1]
print('reverse: ', y)
if x == y:
    print('It is a palindrome')
else:
    print('It not a palindrome')