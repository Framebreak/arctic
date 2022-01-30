from random import randrange


def Hello_World(irgentwas:str, seperator:chr):
    x = irgentwas.split(seperator)
    print(x)
    return x

def Flicken(input:list, seperator:chr):
    o = ""
    for i in range(len(input)-1):
        o = o + str(input[i]) + seperator
    o+= input[len(input)-1]
    return o

def DndStats():
    n = 0
    while n <6:
        firstStat = [0,0,0,0]
        i = 0
        while i < 4:
            firstStat[i] = randrange(1, 6)

            i+= 1
        stat = (sorted(firstStat, reverse=True))
        print(stat)
        result = stat[0] + stat[1] + stat[2]
        print(result)
        n+=1

liste = Hello_World('ach so geht das', "a")
f = Flicken(liste, "a")
print(f)
DndStats()