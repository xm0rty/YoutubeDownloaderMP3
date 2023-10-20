from pytube import YouTube

userContinue = True
while(userContinue):
    ytVideos = str(input("Enter links separated by comma if multiple (ex: https://youtu.be/*,https://youtu.be/*): ")).split(",")
    try:
        for videoLink in ytVideos:
            ytVideo = YouTube(videoLink)
            # Downloads the audio
            audio = ytVideo.streams.filter(only_audio=True).first().download("Audios/",filename=ytVideo.title + ".mp3")
            print(f"Done! {ytVideo.title} has been downloaded")
        while(True):
            print("Do you want to download more? (Y/N)")
            userInput = input().upper()
            if(userInput!='Y' and userInput!='N'):
                print("Wrong Input")
            elif(userInput=='N'):
                userContinue = False
                break
            elif(userInput=='Y'):
                break
    except:
        print("error")
        input("Please close this window and retry")
        exit()
