# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(input().split())
print(all(a > set(input().split()) for _ in range(int(input()))))
