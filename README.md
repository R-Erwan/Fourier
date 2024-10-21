# DFT Algorithme de la transformé de Fourier discrète 1D
G[u] = ∑ g[x] * e( -2iπux / N ) avec u = 0..N-1

ou grace a la FORMULE D'EULER

**e(−iθ) = cos(θ) − i * sin(θ)**

**e(iθ) = cos(θ) + i * sin(θ)**

G[u] = ∑ g[x] * ( cos( 2πux / N) - i * sin( 2πux / N) ) avec u = 0..N-1

- g[x] est l'échantillon du signal d'entré a l'indice x
- G[u] est le coefficient de la DFT a la fréquence discrète u
- N est la taille de l'échantillon
- i nombre imaginaire
- e(-2ieπux) facteur de rotation complexe

## Algo en pseudo-code :
Entré : un tableau de signal g[n] de longeur N

1. Initialisé un tableau G[u] de longeur N pour stocker les résultats de la DFT
2. Pour chaque fréquence u de 0 a N-1 :
   - Initialisé G[u] = 0 (coeff fréquentiel)
   - Pour chaque échantillon x de 0 a N-1 :
     - Calculer l'angle θ 2πux / N
     - Mettre a jour G[u] en ajoutant g[x] * exp(-i θ) * (cos(θ - i * sin(θ)))

     ***QUESTION Pourquoi on a du cos et du sin ?***
     ***REPONSE Formule d'EULER***

   - Le résultat pour cette fréquence u est calculé
3. Retourner le tableau G[u] contenant les coefficients de la DFT

## IDFT Algo de la transformé de fourier inverse 1D

Penser a normalisé le signal pour obtenir la signal dans le domaine temporel. Car la DFT est une somme
discrète de N termes, donc il faut rammener les coeff a la bonne échelle lors de l'inversion.

***QUESTION : Pourquoi on doit normalisé ? REPONSE :*** 




# Calcul des fréquences associées à la DFT

La **transformée de Fourier discrète (DFT)** permet de transformer un signal temporel en un signal dans le domaine fréquentiel. Voici comment calculer les fréquences associées à chaque coefficient de la DFT.

## Principe général

Lorsque votre signal est échantillonné avec un certain intervalle de temps \( dt \), les fréquences associées aux points du domaine fréquentiel peuvent être calculées à partir de ces principes :

1. **Nombre de points de la DFT** : La DFT génère \( N \) points, où \( N \) est le nombre d'échantillons dans le signal d'origine.

2. **Fréquence de Nyquist** : La fréquence maximale représentée est la **fréquence de Nyquist** :
   \[
   f_{\text{max}} = \frac{1}{2 \cdot dt}
   \]
   Cette fréquence correspond à la moitié de la fréquence d'échantillonnage et est la plus haute fréquence observable dans votre signal.

3. **Espacement des fréquences** : Les fréquences sont espacées de :
   \[
   \Delta f = \frac{1}{N \cdot dt}
   \]
   La première fréquence (à \( k = 0 \)) est toujours 0 Hz (la composante continue ou "DC").

4. **Fréquences positives et négatives** : 
   - Les **fréquences positives** vont de 0 à \( f_{\text{max}} \).
   - Les **fréquences négatives** apparaissent après, du côté supérieur de la transformée, représentant des fréquences au-delà de la fréquence de Nyquist.

## Algorithme manuel pour calculer les fréquences

Les fréquences associées à chaque indice \( k \) dans le domaine fréquentiel sont calculées ainsi :

\[
f_k = \frac{k}{N \cdot dt} \quad \text{pour} \, k = 0, 1, 2, \dots, N-1
\]

### Paramètres :
- \( N \) est le nombre d'échantillons.
- \( dt \) est la durée entre deux échantillons (la période d'échantillonnage).
- \( f_k \) est la fréquence associée au coefficient \( k \).

### Gestion des fréquences négatives :
Lorsque \( k > \frac{N}{2} \), les fréquences sont négatives, car elles représentent les composantes au-delà de la fréquence de Nyquist.

Ces fréquences peuvent être recalculées comme suit pour les indices \( k \) supérieurs à \( N/2 \) :

\[
f_k = - \frac{N-k}{N \cdot dt}
\]

Cela permet d'obtenir les **fréquences négatives** dans la seconde moitié de la transformée, ce qui est particulièrement pertinent pour les signaux réels qui produisent des spectres symétriques.
