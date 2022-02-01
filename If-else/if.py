import sys

# if

name = input ( "Enter Name:" )
if name == "Pratiksha" :
    print ( "Hi", name )
print ( "----------------------------------" )

# if-else

name = input ( "Enter Name:" )
if name == "Hi" :
    print ( "Hi Pratiksha" )
else :
    print ( "Bye" )

print ( "----------------------------------------------" )
a = input ( "Enter no:" )
b = input ( "enter no:" )

if a > b :
    print ( "a is greater than b" )
else :
    print ( "a is less than b" )

print ( "----------------------------------------------" )
# if-elif-else

brand = input ( "Enter your favourite Brand:" )
if brand == "max" :
    print ( "It is cloth brand" )
elif brand == "kfc" :
    print ( "it is eating brand" )
elif brand == "ball" :
    print ( "it is gameing brand" )

else :
    print ( "not recommended" )

sys.exit ( 0 )
