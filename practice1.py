m_code = "MP 34"
s_code = ["AB","CD","EF"]
count = 0
for i in s_code:
    for i1 in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                for p in range(0,10):
                    print(f"{m_code} {i} {i1}{j}{k}{p}")
                    count += 1
print(count)