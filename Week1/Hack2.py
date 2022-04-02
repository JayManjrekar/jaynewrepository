InfoDB = []
movie1 = {"title":"Spiderman",
          "price":"8",
          "actors":["tom holland","zendaya","andrew garfield","toby maguire"]}
movie2 = {"title":"Thor",
          "price":"10",
          "actors":["chris hemsworth","tom hiddleston","Natalie Portman","anthony hopkins"]}
movie3 = {"title":"Iron Man",
          "price":"12",
          "actors":["robert downey jr","Gwen Palthrow","Jeff Bridges","Elon Musk"]}
InfoDB.append(movie1)
InfoDB.append(movie2)
InfoDB.append(movie3)
print(InfoDB)

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  
    print("Recursive loop")
    recursive_loop(0)
def for_loop():
  #for i in range(0,len(InfoDB)):
  #  print(InfoDB[i])

  for i in InfoDB:
    print (i)
def while_loop(n):
  while(n< len(InfoDB)):
    print(InfoDB[n]);
    n += 1

def recursive_loop(n):
  if n == len(InfoDB):
    return
  else:
    print(InfoDB[n])
    n+=1
    recursive_loop(n)
  
  


if __name__ == "__main__":
    tester()