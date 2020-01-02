# Enter your code here. Read input from STDIN. Print output to STDOUT
n_A = int(input())

set_A = set(map(int, input().split()))
n_command = int(input())

for i in range(n_command):
    com_input=input().split()
    command=str(com_input[0])
    set_B_input=input().split()
    set_B=set(map(int, set_B_input))


    eval('set_A.{0}({1})'.format(command,set_B))
print(sum(set_A))
