divisible_number = [num for num in range(1,1001) if any(num%digit == 0 for digit in range(2,10))]
print(divisible_number)


def divisible_num():
    for num in range(1,1001):
        for digit in range(2,10):
            if num % digit == 0:
                print(num)






print(divisible_num())