def Fibonacci(n):
  if( n == 0):
    return [0];
  elif n == 1 :
    return [0, 1]
  else:
    tempList = Fibonacci(n-1)
    tempList.append(tempList[-1] + tempList[-2])
    return tempList

def printfibo():
  print(Fibonacci(12))

if __name__ == "__main__":
    printfibo()