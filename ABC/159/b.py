def is_palindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

s = input()
n = len(s)
if is_palindrome(s) and is_palindrome(s[:n // 2]) and is_palindrome(s[-(n // 2):]):
    print('Yes')
else:
    print('No')
