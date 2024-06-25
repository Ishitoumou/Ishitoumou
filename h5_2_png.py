""""
center of diffraction pattern with friedel pair.
this code is on three part
This is the part-I 
Convert h5_2_png file
"""

import os
import h5py
from PIL import Image


def ouvrir_fichier(chemin):
    with h5py.File(chemin, 'r') as fichier_h5:
        donnees = fichier_h5['data_01/rawdata'][:]
    return donnees

def sauv(chemin, donnees):
    nom_fichier = os.path.basename(chemin)  # Extraire le nom du fichier sans le chemin
    nom_sans_extension = os.path.splitext(nom_fichier)[0]
    chemin_sortie = os.path.join(os.path.dirname(chemin), f"{nom_sans_extension}.tiff")  # Utilisation de l'extension .tiff
    image = Image.fromarray(donnees.astype('uint16'))
    image.save(chemin_sortie)


# Répertoire contenant les fichiers .h5 à convertir
repertoire = '/Users/macquentin/Desktop/Image_native_2/zsm/'

# Liste tous les fichiers dans le répertoire
fichiers = os.listdir(repertoire)

# Filtre pour ne garder que les fichiers .h5
fichiers_h5 = [f for f in fichiers if f.endswith('.h5')]

# Boucle sur chaque fichier .h5 trouvé
for fichier_h5 in fichiers_h5:
    chemin_complet = os.path.join(repertoire, fichier_h5)
    donnees = ouvrir_fichier(chemin_complet)
    sauv(chemin_complet, donnees)
    print(f"Conversion de {fichier_h5} terminée.")
