def palindrome_check(word):
    """
       Checks if given word is a palindrome
    """
    check = word == word[::-1]
    return check
    


print(palindrome_check("kajak"))
