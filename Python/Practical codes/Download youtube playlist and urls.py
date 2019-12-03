#https://pypi.org/project/pytube/
from pytube import Playlist
from pytube import YouTube

pl = Playlist("https://www.youtube.com/watch?v=9BUiX1zOiGE&list=PL6284FEC8658EB472")
#pl.download_all()
#pl.parse_links()
urls=pl.parse_links()
# or if you want to download in a specific directory
# pl.download_all('C:/Users/hossein.mortazavi/Desktop/Kaggle competition/',)
part1='https://www.youtube.com'
part3='watch?v=9BUiX1zOiGE&list=PL6284FEC8658EB472&index='
links=[]
counter=1
for link in urls:
    links.append(part1+link+part3+str(counter))
    counter+=1


counter=0
count_error=0
for link in links[21:22]:
    try:
        counter+=1
        yt=YouTube(link)
        YouTube(link).streams.first().download('C:/Users/hossein.mortazavi/Desktop/dating advice')
        print('video {} downloaded'.format(counter))
    except:
        count_error+=1
        pass
print('video {} downloaded'.format(counter))
print('{} videos got error '.format(count_error))


