import portion as P

p1 = 0
p2 = 0

for d in open('day04input').read().split('\n')[:-2]:
    f, s= d.split(',')[0].split('-'),d.split(',')[1].split('-')
    int1,int2 = P.closed(int(f[0]),int(f[1])), P.closed(int(s[0]), int(s[1]))
    if (int1  in int2) | (int2 in int1):
        p1 += 1
    if (int1.overlaps(int2)) | int2.overlaps(int1) :
        p2 += 1

print(p1,p2)