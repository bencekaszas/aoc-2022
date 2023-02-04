import ast
from copy import deepcopy

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



def bubbleSort(arr):
    n = len(arr)
    swapped = False

    for i in range(n-1):
        for j in range(0, n-i-1):
 
            left = deepcopy(arr[j])
            right = deepcopy(arr[j+1])
            compare(left,right,j)
            if tr[-1] != j+1:
                print('SWAP')
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return

inp = [ast.literal_eval(line) for line in open('input/13').read().strip().replace('\n\n','\n').split('\n')]
inp.append([[2]])
inp.append([[6]])
tr = [1000]



bubbleSort(inp)
for i,line in enumerate(inp):
    if line == [[2]]:
        print(i+1)
    elif line == [[6]]:
        print(i+1)
#print(sum(tr))
