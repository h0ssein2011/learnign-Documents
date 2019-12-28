url_list=[line for line in open(r'C:\Users\hossein.mortazavi\Downloads\Parsget (3).txt')]

import webbrowser

for url in url_list:
    webbrowser.open(url)
