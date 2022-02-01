'''# hello print 10 time
for x in range ( 10 ) :
    print ( "Hello" )
print ( "--------------------------------------------------" )
# print 0 to 10
for x in range ( 11 ) :
    print ( x )

print ( "--------------------------------------------------" )

# print  odd number 0 to 20

for x in range ( 21 ) :
    if (x % 2 != 0) :
        print ( x )

print ( "--------------------------------------------------" )
# print even no

for x in range ( 51 ) :
    if (x % 2 == 0) :
        print ( x )

print ( "--------------------------------------------------" )
# descending order

for x in range ( 10, 0, -1 ) :
    print ( x )

print ( "--------------------------------------------------" )'''

list = eval ( input ( "Enter the list:" ) )
sum = 0

for x in list :
    sum = sum + x;
print ( "the sum=",sum )
