import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

"""
-----------------------------------------------------
Algorithme Transformé de fourier 2D normal et inverse
-----------------------------------------------------
"""

# +++++++++++++++++++++ IMPORTANT +++++++++++++++++++++
def dft2d(image):
    M, N = image.shape  # Dimensions de l'image
    X = np.zeros((M, N), dtype=complex)  # Matrice pour stocker les coefficients de la DFT

    # Calcul de la DFT 2D
    for k in range(M):  # Fréquence selon l'axe des lignes
        for l in range(N):  # Fréquence selon l'axe des colonnes
            sum_val = 0  # Initialiser la somme pour chaque coefficient (k, l)
            for m in range(M):  # Pour chaque pixel (m, n) dans l'image
                for n in range(N):
                    theta = 2 * np.pi * ((k * m / M) + (l * n / N))
                    sum_val += image[m, n] * (np.cos(theta) - 1j * np.sin(theta))
            X[k, l] = sum_val

    return X

def idft2d(X):
    M, N = X.shape  # Dimensions de l'image
    image_reconstructed = np.zeros((M, N), dtype=complex)

    # Calcul de l'IDFT 2D
    for m in range(M):  # Position spatiale selon l'axe des lignes
        for n in range(N):  # Position spatiale selon l'axe des colonnes
            sum_val = 0  # Initialiser la somme pour chaque pixel (m, n)
            for k in range(M):  # Pour chaque coefficient fréquentiel (k, l)
                for l in range(N):
                    theta = 2 * np.pi * ((k * m / M) + (l * n / N))
                    sum_val += X[k, l] * (np.cos(theta) + 1j * np.sin(theta))
            image_reconstructed[m, n] = sum_val

    return image_reconstructed / (M * N)  # Normalisation

# Charge une image depuis un fichier
def load_image(filepath):
    image = Image.open(filepath).convert('L')
    image = image.resize((64, 64))
    return np.array(image)

image = load_image("./img.png")

X_dft2d = dft2d(image)

image_reconstructed = idft2d(X_dft2d)

magnitude = np.abs(X_dft2d)

plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Image originale')
plt.colorbar()

# Afficher la magnitude du spectre de Fourier
plt.subplot(1, 3, 2)
plt.imshow(np.log(1 + magnitude), cmap='gray')  # Utiliser le logarithme pour mieux visualiser
plt.title('Magnitude du spectre de Fourier (DFT 2D)')
plt.colorbar()

# Afficher l'image reconstruite après IDFT
plt.subplot(1, 3, 3)
plt.imshow(image_reconstructed.real, cmap='gray')  # Prendre la partie réelle
plt.title('Image reconstruite après IDFT')
plt.colorbar()

plt.tight_layout()
plt.show()