import numpy as np
import matplotlib.pyplot as plt
import lightfunction as light
dataPath="data/"
import imageio
photo = light.straighten(imageio.imread(dataPath + "rtut.png"))
rgb = np.mean(photo[light.ROWS, light.COLS, 0:3], axis=1)
red, green, blue = rgb[:, 0], rgb[:, 1], rgb[:, 2]
from scipy.signal import find_peaks
peaks_red, _ = find_peaks(red, prominence=20)
peaks_green, _ = find_peaks(green, prominence=20)
peaks_blue, _ = find_peaks(blue, prominence=1)
print(peaks_red, peaks_green, peaks_blue)
peaks = [435.8, 487.7, 546.1, 611.6] # нм
pixels = [77, 139, 240, 355]                         # ваши номера пикселей


fit = np.polyfit(pixels, peaks, 1)
a, b = fit

print(f"k = {a:.6f} , b={b:.6f}")

pixel_numbers = np.arange(len(rgb))


wavelength = np.polyval(fit,pixel_numbers)



plt.figure(figsize=(10, 7))

plt.plot(pixels, peaks, 'o')

plt.plot(
    pixels,
    np.polyval(fit, pixels),
)

plt.xlabel("Номер пикселя")
plt.ylabel("Длина волны, нм")
plt.title("Калибровочная зависимость длины волны от номера пикселя")
plt.legend()
plt.grid()

plt.show()
