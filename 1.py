# Calculator v2

from colorama import init
from colorama import Fore, Back, Style

init()

test = 1
test2 = 'Calc' 

print( Fore.BLACK )
print( Back.YELLOW )
print ( 'Hi my name is ' + test2 + '!' )
print ( "I do calculations in less than " + str (test) + ' second!' )

print( Back.GREEN )
name = input ( "What's your name dude? " )
age = print ( "I am a calculator faster than any leather bag on this planet! " )

print( Back.RED )
print ( 'What`s going on ' + name + '?' )

print( Back.GREEN )
what = input( 'What do we do (+,-): ' ) 

print( Back.RED )
a = float ( input( 'Enter the first number: ') )
b = float ( input( 'Enter the second number: ') )  

print( Back.YELLOW )
if what == "+":
	c = a + b
	print( "Result: " + str(c) )

elif what == "-":
	c = a - b
	print( "Result: " + str(c) )
else:
	print( "You made up something! Do not do this anymore!" )

input()
