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

# match check

filename='test.txt'

filename[:4] == 'test'
filename[-4:] == '.txt'

#another way is use regular exprecsions
import re
url='http://python.org'

re.match('http:https:ftp',url)

from fnmatch import fnmatch,fnmatchcase
fnmatch('foo.txt','*.txt')

fnmatch('foo.txt','?oo.txt')

fnmatch('Dat45.csv','Dat[0-9]*')

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
[name for name in names if fnmatch(name,'Dat[0-9]*')]
