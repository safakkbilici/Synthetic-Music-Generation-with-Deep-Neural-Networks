import pygame
import argparse


class MIDI(object):
    def __init__(self, volume = 0.8,freq=44100,
                 bitsize=-16, nof_channels=2,buffer=1024):
        self.volume = volume # [0,1.0]
        self.freq = freq
        self.bitsize = bitsize
        self.nof_channels = nof_channels
        self.buf = buffer
    def play_music(self,music_file):

        clock = pygame.time.Clock()
        #try:
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            clock.tick(30)

    def play_midi(self,midi_file):
        pygame.mixer.init(self.freq, self.bitsize, self.nof_channels, self.buf)

        pygame.mixer.music.set_volume(self.volume)
        try:
            self.play_music(midi_file)
        except KeyboardInterrupt:
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.stop()
            raise SystemExit
