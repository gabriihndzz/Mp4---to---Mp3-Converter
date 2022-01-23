from moviepy.editor import VideoFileClip
import glob

name = input()

for file in glob.glob("D:/Down. application/Version 4.0/App/Downloaded/"+ name + ".mp4"):
    print(file)
    videoclip = VideoFileClip(file)
    audioclip = videoclip.audio
    audioclip.write_audiofile("D:/Down. application/Version 4.0/App/Downloaded/" + name + ".mp3")
