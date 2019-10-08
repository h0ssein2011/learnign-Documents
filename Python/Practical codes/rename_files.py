
import os
# change the dicnaries
os.chdir('C:/Users/Hossein/Desktop/dl1/W1')
#get all filenames and rename based on the this 
for file in os.listdir():


    f=open(file,'r')
    src=file[f.name.find('(')+1:f.name.find(')')]
    extention=file[f.name.find('.'):]
    f.close()
    new_name=src+'_'+file[:f.name.find('(')]+extention

    os.rename(file,new_name)
