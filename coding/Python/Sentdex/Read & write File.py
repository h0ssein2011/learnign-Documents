# write an read tutorial


text='this is a sample\n text'

saveFile=open('exampleWtite.txt','w')

saveFile.write(text)

saveFile.close()

# append the file


app_file=open('exampleWtite.txt','a')

app_file.write(append_text)

app_file.close()
