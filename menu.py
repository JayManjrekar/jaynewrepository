from Week1.Fibonacci import printfibo
from Week1.Hack1 import printinfo
from Week1.Hack2 import tester

from Week2.Factorial import printfac
from Week2.Mathfunction import mfunc
from Week2.PalindromeEC import pp
from Week2.palindromewre import pal




week1 = {
  1: {
    "display": "Fibonacci",
    "exec": printfibo,
    "type": "func"
  },
  2: {
    "display": "InfoDB",
    "exec": printinfo,
    "type": "func"
  },
  3: {
    "display": "Loops",
    "exec": tester,
    "type": "func"
  },  
  0: {
    "display": "Quit",
    "exec": quit,
    "type": "func"
  }
}
week2 = {
    1: {
        "display":"Factorial",
        "exec":printfac,
        "type":"func"
    },
    2: {
        "display":"LCM",
        "exec":mfunc,
        "type":"func"
    },
    3: {
        "display":"Palindrome",
        "exec":pp,
        "type":"func"
    },
    4: {
        "display":"Palindrome with re",
        "exec":pal,
        "type":"func"
    },
    0: {
        "display":"Quit",
        "exec":quit,
        "type":"func"
    }
}

mainMenu = {
    1: {
        "display": "InfoDB and Fibonacci",
        "exec": week1,
        "type": "submenu"
    },
    2: {
        "display": "Math Functions",
        "exec": week2,
        "type": "submenu"
    },

    0: {
        "display": "Quit",
        "exec":quit,
        "type":"func"
    }
}


def buildMenu(menu):
    for key,value in menu.items(): 
        display = value["display"]
        print(f"{key} ------ {display}") # each menu item is printed
    print("What is your choice? (enter the number value) ") # user input promp

def presentMenu(menu):
    buildMenu(menu) #print out menu and take input
    choice = int(input())
    while choice not in menu: # ensure that choice is valid
        choice = int(input("Please elect a valid item. "))
    if (choice) in menu:
        if menu[choice]["type"] == "func": #determine whether recursion is needed
            menu[choice]["exec"]() #run function

        else:
            presentMenu(menu[choice]["exec"]) #display submenu

if __name__ == "__main__":
  while True:
    print('\033[2J')  # Clear screen
    presentMenu(mainMenu)
    



