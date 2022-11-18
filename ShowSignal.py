import matplotlib.pyplot as plt
import SpeechAndSilence
class Process:
    def __init__(self,url,text,N_FFT = 512) -> None:       
        self.Audio = SpeechAndSilence.Process(url,N_FFT)
        self.text = text
    def show(self):
        figure, axis = plt.subplots(2,2)
        axis[0][0].plot(self.Audio.getOriginSignal()[0],self.Audio.getOriginSignal()[1])
        axis[0][0].set_title(self.text)
        axis[0][1].plot(self.Audio.getSpeechSignal()[0],self.Audio.getSpeechSignal()[1])
        axis[0][1].set_title("Tính hiệu tiếng nói")
        axis[1][0].plot(self.Audio.getStableSignal()[0],self.Audio.getStableSignal()[1])
        axis[1][0].set_title("Tính hiệu tiếng nói ổn định")
        axis[1][1].plot(self.Audio.getVectorFFT()[0],self.Audio.getVectorFFT()[1])
        axis[1][1].set_title(f"Vector FFT với {self.Audio.N_FFT} chiều")
        plt.show()