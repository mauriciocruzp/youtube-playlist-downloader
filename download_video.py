from pytube import YouTube
import re


def run(url):
    try:
        yt = YouTube(url)
        file_extension = "mp4"
        filename = yt.author + " - " + yt.title + "." + file_extension
        filename = re.sub(r'[<>:"/\\|?*]', '', filename)

        yt.streams.filter(progressive=True, file_extension=file_extension).order_by(
            "resolution"
        ).desc().first().download(filename=filename, output_path="downloads")
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":
    url = input("Enter the video URL: ")
    run(url)
