from pydub import AudioSegment
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input','-in',type = str, help = 'MP3 file')
parser.add_argument('--output','-out',type = str, help = 'Path to WAV file.')
args = parser.parse_args()

sound = AudioSegment.from_mp3(args.input)
sound.export(args.output, format="wav")  
