from pytube import Playlist
import download_video

def run(url):
    try:
        urls = Playlist(url)
        if urls:
            for link in urls:
                download_video.run(link)
        else:
            print("No links found")
    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    url = input("Enter the playlist URL: ")
    run(url)
