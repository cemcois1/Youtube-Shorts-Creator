import os

from Scripts.SoundCreator import SoundCreator
from Scripts.VideoCreator import create_video_Only_Added_Audio, add_Sound_to_Video, add_text_to_video
from Scripts.OCRReader import ocr_reader
import moviepy.editor as mp



soundPath= 'audio.mp3'
BackgroundVideoPath='BGVideo.mp4'
firstPhotoPath='SS.png'

# OCR işlemi yap ses yazısını al
#text = ocr_reader(firstPhotoPath)

# Metinleri ekrana yazdır
text="What made you realize you're old? this is test message testing a"

#Sound Creating part
soundGenerator=SoundCreator('AKIA2UVTRW7EEE2WUUMW','mO9lK2fnCvskO6oph3n8FxGGr8hKOn3QtOm+paKl','eu-west-2')
# Text to Speech
ttsSound = soundGenerator.create_sound(text=text, output_format='mp3',
                                    voice_id='Salli')


# Add sound to Sound file

with open(soundPath, 'wb') as file:
    file.write(ttsSound)

# find sound duration
clip = mp.CompositeAudioClip([mp.AudioFileClip(soundPath)])
print(str(clip.duration) + " seconds sound time")


# Video Creating part
firstResultVideoPath='Result0.mp4'
seccondVideoPath='Result1.mp4'
create_video_Only_Added_Audio(soundPath, BackgroundVideoPath,firstResultVideoPath,audioTime=clip.duration)

add_text_to_video(firstResultVideoPath,seccondVideoPath,text)

#open output video
#Add TTS Sound To Video
#add_Sound_to_Video(soundPath,'videoplayback.mp4','OutputVideo.mp4')


"""
1-video için ses oluştur 
2-sesi ana videoya ekle
3-


"""



