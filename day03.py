data = open('day03input').read().split('\n')[:-2]

def priorityval(x):
    if x.isupper():
        return(ord(x) - 38)
    else:
        return(ord(x) - 96)

rsacks = [(rsack[:len(rsack)//2], rsack[len(rsack)//2:]) for rsack in data]
dups = []
for rsack in rsacks:
    rdups = []
    for item in rsack[0]:
        for item2 in rsack[1]:
            if item == item2:
                rdups.append(priorityval(item))
    dups.append(list(set(rdups)))

groups = [[i, data[data.index(i)+1], data[data.index(i) + 2]] for i in data[::3]]

dupsum = []
for group in groups:
    rdups = []
    gdups = []
    for item in group[0]:
        for item2 in group[1]:
            if item == item2:
                rdups.append(item)
    for item3 in group[2]:        
        for dup in list(set(rdups)):
            if dup == item3:
                gdups.append(dup)
    dupsum.append(list(set(gdups)))

dupsum = sum(dupsum,[])
print(sum([priorityval(i) for i in dupsum]))
print(sum(sum(dups,[]))) 
