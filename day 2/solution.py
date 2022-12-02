file = open("input.txt")

def convert(val):
        if val == "A" or val == "X":
            val = 1
        if val == "B" or val == "Y":
            val = 2
        if val == "C" or val == "Z":
            val = 3
        return val
 
def Winner(elf,me):
    values =[1,2,3,1,2,3]
    if elf == me:
        win = 3 #draw
    for v in values:
        i=values.index(v)
        if elf == v:
            if me == values[i+1]:
                win = 6 #win
            if me == values[i+2]:
                win = 0 #loose
    return win
        

tot = 0

for line in file:
    elf = line[0]
    me = line [2]
    elf = convert(elf)
    me = convert(me)
    win = Winner(elf, me)
    score = me + win
    tot = tot + score
print(tot)

