import ast

def compare(left,right,i):
    print(left,right)
    left.reverse()
    right.reverse()

    global decision
    decision = False

    while left and right and not(decision):
        l,r = left.pop(), right.pop()
        print(l,r)
        if type(l) == int and type(r) == int:
            if l > r : 
                decision = True
                return
            elif l < r: 
                decision = True
                print('added for <',i+1)
                tr.append(i+1)
                return
        elif type(l) == list and type(r) == list:
            compare(l,r,i)
        else:
            if type(l) == int:
                compare([l],r,i)
            else:
                compare(l,[r],i)
    else:
        if decision: return
        elif left == [] and right == []: return
        elif left == []:
            decision = True
            print('added for emtpy',i+1)
            tr.append(i+1)
        else:
            decision = True


inp = [pair.split('\n') for pair in open('input/13').read().strip().split('\n\n')]
tr = []



for i,pair in enumerate(inp):
    left = ast.literal_eval(pair[0])
    right = ast.literal_eval(pair[1])

    compare(left,right,i)

print(sum(tr))
