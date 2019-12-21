#https://pypi.org/project/pytube/
from pytube import Playlist
from pytube import YouTube
import os

pl = Playlist("https://www.youtube.com/watch?v=qBigTkBLU6g&list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9")
#pl.download_all()
#pl.parse_links()
urls=pl.parse_links()
# or if you want to download in a specific directory
# pl.download_all('C:/Users/hossein.mortazavi/Desktop/Kaggle competition/',)
part1='https://www.youtube.com'
part3='watch?v=IFKQLDmRK0Y&list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9&index='

links=[]
counter=1
for link in urls:
    links.append(part1+link+part3+str(counter))
    counter+=1


counter=0
count_error=0
for link in links:
    try:
        counter+=1
        yt=YouTube(link)
        outputfile=YouTube(link).streams.first().download('C:/Users/hossein.mortazavi/Desktop/Statquest')
        file_name=os.name(outputfile)
        print(file_name)
        print('video {} downloaded'.format(counter))
    except:
        count_error+=1
        pass
print('video {} downloaded'.format(counter))
print('{} videos got error '.format(count_error))


