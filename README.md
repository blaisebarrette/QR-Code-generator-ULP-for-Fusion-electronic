# QR Code Generator ULP for Eagle/Fusion Electronics

Ce plugin permet de générer des QR codes directement sur les layers de votre PCB dans Eagle/Fusion Electronics.

## Fonctionnalités

- Génération de QR code à partir d'une URL
- Placement direct sur le layer de votre choix (tSilk par défaut)
- Dimension personnalisable en mils
- Interface simple d'utilisation

## Installation

1. Copiez le fichier `qrcode_generator.ulp` dans votre dossier ULP d'Eagle
2. Copiez également le fichier `qrencode.h` dans le même dossier

## Utilisation

1. Dans Eagle/Fusion Electronics, ouvrez votre design de PCB
2. Exécutez le script via la commande : `RUN qrcode_generator.ulp`
3. Dans la fenêtre qui s'ouvre :
   - Entrez l'URL souhaitée
   - Ajustez la taille (en mils)
   - Sélectionnez le layer de destination
4. Cliquez sur OK pour générer le QR code

## Notes

- La taille par défaut est de 1000 mils
- Le layer par défaut est tSilk (top silkscreen)
- Le QR code est généré en éléments de dessin vectoriels 