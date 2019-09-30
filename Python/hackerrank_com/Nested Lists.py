if __name__ == '__main__':
    n=int(input())
    students=[]
    students=[[input(), float(input())] for _ in range(n) ]


second_highest = sorted(list(set([marks for name, marks in students])))[1]
print('\n'.join([a for a,b in sorted(students) if b == second_highest]))
