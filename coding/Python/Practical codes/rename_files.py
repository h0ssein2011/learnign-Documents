
import os
# change the dicnaries
os.chdir('/media/hossein/0881-8560/sq_ml')
#get all filenames and rename based on the this

for file in os.listdir():


    f=open(file,'r')
    # src=file[f.name.find('(')+1:f.name.find(')')]
    # src=file[:f.name.find('How')].strip()
    # extention=file[f.name.find('.'):]
    # f.close()
    # # new_name=src+'_'+file[:f.name.find('(')]+extention
    # new_name=src + extention
    # #print(new_name)
    new_name=f.name.replace('StatQuest','')
    os.rename(file,new_name)

    print(f.name)