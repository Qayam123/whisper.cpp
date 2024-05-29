from pydub import AudioSegment
import sys

class Conversion:

    def __init__(self, audio_filepath, wav_filepath):
        self.audio_filepath = audio_filepath
        self.wav_filepath = wav_filepath
    
    def convert_mp3_to_wav(self):
        # Load the MP3 file
        audio = AudioSegment.from_mp3(self.audio_filepath)
        # Export as WAV
        wav_temp_path = "temp.wav"
        audio.export(wav_temp_path, format="wav")
        return wav_temp_path

    def convert_to_16khz(self):
        # Convert MP3 to WAV
        wav_temp_path = self.convert_mp3_to_wav()
        # Load the temporary WAV file
        audio = AudioSegment.from_wav(wav_temp_path)
        # Set the frame rate to 16 kHz
        audio_16khz = audio.set_frame_rate(16000)
        # Export the audio in 16 kHz
        audio_16khz.export(self.wav_filepath, format="wav")
        return self.wav_filepath

if __name__ == "__main__":
    input_mp3_path = sys.argv[1]  # Path to the input MP3 file
    output_wav_path = sys.argv[2]  # Path to the output WAV file
    conversion_obj = Conversion(input_mp3_path, output_wav_path)
    result = conversion_obj.convert_to_16khz()
    print(f"Converted {input_mp3_path} to 16 kHz and saved as {output_wav_path}")

