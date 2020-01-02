N_En=int(input())
En_roll=list(map(int,input().split()))
N_Fr=int(input())
Fr_roll=list(map(int,input().split()))

print(sum([1  for i in En_roll if i in Fr_roll ]))
