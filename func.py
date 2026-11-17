import numpy as np
import matplotlib.pyplot as plt
import lightfunction as light

mercury = light.readIntensity( "rtut.png",   "mercury2.png", "ртутная лампа", "белый лист")
from scipy.signal import find_peaks