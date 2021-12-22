size = input()
w = int(size.split()[0])
l = int(size.split()[1])

form=".|."

for i in range(1,w+1):
    #top lines
    if i < ((w+1)/2) :
        print((form*((2*i)-1)).center(l,"-"))
    # belt line
    if i == ((w+1)/2):
        print("WELCOME".center(l,"-"))
    #down lines
    if i > ((w+1)/2) :
        print((form*(2*(w-i)+1)).center(l,"-"))
