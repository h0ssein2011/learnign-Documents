#https://pypi.org/project/pytube/
from pytube import Playlist
from pytube import YouTube
import os

pl = Playlist("https://www.youtube.com/watch?v=Gv9_4yMHFhI&list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF")
#pl.download_all()
#pl.parse_links()
urls=pl.parse_links()
# or if you want to download in a specific directory
# pl.download_all('C:/Users/hossein.mortazavi/Desktop/Kaggle competition/',)
part1='https://www.youtube.com/'
part3='watch?v=fSytzGwwBVw&list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF&index='


download_indexes = [8,9,13,16,17,18,19,21,22,23,24,26,27,28,30,33,37,38,43,47,48,49,50,51,54]

links=[]
counter=1
for link in urls:

    links.append(part1+link+part3+str(counter))
    counter+=1

counter=0
count_error=0
error_links=[]
for link in links:
    try:
        counter+=1
        if counter in download_indexes:
            yt=YouTube(link)
            file_name=str(counter)+'_'+yt.streams.first().default_filename
            # remove double format names in filename
            file_name = file_name[0:file_name.find('.')]
            yt.streams.first().download(filename=file_name)

            print('video {} downloaded'.format(counter))
    except:
        count_error+=1
        error_links.append(link)
        pass
print('video {} downloaded'.format(counter))
print('{} videos got error '.format(count_error))


# error_links

with open('got_errors2.txt' ,'w') as error_lks:
    for url in error_links:
        error_lks.write('%s\n' % url)

