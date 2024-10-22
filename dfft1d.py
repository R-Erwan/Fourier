import numpy as np
import matplotlib.pyplot as plt

"""
-----------------------------------------------------
Algorithme Transformé de fourier RAPIDE 1D normal et inverse
-----------------------------------------------------
"""

def fft1d(signal):
    N = len(signal)
    if N <= 1:
        return signal  # Cas de base pour la récursion

    # Séparer les termes pairs et impairs
    even_terms = fft1d(signal[0::2])
    odd_terms = fft1d(signal[1::2])

    # Combiner les termes pairs et impairs
    X = np.zeros(N, dtype=complex)
    for k in range(N // 2):
        t = np.exp(-2j * np.pi * k / N) * odd_terms[k]  # Twiddle factor
        X[k] = even_terms[k] + t
        X[k + N // 2] = even_terms[k] - t

    return X


def ifft1d(X):
    N = len(X)
    if N <= 1:
        return X  # Cas de base pour la récursion

    # Séparer les termes pairs et impairs
    even_terms = ifft1d(X[0::2])
    odd_terms = ifft1d(X[1::2])

    # Combiner les termes pairs et impairs
    signalR = np.zeros(N, dtype=complex)
    for k in range(N // 2):
        t = np.exp(2j * np.pi * k / N) * odd_terms[k]  # Twiddle factor (note le signe positif)
        signalR[k] = even_terms[k] + t
        signalR[k + N // 2] = even_terms[k] - t

    return signalR / N  # Normalisation

# Calculer les fréquences pour le spectre
def calc_freq(N, dt):
    freqs = []
    for k in range(N):
        if k <= N // 2:
            freqs.append(k / (N * dt))  # Fréquences positives
        else:
            freqs.append(-(N - k) / (N * dt))  # Fréquences négatives
    return freqs


# Générer un signal simple (exemple : somme de sinusoïdes)
N = 512  # Nombre d'échantillons puissance de 2
deltaT = np.linspace(0, 1, N)
signal = np.sin(2 * np.pi * 50 * deltaT) + 0.5 * np.sin(2 * np.pi * 120 * deltaT)  # 50Hz et 120Hz

Xfft= fft1d(signal) # Calcul de la DFT avec notre propre fonction
frequences = calc_freq(N, deltaT[1] - deltaT[0]) # Calcul de la fréquence associée
magnitude = np.abs(Xfft)  # Amplitude (module)
signalIFFT = ifft1d(Xfft) # Reconstruction du signal avec la ifft

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
plt.plot(deltaT, signalIFFT.real)  # Se concentrer sur les fréquences positives
plt.title('Signal après IDFT')
plt.xlabel('Temps (secondes)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
