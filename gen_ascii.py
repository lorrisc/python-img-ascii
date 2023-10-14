from PIL import Image

# Définir le dossier et le nom de l'image
dossier = "input/"
nom_image = input("Entrez le nom de l'image : ")
nom_image_ext = input("Entrez l'extention' : ")
chemin = dossier + nom_image + '.' + nom_image_ext

# Ouvrir l'image
img = Image.open(chemin)
largeur, hauteur = img.size

# Obtenir les pixels
pixels = []
for y in range(hauteur):
    ligne_pixels = []
    for x in range(largeur):
        ligne_pixels.append(img.getpixel((x, y)))
    pixels.append(ligne_pixels)

# Calculer la luminance et créer la représentation ASCII
ascii_art = []
for ligne in pixels:
    ligne_ascii = []
    for pixel in ligne:
        luminance = 0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2]
        ligne_ascii.append(luminance)
    ascii_art.append(ligne_ascii)

# Écrire le fichier texte ASCII
with open('output/' + nom_image + '.txt', 'w') as fichier:
    for ligne_ascii in ascii_art:
        for luminance in ligne_ascii:
            if luminance < 25:
                fichier.write("@")
            elif luminance < 50:
                fichier.write("%")
            elif luminance < 75:
                fichier.write("#")
            elif luminance < 100:
                fichier.write("*")
            elif luminance < 125:
                fichier.write("+")
            elif luminance < 150:
                fichier.write("=")
            elif luminance < 175:
                fichier.write("-")
            elif luminance < 200:
                fichier.write(":")
            elif luminance < 225:
                fichier.write(".")
            else:
                fichier.write(" ")
        fichier.write("\n")

print("Fichier texte ASCII créé avec succès!")
