import pickle
dct = {111: "Eric", 112: "Kyle", 113: "Butters"}
with open("test.txt","wb") as file:
    pickle.dump(dct,file)

with open("test.txt","rb") as file:
    dct2 = pickle.load(file)
print(dct2[112])