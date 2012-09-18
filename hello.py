name = raw_input("What is your name? ")

print "Hello world"
print "line 2!"
print name

fib = lambda n:reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]

fib_val = raw_input("What Fibonacci number would you like to compute? ")
print fib(int(fib_val))
