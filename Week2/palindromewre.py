

      

def pal():      
  good = "mom"
  goodphrase = "A man, a plan, a canal -- Panama!"
  bad = "failure"
  badphrase = "banner just look"
  
  Entry1 = Palindrome(good)
  Entry2 = Palindrome(goodphrase)
  Entry3 = Palindrome(bad)
  Entry4 = Palindrome(badphrase)
  

  print(f"{good} is {Entry1._is_a_palindrome}")
  print(f"{bad} is {Entry3._is_a_palindrome}")
  print(f"{goodphrase} is {Entry2._is_a_palindrome}")
  print(f"{badphrase} is {Entry4._is_a_palindrome}")

if __name__ == "__main__":
    pal()