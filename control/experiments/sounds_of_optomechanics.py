#!/usr/bin/python
from sys import argv
rawfile = argv[1]
wavfile = rawfile[:-4] + '.wav'
mp3file = wavfile[:-4] + '.mp3' # sounded shite with default lame settings

import LeCroy
(header,x,y,i) = LeCroy.InterpretWaveform(open(rawfile).read())
import scipy.io.wavfile
scipy.io.wavfile.write(wavfile, 192000/16, y-y.mean())

# first applied to 2016-11-24_14-31-40.raw
# frequency 45kHz => downscaled frequecy 45kHz*(192000/16)/2E6 ~ 270Hz cf. C_4 = 261Hz 
