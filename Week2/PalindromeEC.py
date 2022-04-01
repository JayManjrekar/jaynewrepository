class palindrome:
  def __init__ (self,forward):
    self.forward=forward

  def mypalindrome(self):
    tempforward =""
    for i in self.forward:
      if(i.isalpha()):
        tempforward += i

    
    backwardsWord =""
    for i in range(len(tempforward)-1,-1, -1):
      backwardsWord += tempforward[i]

    if (tempforward==backwardsWord):
      print(self.forward + " is a palindrome")
    else:
      print(self.forward + " not a palindrome")

def pp():
  p = palindrome("saippuakivikauppias")
  p.mypalindrome()
  
  p1 = palindrome("failure")
  p1.mypalindrome()
  
  p2 = palindrome("A man, a plan, a canal -- Panama!")
  p2.mypalindrome()

if __name__ == "__main__":
    pp()