# QR Code Generator ULP for Fusion Electronics

Un outil simple et efficace pour générer des QR codes directement dans Eagle/Fusion360 Electronics.

## Caractéristiques

- Génération de QR codes à partir d'URLs
- Placement automatique intelligent sur le PCB
- Support de plusieurs couches (Silkscreen, Documentation)
- Taille personnalisable (250-5000 mils)
- Positionnement manuel possible avec coordonnées X,Y
- Aucune installation locale requise

## Installation

1. Téléchargez le fichier `qrcode_generator.ulp`
2. Placez-le dans un dossier accessible

C'est tout ! Pas besoin d'installer Python ou d'autres dépendances.

## Utilisation

1. Dans Eagle/Fusion360 Electronics, ouvrez votre design PCB
2. Exécutez le script ULP :
   - Dans Eagle : `File > Run ULP > qrcode_generator.ulp`
   - Dans Fusion360 : `Tools > Run ULP > qrcode_generator.ulp`

3. Dans la fenêtre qui s'ouvre :
   - Entrez l'URL pour votre QR code
   - Choisissez la taille (en mils)
   - Sélectionnez la couche de destination
   - La position par défaut sera calculée automatiquement
   - Vous pouvez ajuster la position manuellement si nécessaire

4. Cliquez sur OK pour générer le QR code

## Couches Supportées

- Top Silkscreen (tPlace)
- Bottom Silkscreen (bPlace)
- Top Documentation (tDocu)

## Position Automatique

Le QR code est automatiquement positionné pour éviter les conflits avec votre design :
- Position par défaut = -(taille + 1000) en X et Y
- Exemple : Pour un QR code de 500 mils, position = -1500,-1500
- Cette position peut être ajustée avec le bouton "Update Position"

## Notes Techniques

- Le QR code est généré via un service cloud sécurisé
- Taille minimale : 250 mils
- Taille maximale : 5000 mils
- Plage de positionnement : -50000 à +50000 mils

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer des améliorations
- Soumettre des pull requests

## Licence

Ce projet est sous licence MIT.

## Auteurs

- Blaise Barrette - Conception et développement initial
- Avec l'aide de l'équipe Cursor AI