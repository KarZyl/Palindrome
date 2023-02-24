
def palindrome_check(word):
    """
       Checks if given word is a palindrome
    """
    position_half_word = int((len(word)-len(word) % 2) / 2)
        
    for a in range(0,position_half_word):
      if word[a] == word[-(a+1)]:
        pass
        check = ""
      else:
        check = " not"        
        break
    print (f"Given word is{check} a palindrome")
    
      
    
  



