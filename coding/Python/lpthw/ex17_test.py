# this is a test that show I can handle soft jobs

from sys import argv

from os.path import exists

script,from_file,to_file=argv
# open the file
in_data=open(from_file)
in_data=in_data.read()

print(f"the lenght of data is:{len(in_data)} byte")
#print(f"the input file has {len(in_data)} byte long")


out_data=open(to_file,'w')
out_data=out_data.write(in_data)

print("thats all let see the result")

in_data.close()
out_data.close()
