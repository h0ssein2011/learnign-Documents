N,X=map(int ,input().split())
studets=[]
for i in range(X):

    studets.append(map(float, input().split()))

for i in zip(*studets):
    print(sum(i)/len(i))
