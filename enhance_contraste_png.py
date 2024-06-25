import numpy as np
import os
import cv2

dossier_images = '/Users/macquentin/Desktop/Image_native_2/zsm/X'
dossier_contraste_test = os.path.join(dossier_images, 'tiff_augmentation_contraste')
os.makedirs(dossier_contraste_test, exist_ok=True)

# Valeurs fixes pour alpha et beta
alpha = 300
beta = 0
chemins_images_tiff = [os.path.join(dossier_images, fichier) for fichier in os.listdir(dossier_images) if fichier.lower().endswith('.tiff') or fichier.lower().endswith('.tif')]

for chemin_image_tiff in chemins_images_tiff:
    image = cv2.imread(chemin_image_tiff, cv2.IMREAD_UNCHANGED)
    if image is None:
        print(f"Impossible de lire l'image {chemin_image_tiff}.")
        continue
    
    image_contrast_adjusted = np.clip(image.astype(np.float32) * alpha + beta, 0, 65535).astype(np.uint16)
    image_inverse = cv2.bitwise_not(image_contrast_adjusted)
    nom_image_base = os.path.splitext(os.path.basename(chemin_image_tiff))[0]
    nom_fichier = f"{nom_image_base}_alpha_{alpha}_beta_{beta}_inverse.png"
    chemin_sauvegarde = os.path.join(dossier_contraste_test, nom_fichier)
    cv2.imwrite(chemin_sauvegarde, image_inverse)
    
    print(f"Image sauvegardée: {nom_fichier}")

print("Processus terminé.")
