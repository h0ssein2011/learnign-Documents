# this is function tutorial

def print_two(*args):
      arg1,arg2=args
      print(f"arg1:{arg1} , arg2 {arg2}")

def print_two_again(arg1,arg2):
    print(f"arg1:{arg1} , arg2 {arg2}")

def print_one(arg1):
    print(f"arg1:{arg1}")

def print_none():

    print("this def do nothing")

print_two("hossein","mortazavi")
print_two_again("hossein","mortazavi")
print_one("hossein")
print_none()

print(" ")
