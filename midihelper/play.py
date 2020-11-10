from playhelper import MIDI

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--midi_file','-mid',type = str, help = 'A MIDI file to play.')
parser.add_argument('--volume','-vol',type = float, default=0.8,help = 'Volume.')
parser.add_argument('--frequency','-freq',type=int,default=44100,help='Frequency.')
parser.add_argument('--bitsize','-bit',type= int,default=-16,help='Bitsize')
parser.add_argument('--nof_channels','-c',type = int,default=2,help='Number of channels.')
parser.add_argument('--buffer', '-buf', type=int,default=1024,help='Buffer')
args = parser.parse_args()

player = MIDI(args.volume,args.frequency,args.bitsize,args.nof_channels,args.buffer)

player.play_midi(args.midi_file)
