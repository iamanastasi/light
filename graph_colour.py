import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def find_spectrum_box(filename, pad=10):
    img = np.asarray(Image.open(filename).convert("RGB"), dtype=float)
    brightness = img.max(axis=2)
    ys, xs = np.where(brightness > 25)
    return ys.min() - pad, ys.max() + pad, xs.min(), xs.max()

y1, y2, x1, x2 = find_spectrum_box("white.png")

def readIntensity(filename):
    img = np.asarray(Image.open(filename).convert("RGB"), dtype=float)
    crop = img[y1:y2, x1:x2]
    intensity = crop.mean(axis=(1, 2))
    return intensity, crop

white, white_crop = readIntensity("white.png")
red, _ = readIntensity("red.png")
yellow, _ = readIntensity("yellow.png")
green, _ = readIntensity("green.png")
blue, _ = readIntensity("blue.png")

wavelength = np.linspace(400, 700, len(white))

plt.figure(figsize=(10, 6))
ax = plt.gca()
ax.set_facecolor("lightgrey")
plt.plot(wavelength, white, "w", linewidth=2, label="белый лист")
plt.plot(wavelength, red, "r", linewidth=1.5, label="красный лист")
plt.plot(wavelength, yellow, "gold", linewidth=1.5, label="жёлтый лист")
plt.plot(wavelength, green, "g", linewidth=1.5, label="зелёный лист")
plt.plot(wavelength, blue, "b", linewidth=1.5, label="синий лист")

top = np.max(white) * 1.05
strip = np.transpose(white_crop, (1, 0, 2))
strip = np.clip(strip / np.max(strip) * 1.5, 0, 1)
plt.imshow(strip, extent=[wavelength[0], wavelength[-1], -0.08 * top, 0], aspect="auto")

plt.ylim(-0.08 * top, top)
plt.xlim(wavelength[0], wavelength[-1])
plt.xlabel("Длина волны, нм")
plt.ylabel("Интенсивность, отн. ед.")
plt.title("Интенсивность света лампы накаливания")
plt.legend()
plt.grid(True, alpha=0.4)
plt.tight_layout()
plt.savefig("intensities.png", dpi=300)
plt.show()

mask = white > (np.max(white) * 0.05)
wl_valid = wavelength[mask]

albedo_white = white[mask] / white[mask]
albedo_red = red[mask] / white[mask]
albedo_yellow = yellow[mask] / white[mask]
albedo_green = green[mask] / white[mask]
albedo_blue = blue[mask] / white[mask]

plt.figure(figsize=(10, 6))
ax = plt.gca()
ax.set_facecolor("lightgrey")
plt.plot(wl_valid, albedo_white, "w", linewidth=2, label="белый лист")
plt.plot(wl_valid, albedo_red, "r", linewidth=1.5, label="красный лист")
plt.plot(wl_valid, albedo_yellow, "gold", linewidth=1.5, label="жёлтый лист")
plt.plot(wl_valid, albedo_green, "g", linewidth=1.5, label="зелёный лист")
plt.plot(wl_valid, albedo_blue, "b", linewidth=1.5, label="синий лист")

plt.ylim(0, 1.1)
plt.xlim(430, 650)
plt.xlabel("Длина волны, нм")
plt.ylabel("Альбедо")
plt.title("Альбедо цветных листов")
plt.legend()
plt.grid(True, alpha=0.4)
plt.tight_layout()
plt.savefig("albedo.png", dpi=300)
plt.show()
