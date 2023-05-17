from moviepy.editor import *
from moviepy.audio.AudioClip import AudioArrayClip
import textwrap
import numpy as np


def create_video_Only_Added_Audio(audio_file_path, video_file_path, output_file_path, audioTime=None):
    # Define video file
    audiofileclip = AudioFileClip(audio_file_path)

    # Cut audio file to the specified time if audioTime is given
    if audioTime is not None:
        audiofileclip = audiofileclip.subclip(0, audioTime)

    video_file = VideoFileClip(video_file_path)

    if audiofileclip.duration < video_file.duration:
        # Calculate the difference in duration
        duration_diff = video_file.duration - audiofileclip.duration
        # Create a silent audio clip of the difference in duration
        silent_clip = AudioArrayClip(np.zeros((int(duration_diff * audiofileclip.fps), audiofileclip.nchannels)),
                                     fps=audiofileclip.fps)
        # Concatenate the original audio clip with the silent audio clip
        audiofileclip = concatenate_audioclips([audiofileclip, silent_clip])

    video_file_audioclip = video_file.audio
    # Write the video file
    video_with_new_audio = CompositeAudioClip([audiofileclip])
    video_file.audio = video_with_new_audio
    video_file.write_videofile(output_file_path,
                               codec='libx264',
                               audio_codec='aac',
                               temp_audiofile='temp-audio.m4a',
                               remove_temp=True,
                               fps=60)
def add_text_to_video(video_file_path, output_file_path, text):
    # Define video file
    video_clip = VideoFileClip(video_file_path)

    wrapper = textwrap.TextWrapper(width=26)
    wrapped_text = '\n'.join(wrapper.wrap(text))

    # Get the width of the video
    video_width,video_height = video_clip.size

    # Create a TextClip (requires ImageMagick)
    txt_clip = TextClip(wrapped_text, color='white')

    # Resize the text to fit within the video
    txt_clip = txt_clip.on_color(size=(video_width-int(video_width/8), txt_clip.size[1]))

    # Center the TextClip
    txt_clip = txt_clip.set_pos('center').set_duration(video_clip.duration)

    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([video_clip, txt_clip])

    # Write the video file
    video.write_videofile(output_file_path,
                          codec='libx264',
                          audio_codec='aac',
                          temp_audiofile='temp-audio.m4a',
                          remove_temp=True,
                          fps=60)
def add_Sound_to_Video(sound_file_path, video_file_path, output_file_path):
    # Define video file
    audiofileclip = AudioFileClip(sound_file_path)
    video_file = VideoFileClip(video_file_path).subclip(0,30)

    # Write the video file
    video_with_new_audio = CompositeAudioClip([audiofileclip])
    video_file.audio = video_with_new_audio
    video_file.write_videofile(output_file_path,
                               codec='libx264',
                               audio_codec='aac',
                               temp_audiofile='temp-audio.m4a',
                               remove_temp=True,
                               fps=60)