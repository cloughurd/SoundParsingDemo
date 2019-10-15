import soundfile as sf
import matplotlib.pyplot as plt

data, sr = sf.read('gingerbread2019_09_30_10_01_39.wav')

print(len(data))

plt.plot(data)
plt.show()

# plt.plot(data[1])
plt.show()

print(data)
print(sr)