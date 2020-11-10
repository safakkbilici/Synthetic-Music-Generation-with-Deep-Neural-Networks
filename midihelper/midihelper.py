from glob import glob
import os
from music21 import converter, instrument, note, chord, stream
import pickle
import numpy as np
from keras.utils import np_utils;

def getNotes(path_to_midi):
    data = glob(path_to_midi+'/*.mid')
    data = data[:3]
    notes = []
    for midifile in data:
        midi = converter.parse(midifile)
        parse_note = []
        try:
            parts = instrument.partitionByInstrument(midi)
        except:
            pass
        if parts:
            parse_note = parts.parts[0].recurse()
        else:
            parse_note = midi.flat.notes

        for a_note in parse_note:
            if isinstance(a_note,note.Note):
                notes.append(str(note.pitch))
            elif isinstance(a_note,chord.Chord):
                notes.append('.'.join(str(n) for n in a_note.normalOrder))

    with open('data/notes','wb') as f:
        pickle.dump(notes,f)

    return notes

def noteToSequence(notes,nvocab):
    seq_len = 100
    pitches = sorted(set(note for note in notes))
    int_note = dict((note,number) for number, note in enumerate(pitches))

    inp = []
    out = []

    for i in range(0, len(notes) - seq_len, 1):
        seq_in = notes[i: i+seq_len]
        seq_out = notes[i + seq_len]
        inp.append([int_note[ascii] for ascii in seq_in])
        out.append(int_note[seq_out])

    npatterns = len(inp)

    inp = np.reshape(inp, (npatterns,seq_len,1))
    inp = inp / float(nvocab)
    out = np_utils.to_categorical(out)

    return (inp,out)
