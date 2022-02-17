from pytube import YouTube

with open(file='Dl_files.txt', mode='r') as f:
    for url in f.readlines():
        # print(url)

        yt = YouTube(url)
        file_name = yt.streams.first().default_filename
        
    
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('/home/hossein/Shared_Folder/')
        print('done')


