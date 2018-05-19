# this tutorial is related to copy from one file to another

# load needed packages
from sys import argv
from os.path import exists

# get appropriate data
script,from_file,to_file=argv

# just simple print
print(f"we want to copy from {from_file} to {to_file}")

# open origin file
in_file=open(from_file)
# read origin file
in_data=in_file.read()

#simple line fot getting file
print(f"the input file has {len(in_data)} byte long")
print(f"Does the output file exist? {exists(to_file)}")
print("Are you ready? so press Enter to proceed")
input()

# open destination file
out_file=open(to_file,'w')
#write des file
out_file.write(in_data)

print("well done all things done.")
# close files
out_file.close()
in_file.close()
print(" ")
