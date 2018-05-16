# this is reading and writing tutorials

from sys import argv

script , fileName =argv

print(f"we are going to erase {fileName}")
print("if you dont want that enter Ctr+C")
print("if you want press Enter in your keyboard")

input("?")

print("opening the file ....")
target=open(fileName,'w')

print("truncating the file! goodBye")
target.truncate()

print("Now I am asking you some Line")
Line1=input("Line1:")
Line2=input("Line2:")
Line3=input("Line3:")

target.write(Line1)
target.write("\n")
target.write(Line2)
target.write("\n")
target.Line3(Line3)
target.write("\n")

print("and finally we close it")

target.close()
