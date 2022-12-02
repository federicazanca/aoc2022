file = open("input.txt")
elves = []
elf = 0
for line in file:
        if line != "\n" :
            elf += int(line)
        else:
            elves.append(elf)
            elf = 0           
result1 = max(elves)
print(result1)
elves2 = sorted(elves)
result2=elves2[-1]+elves2[-2]+elves2[-3]
print(result2)
