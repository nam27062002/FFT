from python_speech_features import mfcc
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
(rate,sig) = wav.read("Test/1/a.wav")
mfcc_feat = mfcc(sig,rate)
plt.plot(mfcc_feat)
plt.show()