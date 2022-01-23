from moviepy.editor import VideoFileClip
import glob

name = input()

for file in glob.glob("D:/Deskop/App/"+ name + ".mp4"):
    print(file)
    videoclip = VideoFileClip(file)
    audioclip = videoclip.audio
    audioclip.write_audiofile("D:/Deskop/App/" + name + ".mp3")
