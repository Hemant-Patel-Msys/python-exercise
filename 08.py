# 8. Take the input marks from user using input() function and find out the grade of the students. Note
# the grading will be in this manner – (100 – 91) – A1, (90-81) – A2, (80-71) – B1, (70-61) – B2, (60-
# 51) – C1 (50-40) – C2 and less than 40 students will ‘Fail’. Also make sure user should input the
# marks in the range 0<=marks<=100, if user will input some other marks in should print invalid
# marks.


num = int(input("ENter the marks:- "))
try:
    if num in range(0,101):
        if num in range(91,101):
            print("A1")
        elif num in range(81,91):
            print("A2")
        elif num in range(71,81):
            print("B1")
        elif num in range(61,71):
            print("B2")
        elif num in range(51,61):
            print("C1")
        elif num in range(41,51):
            print("C2")
        else:
            print("FAIL")
    else:
        print("please provide valid input")

#except:
   # print("Please provide the valid input")
finally:
    print("Thank You!")