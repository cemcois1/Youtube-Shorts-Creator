import boto3


class SoundCreator:
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        self.client = boto3.client('polly',
                                   aws_access_key_id=aws_access_key_id,
                                   aws_secret_access_key=aws_secret_access_key,
                                   region_name=region_name)

    def create_sound(self, text, voice_id='Joanna', output_format='mp3'):
        response = self.client.synthesize_speech(Text=text, OutputFormat=output_format,
                                                 VoiceId=voice_id)

        return response['AudioStream'].read()
