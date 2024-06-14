# s = "A man, a plan, a canal: Panama"
# s = ".,"
s = "0p"
def isValid(s:str):
    s = s.lower()
    start = 0
    end = len(s) - 1

    while start < end:
        while start < end and  not s[start].isalnum():
            start += 1
        while start < end and not s[end].isalnum():
            end -= 1

        if s[start] != s[end]:
            return False
        
        if s[start] == s[end]:
            start += 1
            end -= 1
    return True
print(isValid(s))