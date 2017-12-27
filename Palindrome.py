def ispalindrome(s):
    if len(s) < 2:
        return True
    if s[0]== s[len(s)-1]:
        return ispalindrome(s[1:len(s)-1])
    else:
        return False

s = raw_input()
print ispalindrome(s)
