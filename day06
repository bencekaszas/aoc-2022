inp =  open('input/day06input').read().strip()

def get_marker(str, length):
    for i in range(length,len(str)):
        if len(set(str[i-length:i])) == length:
            print(i)
            break

get_marker(inp,4)
get_marker(inp,14)