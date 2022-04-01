# palindrome with re

import re


class Palindrome:
    def __init__(self, candidate):
      self._candidate = candidate 
      self._length = len(candidate)   
      self._is_a_palindrome = False 
    
      self._az09 = re.sub(r'[^a-zA-Z0-9]', '', self._candidate)  
 
      self._analysis = []  
      self._tests = 0 
  
      self.__call__()  

    def __call__(self):
      c = self._az09
      tests = int(len(c) / 2)
    
      for i in range(0, tests):
          front = c[i];
          back = c[len(c) - i - 1]
          if front.lower() == back.lower():
              self.logger(front, back, True)
              self._tests += 1
          else:
              self.logger(front, back, False)
              return
      self._is_a_palindrome = True
      return

    def logger(self, front, back, result):
      self._analysis.append({"test": self._tests, "front": front, "back": back, "result": result})

      

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