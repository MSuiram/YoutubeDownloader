from pytubefix import YouTube 
from pytubefix.cli import on_progress

def download(url):
        yt = YouTube(url)
        print(f"Début de : {yt.title}") 
        ys = yt.streams.get_highest_resolution()
        ys.download()
        print(f"Fin de : {yt.title}")

video_download = []
invalid_url = []

with open("url.txt", "r", encoding="utf-8") as file:
    video_no_download = file.readlines()
    print(video_no_download)

for url in video_no_download:
    try:
        download(url)
        video_download.append(url)
    except:
        print(f'This url : {url} is invalid')
        invalid_url.append(url)

if len(url) != 0:
    print(f'There is {len(invalid_url)} invalid url !!!')
    with open("invalid.txt", "w", encoding="utf-8") as f:
        for url in invalid_url:
            f.write(url)