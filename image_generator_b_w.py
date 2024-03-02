from PIL import Image
import random

# Dimensions de l'image
largeur = 150
nom_fichier="./out/test.txt"

with open(nom_fichier, 'rb') as fichier:
    # Lecture du contenu ou d'autres opérations sur le fichier si nécessaire
    contenu = fichier.read()
    taille_fichier = fichier.tell()
    print(taille_fichier)

image = Image.new("RGB", (largeur,taille_fichier//largeur+1), "white")
y=0
x=0
for i in contenu:
    x=x+1

    if x%largeur == 0:
        y=y+1
        x=0

    couleur=(i,i,i)
    #print(x,y,couleur)
    image.putpixel((x, y), couleur)
    #print(couleur)
    


# Enregistrement de l'image
image.save("./out/image_random00.png")

# Affichage de l'image (optionnel)

