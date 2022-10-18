from gtts import gTTS
import os
message= "you are awesome"
output=gTTS(text=message,lang="en",slow=False)
output.save("output.mp3")
os.system("start output.mp3")