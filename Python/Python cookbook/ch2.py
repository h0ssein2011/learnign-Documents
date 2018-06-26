# splitting text

line = 'asdf fjdk; afed, fjek,asdf, foo'
import re

r=re.split(r'[;,\s]\s*',line)
r
