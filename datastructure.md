{% include nav.html %}

## Week 3

### Console Colors
#### install colorama
```
$ pip install colorama
```
#### imports
```
import colorama
from colorama import Fore, Back, Style
```
#### Set the color semi-permanently
```
print(Fore.CYAN)
print("Text will continue to be cyan")
print("until it is reset or changed")
print(Style.RESET_ALL)
```
#### Colorize a single line and then reset
```
print(Fore.RED + 'You can colorize a single line.' + Style.RESET_ALL)
```
#### Colorize a single word in the output
```
print('Or a single ' + Back.GREEN + 'words' + Style.RESET_ALL + ' can be highlighted')
```

#### Combine foreground and background color
```
print(Fore.BLUE + Back.WHITE)
print('Foreground, background, and styles can be combined')
print("==========            ")
```

## Week 2 

### Exmaples and Code Snippets

#### self 
``self`` as it suggests, refers to itself- the object which has called the method. That is, if you have N objects calling the method, then ```self.a``` will refer to a separate instance of the variable for each of the N objects. Imagine N copies of the variable ``a`` for each object


#### __init__
``__init__`` is what is called as a constructor in other OOP languages such as C++/Java. The basic idea is that it is a special method which is automatically called when an object of that Class is created

#### class Example
```
class receipt():
    def __init__(self,apples,figs,dates):
        self.apples = apples
        self.figs = figs
        self.dates = dates
        self.bill = apples + figs + dates
        print ("Buy",self.apples,"apples", self.figs,"figs 
                and",self.dates,"dates. 
                Total bill is",self.receipt," pieces of fruit")
                
purchase = receipt(5,6,7)
```
result
```
> Buy 5 apples 6 figs and 7 dates. Total fruitty bill is 18  pieces of fruit
```


## Hack 1
<div class="row justify-content-center" style="margin: 2%;">
    <iframe height="1000px" width="700px" src="https://replit.com/@JayManjrekar/Hack1?lite=true#main.py"></iframe>
</div>

## Hack 2

<div class="row justify-content-center" style="margin: 2%;">
    <iframe height="1000px" width="700px" src="https://replit.com/@JayManjrekar/Hack2?lite=true#main.py"></iframe>
</div>

## Fibonacci

<div class="row justify-content-center" style="margin: 2%;">
    <iframe height="1000px" width="700px" src="https://replit.com/@JayManjrekar/Fibonacci#main.py"></iframe>
</div>

## Big File With Everything

<div class="row justify-content-center" style="margin: 2%;">
    <iframe height="1000px" width="700px" src="https://replit.com/@JayManjrekar/Jaysactualrepo-1?lite=true#.replit"></iframe>
</div>
