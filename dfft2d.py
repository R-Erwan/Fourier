import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

"""
-----------------------------------------------------
Algorithme Transformé de fourier RAPIDE 2D normal et inverse
-----------------------------------------------------
"""

def fft2d(image):
    M, N = image.shape
    # Appliquer la FFT 1D sur chaque ligne
    fft_rows = np.zeros((M, N), dtype=complex)
    for i in range(M):
        fft_rows[i, :] = fft1d(image[i, :])

    # Appliquer la FFT 1D sur chaque colonne (sur le résultat précédent)
    fft_cols = np.zeros((M, N), dtype=complex)
    for j in range(N):
        fft_cols[:, j] = fft1d(fft_rows[:, j])

    return fft_cols

def ifft2d(X):
    M, N = X.shape
    # Appliquer l'IFFT 1D sur chaque colonne
    ifft_cols = np.zeros((M, N), dtype=complex)
    for j in range(N):
        ifft_cols[:, j] = ifft1d(X[:, j])

    # Appliquer l'IFFT 1D sur chaque ligne (sur le résultat précédent)
    ifft_rows = np.zeros((M, N), dtype=complex)
    for i in range(M):
        ifft_rows[i, :] = ifft1d(ifft_cols[i, :])

    return ifft_rows

# Implémentation de la FFT 1D
def fft1d(signal):
    N = len(signal)
    if N <= 1:
        return signal  # Cas de base

    # Séparer les termes pairs et impairs
    even_terms = fft1d(signal[0::2])
    odd_terms = fft1d(signal[1::2])

    # Calculer la combinaison des termes pairs et impairs
    X = np.zeros(N, dtype=complex)
    for k in range(N // 2):
        t = np.exp(-2j * np.pi * k / N) * odd_terms[k]  # Facteur de rotation (Twiddle factor)
        X[k] = even_terms[k] + t
        X[k + N // 2] = even_terms[k] - t

    return X

# Implémentation de l'IFFT 1D
def ifft1d(X):
    N = len(X)
    if N <= 1:
        return X  # Cas de base

    # Séparer les termes pairs et impairs
    even_terms = ifft1d(X[0::2])
    odd_terms = ifft1d(X[1::2])

    # Calculer la combinaison des termes pairs et impairs
    signalR = np.zeros(N, dtype=complex)
    for k in range(N // 2):
        t = np.exp(2j * np.pi * k / N) * odd_terms[k]  # Facteur de rotation (Twiddle factor, signe opposé)
        signalR[k] = even_terms[k] + t
        signalR[k + N // 2] = even_terms[k] - t

    return signalR / 2  # Normalisation

# Chargement d'une image
def load_image(filepath):
    image = Image.open(filepath).convert('L')  # Convertir en niveaux de gris
    return np.array(image)

# Exemple d'utilisation
image = load_image("./img.png")

# Appliquer la FFT 2D
X_fft2d = fft2d(image)

# Magnitude du spectre de Fourier
magnitude = np.abs(X_fft2d)

# Appliquer l'IFFT 2D pour reconstruire l'image
image_reconstructed = ifft2d(X_fft2d)

# Affichage des résultats
plt.figure(figsize=(12, 6))

# Image originale
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Image originale')
plt.colorbar()

# Spectre de Fourier (magnitude)
plt.subplot(1, 3, 2)
plt.imshow(np.log(1 + magnitude), cmap='gray')  # Utiliser le logarithme pour mieux visualiser
plt.title('Magnitude du spectre de Fourier (FFT 2D)')
plt.colorbar()

# Image reconstruite après IFFT
plt.subplot(1, 3, 3)
plt.imshow(image_reconstructed.real, cmap='gray')
plt.title('Image reconstruite après IFFT 2D')
plt.colorbar()

plt.tight_layout()
plt.show()
