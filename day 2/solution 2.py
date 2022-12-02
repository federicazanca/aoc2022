file = open("input.txt")

def convert(val):
        if val == "A":
            val = 1
        if val == "B":
            val = 2
        if val == "C":
            val = 3
        return val
    
def convertwin(win):
        if win == "X":
            win = 0
        if win == "Y":
            win = 3
        if win == "Z":
            win = 6
        return win    
    
    
def myvalue(elf,win):
    values =[1,2,3,1,2,3]
    if win == "Y": #draw
        me = elf
    for v in values:
        i=values.index(v)
        if elf == v:
            if win == "X": #lose 
                me = values[i+2]
            if win =="Z": #win
                me = values[i+1]
    return me

tot = 0

for line in file:
    elf = line[0]
    win = line [2]
    elf = convert(elf)
    me = myvalue(elf, win)
    win = convertwin(win)
    score = me + win
    print(score)
    tot = tot + score
print(tot)

