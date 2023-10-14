# Convertisseur d'image en Art ASCII

Ce script Python utilise la bibliothèque PIL (Python Imaging Library) pour convertir une image en art ASCII. L'art ASCII est une représentation graphique d'une image à l'aide de caractères ASCII de différentes nuances de gris.

## Prérequis

Assurez-vous d'avoir Python installé sur votre système.
Installez également la bibliothèque PIL (Python Imaging Library) en utilisant la commande suivante :
pip install pillow

## Utilisation

1. Placez l'image que vous souhaitez convertir dans le dossier `input/`.

2. Exécutez le script `gen_ascii.py`.

3. Suivez les instructions pour entrer le nom de l'image (sans l'extension) et l'extension du fichier image.

4. Le script générera un fichier texte ASCII dans le dossier `output/` avec le même nom que l'image d'origine.

## Résultats

Le script convertit l'image en niveaux de gris en utilisant la formule de luminance et remplace les niveaux de gris par des caractères ASCII correspondants. Les caractères ASCII sont utilisés pour représenter différentes nuances de gris, créant ainsi une version artistique de l'image d'origine.
