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
liste = Hello_World('ach so geht das', "a")
f = Flicken(liste, "a")
print(f)
