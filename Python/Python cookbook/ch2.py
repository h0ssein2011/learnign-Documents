# splitting text

line = 'asdf fjdk; afed, fjek,asdf, foo'
import re

r=re.split(r'[;,\s]\s*',line)
r

fields =re.split(r'(;|,|\s*)',line)

# start and end a text
filename='spam.txt'

filename.startswith('spam')
filename.endswith('.txt')

name,format=filename.split('.')

#mulitplie choose
import os
filename=os.listdir()
filename

[name for name in filename if name.endswith(('.py','.h'))]
