def palindrome_check(word):
    """
       Checks if given word is a palindrome
    """
    check = (word == word[::-1])
    result = (f"Given word is a palindrome: {check}")
    return result
    


print(palindrome_check("kajak"))
