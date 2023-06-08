st = "Hemant"

def func(st):
    vowels = ["a", "e", "i", "o", "u"]
    vowels_present = ""
    output = ""

    for i in st:
        if i in vowels:
            vowels_present += i

    counter = 1
    for i in range(len(st)):
        if st[i] in vowels:
            output += vowels_present[-counter]
            counter += 1
        else:
            output += st[i]

    print(output)

func(st)