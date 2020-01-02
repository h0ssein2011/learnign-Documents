N_En=int(input())
En_roll=set(map(int,input().split()))
N_Fr=int(input())
Fr_roll=set(map(int,input().split()))

ymmetric_difs=En_roll.symmetric_difference(Fr_roll)
print(len(ymmetric_difs))
