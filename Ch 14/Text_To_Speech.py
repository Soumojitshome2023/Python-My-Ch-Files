from gtts import gTTS
import os

mytext = "Hi, this is an example of converting text to audio. This is a bot speaking here, not a real human!"
audio = gTTS(text=mytext, lang="en", slow=False)

audio.save("Text_To_Speech_example.mp3")
# os.system("Text_To_Speech_example.mp3")

# audio.save("example.mp3")
# os.system("start example.mp3")  this line for auto play the audio

print("Done")