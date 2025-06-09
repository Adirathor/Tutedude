def factorial():
    n=int(input ("Enter a number: "))
    def fact(n):
        if n < 2:
            return 1
        else:
            return n*fact (n-1)
    result=fact (n)
    print ("factorial of", n , "is: ", result)
print ("Thank you for using tha program. ")
factorial ()