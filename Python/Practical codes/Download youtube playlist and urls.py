#https://pypi.org/project/pytube/
from pytube import Playlist
from pytube import YouTube

pl = Playlist("https://www.youtube.com/watch?v=2d6hh2Ryx_c&list=PLpQWTe-45nxL3bhyAJMEs90KF_gZmuqtm&index=3")
#pl.download_all()
pl.parse_links()
# urls=pl.parse_links()
# or if you want to download in a specific directory
# pl.download_all('C:/Users/hossein.mortazavi/Desktop/Kaggle competition/',)
part1='https://www.youtube.com'
part3='&list=PLpQWTe-45nxL3bhyAJMEs90KF_gZmuqtm&index='
links=[]
counter=1
for link in urls:
    links.append(part1+link+part3+str(counter))
    counter+=1


counter=0
count_error=0
for link in links[]:
    try:
        counter+=1
        yt=YouTube(link)
        YouTube(link).streams.first().download()
        print('video {} downloaded'.format(counter))
    except:
        count_error+=1
        pass
print('video {} downloaded'.format(counter))
print('{} videos got error '.format(count_error))
