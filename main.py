import numpy as np
import matplotlib.pyplot as plt


# Fonction DFT 1D
def dft(signal):
    N = len(signal)
    X = np.zeros(N, dtype=complex)  # Tableau pour stocker les coefficients de la DFT

    for k in range(N):  # Pour chaque fréquence k
        for n in range(N):  # Pour chaque échantillon n
            theta = 2 * np.pi * k * n / N
            X[k] += signal[n] * (np.cos(theta) - 1j * np.sin(theta))  # e^{-j*theta}

    return X

# Fonction IDFT 1D
def idft(X):
    N = len(X)
    signal = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            theta = 2 * np.pi * k * n / N
            signal[k] += X[n] * (np.cos(theta) + 1j * np.sin(theta))
    return signal / N

#TODO DFT 2D
#TODO IDFT 2D

#TODO DFFT 1D
#TODO IDFFT 1D
#TODO DFFT 2D
#TODO IDFFT 2D

def calc_freq(N, dt):
    freqs = []
    for k in range(N):
        if k <= N // 2:
            freqs.append(k / (N * dt))  # Fréquences positives
        else:
            freqs.append(-(N - k) / (N * dt))  # Fréquences négatives
    return freqs



# Générer un signal simple (exemple : somme de sinusoïdes)
N = 500  # Nombre d'échantillons
deltaT = np.linspace(0, 1, N)
signal = np.sin(2 * np.pi * 50 * deltaT) + 0.5 * np.sin(2 * np.pi * 120 * deltaT)  # 50Hz et 120Hz

# Calcul de la DFT avec notre propre fonction
Xdft = dft(signal)

# Calcul de la fréquence associée
frequences = calc_freq(N, deltaT[1] - deltaT[0])

# Magnitude (amplitude)
magnitude = np.abs(Xdft)  # Amplitude (module)

# Reconstruction du signal avec la IDFT
signalIDFT = idft(Xdft)

# Visualisation
plt.figure(figsize=(12, 6))

# Afficher le signal d'origine
plt.subplot(3, 1, 1)
plt.plot(deltaT, signal)  # Représenter le signal temporel d'origine
plt.title('Signal d\'origine')
plt.xlabel('Temps (secondes)')
plt.ylabel('Amplitude')

# Afficher la magnitude
plt.subplot(3, 1, 2)
plt.plot(frequences[:N // 2], magnitude[:N // 2])  # Se concentrer sur les fréquences positives
plt.title('Magnitude du spectre de Fourier (implémentation DFT)')
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Amplitude')

# Afficher le signal d'origine recalculer avec la IDFT
plt.subplot(3, 1, 3)
plt.plot(deltaT, signalIDFT.real)  # Se concentrer sur les fréquences positives
plt.title('Signal après IDFT')
plt.xlabel('Temps (secondes)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
