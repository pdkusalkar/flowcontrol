'''#print no 1 to 10

x=1
while x<=10:
    print(x)
    x=x+1

# sum of no

n = int ( input ( "Enter number:" ) )
sum = 0
i = 1
while i <= n :
    sum = sum + 1
    i = i + 1
    print ( "the sum of 1st", n, "number is:", sum )


name = ""
while name != "durga" :
    name = input ( "enter name:" )
print ( "thanks for confirmation" )


i = 0;
while True :
    i = i + 1;
    print ( "hello", i )


for i in range(4):
    for j in range(4):
        print("i=",i,"j=",j)


n = int ( input ( "enter no of rows:" ) )
for i in range ( 1, n + 1 ) :
    for j in range ( 1, i + 1 ) :
        print ( "*", end="" )
    print ()
    '''

n = int ( input ( "enter no row:" ) )
for i in range ( 1, n + 1 ) :
    print ( "*" * i )

n = int ( input ( "enter no row:" ) )
for i in range ( 1, n + 1 ) :
    print ( "" * (n - i), end="" )
print ( "*" * i )
