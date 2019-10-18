N_En=int(input())
En_roll=list(map(int,input().split()))
N_Fr=int(input())
Fr_roll=list(map(int,input().split()))

both=set(En_roll+Fr_roll)
print(len(both))
