### Set .add()
d = int(input())
s = set(input() for i in range(d))
print(len(s))

### Set discard(), pop(), remove()
n = int(input())
s = set(map(int, input().split()))
num_cmds = int(input())

for x in range(num_cmds):
    cmd = list(input().strip().split(' '))
    if cmd[0] == "pop":
        s.pop()
    elif cmd[0]  == "remove":
        s.remove(int(cmd[1]))
    else :
        s.discard(int(cmd[1]))

print(sum(list(s)))


### Symmetric difference
n = input()
N = list(map(int, input().split()))
m = input()
M = list(map(int, input().split()))

sym_diff = []

sym_diff.append(list(set(N).difference(set(M))))
sym_diff.append(list(set(M).difference(set(N))))

sym_diff = [item for sublist in sym_diff for item in sublist]

for elem in sorted(sym_diff):
    print(elem)
