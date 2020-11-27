# Music Generation

<img src="/showcase/img/team1.jpeg" alt="drawing" width="850"/>

Music is an art of time. It is formed by the colaboration of instruments -composed with many instruments collectively- harmonization of notes. So, music generation with deep neural networks strictly connected with this features of music. There are many models have been proposed so far for generating music. Some of them based on the structure of Recurrent Neural Networks or Generative Adversarial Networks or Variational Autoencoders.

In this work, we tackle the generating music with deep neural networks, especially with Vector Quantized Variational Autoencoders (Oord et al., 2017).

## Project Dependencies

- music21==5.7.0
- Keras==2.4.3
- NumPy==1.18.5
- pygame==1.9.6

## Jukebox
JukeBox is a generative model for music with singing that is based on Vector Quantized Variational Autoencoders. The models uses raw audio (.wav) for training data. We implemented upsampling section and created music based on different styles. Jukebox is trained on 1.2 million songs with paired lyrics and metadata from LyricWiki. Trained on 32 bit, 44.1 kHz.

Raw audio is represented as a continuous waveform $$x \in [-1,1]^T$$  where the number of samples $$T$$ is the product of the audio duration $$t$$ and the sampling rate, typically 16 kHz to 48 kHz. Input of the Vector Quantized Variational is this continuous waveform.

### Sampler
The [sampler.ipynb](https://github.com/inzva/music-generation/blob/main/jukebox/sampler.ipynb) notebook is for generate music with pre-trained weigths, using conditional informations.

- **Run it on colab!**
- To sample normally, model can be 5b, 5b_lyrics, 1b_lyrics.
- The hyperparameters are for a V100 GPU with 16 GB GPU memory. The 1b_lyrics, 5b, and 5b_lyrics top-level priors take up 3.8 GB, 10.3 GB, and 11.5 GB.
- If you continue to have memory issues after this (or run into issues on your own home setup), switch to the 1B model.


For more control over the generations, try co-composing with either the 5B or 1B Lyrics Models. Again, specify your artist, genre, and lyrics. However, now instead of generating the entire sample, the model will return 3 short options for the opening of the piece (or up to 16 options if you use the 1B model instead). Choose your favorite, and then continue the loop, for as long as you like. Throughout these steps, you'll be listening to the audio at the top prior level, which means it will sound quite noisy. When you are satisfied with your co-creation, continue on through the upsampling section. This will render the piece in higher audio quality. Your first samples will be located in your local drive folder, please mount the drive and choose your base storage directory. 

After all, choose your favorite sample from your latest group of generations, then upsample co-composition to higher audio quality.

Your final samples have to level: level 1 and level 0. The level_1 samples will be available after around one hour (depending on the length of your sample) and are saved under {hps.name}/level_0/item_0.wav, while the fully upsampled level_0 will likely take 4-12 hours. You can access the wav files down below, or using the "Files" panel at the left of this colab.

(Please note, if you are using this CoLab on Google's free tier, you may want to download intermediate steps as the connection will last for a maximum 12 hours.)

### Examples
[This folder](https://github.com/inzva/music-generation/tree/main/jukebox/samples) contains our examples for music generation. 

## wavhelper

If you have problems with playing .wav audio files, use the [script](https://github.com/inzva/music-generation/blob/main/wavhelper/mp32wav.py) in wavhelper folder.

```bash
python3 mp32wav.py --input /path/to/wav.wav --output /path/to/mp3.mp3
```

## midihelper

If you want a create simple RNN model for generating music using midi files, [midihelper.py](https://github.com/inzva/music-generation/blob/main/midihelper/midihelper.py) contains midi2sequence scripts, and if you have problems with playing midi files in your computer, [play.py](https://github.com/inzva/music-generation/blob/main/midihelper/play.py) and [playhelper.py](https://github.com/inzva/music-generation/blob/main/midihelper/playhelper.py) contain functions to play midi files.

```bash
python3 play.py --midi_file /path/to/midi.mid --volume 0.8 --frequency 44100 --bitsize -16 --nof_channels 2 --buffer 1024
```

## References

\[1\] Attentional networks for music generation, [arXiv](https://arxiv.org/pdf/2002.03854)

\[2\] MuseGAN: Multi-track Sequential Generative Adversarial Networks for Symbolic Music Generation and Accompaniment, [arXiv](https://arxiv.org/pdf/1709.06298.pdf)

\[3\] Jukebox: A Generative Model for Music, [arXiv](https://arxiv.org/pdf/2005.00341.pdf)

\[4\] Neural Discrete Representation Learning, [arXiv](https://arxiv.org/pdf/1711.00937.pdf)
