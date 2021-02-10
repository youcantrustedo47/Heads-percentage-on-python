'''
HeadsPercentage

by trustnoedo

'''

from random import randint

def ncoins(n):
    lst = []
    heads = "H"
    tails = "T"
    for i in range(n):
        a = randint(1, 2)
        if a == 1:
            lst.append(heads)
        else:
            lst.append(tails)
    num = lst.count("H")
    prc = int((num / x) * 100)
    return prc


x = int(input("Insert the number of coin flips you wanna perform: "))
percentage = ncoins(x)

print()
print("--------------------------------------")
print()
print("We've reached a Heads' percentage of: "
      "" + str(percentage) + "%")
print()
print("--------------------------------------")
print()
