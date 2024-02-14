word = ''
def is_palindrome(ch):
    global word
    word += ch
    return word[::-1] == word
    
s = 'ababa'
for i in s:
    print(is_palindrome(i),word)
    