import moviepy.editor

from tkinter.filedialog import *

vid = askopenfilename()
video = moviepy.editor.VideoFileClip(vid) # you can also give the video path or url rather than vid  

aud = video.audio
aud.write_audiofile("enjoy.mp3")

print("----Listen----")
