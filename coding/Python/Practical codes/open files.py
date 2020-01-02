url_list=[line for line in open('Parsget.txt')]

import webbrowser

for url in url_list:
    webbrowser.open(url)
