# this is reading tutorials

from sys import argv

script,fileName=argv

txt=open(fileName)

print(f"here your {fileName}:")

print(txt.read())

print("type the fileName again")
file_again=input(">")

txt_again=open(file_again)

print(txt_again.read())
