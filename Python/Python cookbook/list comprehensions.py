lines=[line.strip() for line in open('m_ch1.py','r')]

print(lines)

lines_with_p=[line.strip() for line in open('m_ch1.py') if line[0]=='p']
lines_with_p

#len([line for line in open(r'C:\python\Tutorials\Python cookBook\David Beazley, Brian K. Jones - Python Cookbook-Oreilly (2013).pdf')])

list(zip(open('m_ch1.py') , open('m_ch1.py')))

import  pandas as pd