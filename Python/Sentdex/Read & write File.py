# write an read tutorial

root='C:/'

text='this is a sample\n text'

saveFile=open(root+'exampleWtite.txt','w')

saveFile.write(text)

saveFile.close()
print('please go to %s to see the file' % root)
