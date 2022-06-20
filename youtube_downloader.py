from pytube import YouTube
from pytube.cli import on_progress #load bar

URL = input("What YouTube video do you want to download. URL: ")

def complete_func(stream, file_path):
    """When a youtube video download is complete, it will trigger this funtion"""

    print("Finished downloading")
    print(f"Video Location: {file_path}")

def download_youtube(url):
    """
    Downloads video process. For more information look at https://pytube.io/en/latest/user/quickstart.html or https://pypi.org/project/pytube/.
    Also if you want to know how I did the loading bar look at this https://www.thiscodeworks.com/python-3-x-how-to-use-progress-bar-in-pytube-stack-overflow-python/62145f324ef606001531dbb2
    """
    yt = YouTube(   
        url,
        on_progress_callback=on_progress, #runs the load bar funtion from pytube.cli
        on_complete_callback=complete_func, #call funtion when video is done
        use_oauth=False, 
        allow_oauth_cache=True #can use your youtube account
    )

    video_resolution = yt.streams.get_highest_resolution()
    video_resolution.download()
    
def main():
    download_youtube(URL)

if __name__ == "__main__":
    main()