from pydub import AudioSegment
import sys

def convert_to_16khz(input_wav_path, output_wav_path):
    # Load the input audio file
    audio = AudioSegment.from_wav(input_wav_path)
    
    # Set the frame rate to 16 kHz
    audio_16khz = audio.set_frame_rate(16000)
    
    # Export the audio in 16 kHz
    audio_16khz.export(output_wav_path, format="wav")

if __name__ == "__main__":
    input_wav_path = sys.argv[1]  # Path to the input WAV file
    output_wav_path = "./samples/output_audio_16khz.wav"  # Path to the output WAV file

    convert_to_16khz(input_wav_path, output_wav_path)
    print(f"Converted {input_wav_path} to 16 kHz and saved as {output_wav_path}")
