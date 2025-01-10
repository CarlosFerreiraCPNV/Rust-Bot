# Bot Discord pour Rust : Guide des ressources et aide au recyclage

Bienvenue dans le projet **Rust Discord Bot !** Ce bot est conçu pour aider les joueurs du célèbre jeu de survie Rust en fournissant des informations rapides et précises sur :

- Les moyens de détruire des structures (par exemple, des murs en pierre) avec différentes méthodes.

- Les matériaux que vous obtiendrez en recyclant des objets spécifiques.

# Fonctionnalités
**Destruction de structures**

Avec une simple commande, le bot liste toutes les méthodes possibles pour détruire une structure dans Rust, telles que :

- Les explosifs nécessaires.
- La quantité de ressources (par exemple, soufre, fragments de métal) requise.
- Les estimations de temps pour chaque méthode.

**Informations sur le recyclage**

Le bot peut vous indiquer quels matériaux vous obtiendrez en recyclant des objets dans Rust. Par exemple :

- Les tuyaux métalliques donnent des fragments de métal et de la ferraille.
- Les engrenages fournissent du métal de haute qualité et de la ferraille.

#Commandes

**Préfixe général**

Le bot répond aux commandes commençant par "/". Vous pouvez personnaliser ce préfixe dans le fichier de configuration du bot.

**Exemples**
1. Vérifier les méthodes de destruction
   ```bash
    /raid [liste de structure] [nombre de structures]
  Résultat :
   ```bash
    Faire un RAID sur 1 Stone Wall
    Voici les éléments que vous pouvez utiliser pour détruire un mur en pierre :
    - 10 charges explosives artisanales
    - 3 roquettes
    - 2 explosifs C4
    - 500 coups de pioche
```
2. Vérifier les résultats du recyclage
   ```bash
   /recycle [liste d'items] [nombre d'items] [%]
   ```
   Résultat :
   ```bash
    Recyclage de 1 tuyau métallique (60% de rendement)
    En recyclant 1 tuyau métallique, vous obtiendrez :
    - 10 fragments de métal
    - 1 ferraille
   ```
   
3. Demander de l'aide
   ```bash
   /help
   ```
   Résultat :
   ```bash
   🔹 Commandes spécifiques
                          
   1. ```/raid```

   **Explique les moyens de détruire des structures (ex. murs en pierre, portes métalliques).**
                          
   *Exemple : /raid [structure] [nombre de structure à casser].*
                          
   2. ```/recycle```

   **Indique ce que vous pouvez obtenir en recyclant des objets spécifiques.**
                          
   *Exemple : /recycle [item] [nombre d'items à recycler] [pourcentage].*
                          
   3. ```/commands```

   **Affiche des commandes utiles.**
                          
   *Exemple : /commands.*
                          
   🔹 Besoin d'aide supplémentaire ?

   Si vous avez des questions ou rencontrez des problèmes, n'hésitez pas à demander à un       
   administrateur ou à consulter la documentation liée au bot.

   ```

4. Voir les commandes utiles
   ```bash
   🔸  Se suicider et respawn directement sur un bag, Idéal en cas de RAID pour réapparaître rapidement.
                          
   ```bind [KEY] kill;respawn_sleepingbag [ID]```
                          
   🔸  Zoomer, Permet d’augmenter temporairement votre champ de vision.
                          
   ```bind [KEY] "lookatradius 20;+fov 90;fov 70;lookatradius 0.01"```
                          
   🔸  Afficher des informations utiles dans la console, Active automatiquement des commandes pratiques à chaque             ouverture de la console.

   ```input.bind F1 client.consoletoggle; combatlog; client.ping```
   ```


# Installation

**Prérequis**

- Python 3.8+
- Bibliothèque Discord.py

**Instructions**

1. Clonez le dépôt
   ```bash
    git clone https://github.com/CarlosFerreiraCPNV/Rust-Bot
   ```
2. Installez les dépendances

3. Modifier la variable bot_token dans le fichier TOKEN.py avec le token de votre bot Discord :
   ```bash
    bot_token=votre_token_bot_ici
   ```
4. python bot.py
   ```bash
    python bot.py
   ```
