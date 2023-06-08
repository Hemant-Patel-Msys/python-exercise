def fizzBuzz(n):
    # Write your code here
    for i in range(1,n):
        if(i%3==0 and i%5==0):
            print("FizzBuzz")
        #checking that number is divisible by 3
        elif(i%3 == 0):
            print("Fizz")
        #checking that number is divisible by 5
        elif(i%5 == 0):
            print("Buzz")
        #And if not divisible by either of them print num as it is
        else:
            print(i)

print(fizzBuzz(16))