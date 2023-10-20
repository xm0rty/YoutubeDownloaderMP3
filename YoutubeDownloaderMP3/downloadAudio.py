from pytube import YouTube
import os

# Get the video

ytVideos = str(input("Enter links separated by coma if multiple: ")).split(",")
try:
    for videoLink in ytVideos:
        ytVideo = YouTube(videoLink)

        # Downloads the audio
        audio = ytVideo.streams.filter(only_audio=True).get_audio_only()
        # download the file
        out_file = audio.download("Audios/")
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + "Audio.mp3"
        os.rename(out_file, new_file)

    print("Done! Audio Downloaded")
    input("You can now close this window")

except:
    print("error")
    input("Please close this window and retry")
    exit()
