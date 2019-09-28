#this programm print a component of a range
if __name__ == '__main__':
   n = int(input())
s=''
print(s.join([str(i) for i in range(1,n+1)])

#in this part I want to write a function that do the same thing here

def print_numbers(n):
    s=''
    s=s.join([str(i) for i in range(1,n)])
    print(s)
print_numbers(100)
