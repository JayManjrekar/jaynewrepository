class factorial:
  def __init__(self, n):
    self.n = n 

  def __call__(self):
    ans = self.fact(self.n)
    print(ans)
  
  def fact(self, n):
    if(n == 1):
      return n
    else:
      return n * self.fact(n-1)

f = factorial(10)
f()

