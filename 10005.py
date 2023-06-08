inputt = "my name is kartik"

def func(st):

    st = st.split(" ")

    longest = 0

    for i in st:
        if len(i)>longest:
            longest = len(i)

    for i in range(longest):
        result = ""
        for j in range(len(st)):
            try:
                result += st[j][i]
            except IndexError:
                pass
        print(result, end=" ")

func(inputt)