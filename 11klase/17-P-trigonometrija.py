import math
import matplotlib.pyplot as plt
import numpy as np
import pyaudio

def trig1(a, f):
    grafiksX = []
    grafiksY = []
    grafiksY1 = []
    x = -0.01
    while x<0.01:
        y = a * math.sin(f*2*math.pi*x)
        y1 = a * math.sin((f/4)*2*math.pi*x)
        grafiksX.append(x)
        grafiksY.append(y)
        grafiksY1.append(y1)
        x += 0.000001

    plt.plot(grafiksX, grafiksY)
    plt.plot(grafiksX, grafiksY1)
    plt.title(f'Skaņas grafiks. Frekvence {f} un {f/4}')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()

def trig1_ar_skanu(a, f, t):    
    fs = 44100       # sampling rate, Hz, must be integer

    p = pyaudio.PyAudio()
    samples = (a*np.sin(2*np.pi*np.arange(fs*t)*f/fs)).astype(np.float32)
    stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)
    stream.write(samples)
    stream.stop_stream()
    stream.close()
    p.terminate()
#a
trig1(1, 250)
trig1_ar_skanu(0.1, 173, 7)

# import math
# import matplotlib.pyplot as plt
# import numpy as np
# import pyaudio

# def trig2(a):
#     grafiksX = []
#     grafiksY = []

#     x = -10
#     while x<10:
#         y = a * math.sin(x)
#         y1 = a * math.sin(x)
#         grafiksX.append(x)
#         grafiksY.append(y)
#         x += 0.00001

#     plt.plot(grafiksX, grafiksY)
#     plt.title(f'Skaņas grafiks. Frekvence {a}')
#     plt.xlabel('x')
#     plt.ylabel('y')

#     plt.show()

# def trig1_ar_skanu(a, f, t):    
#     fs = 44100       # sampling rate, Hz, must be integer

#     p = pyaudio.PyAudio()
#     samples = (a*np.sin(2*np.pi*np.arange(fs*t)*f/fs)).astype(np.float32)
#     stream = p.open(format=pyaudio.paFloat32,
#                 channels=1,
#                 rate=fs,
#                 output=True)
#     stream.write(samples)
#     stream.stop_stream()
#     stream.close()
#     p.terminate()

# trig2(300)
# trig1_ar_skanu(14, 150, 25)