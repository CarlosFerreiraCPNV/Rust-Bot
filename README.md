# Bot Discord pour Rust : Guide des ressources et aide au recyclage

Bienvenue dans le projet **Rust Discord Bot !** Ce bot est conçu pour aider les joueurs du célèbre jeu de survie Rust en fournissant des informations rapides et précises sur :

- Les moyens de détruire des structures (par exemple, des murs en pierre) avec différentes méthodes.

- Les matériaux que vous obtiendrez en recyclant des objets spécifiques.

# Fonctionnalités
**Destruction de structures**

Avec une simple commande, le bot liste toutes les méthodes possibles pour détruire une structure dans Rust, telles que :

- Les outils, armes ou explosifs nécessaires.
- La quantité de ressources (par exemple, soufre, fragments de métal) requise.
- Les estimations de temps pour chaque méthode.

**Informations sur le recyclage**

Le bot peut vous indiquer quels matériaux vous obtiendrez en recyclant des objets dans Rust. Par exemple :

- Les tuyaux métalliques donnent des fragments de métal et de la ferraille.
- Les engrenages fournissent du métal de haute qualité et de la ferraille.

#Commandes

**Préfixe général**

Le bot répond aux commandes commençant par !rust. Vous pouvez personnaliser ce préfixe dans le fichier de configuration du bot.

**Exemples**
1. Vérifier les méthodes de destruction
   ```bash
    !rust destroy stone wall
  Résultat :
   ```bash
    Pour détruire un mur en pierre, vous pouvez utiliser :
    - 10 charges explosives artisanales
    - 3 roquettes
    - 2 explosifs C4
    - 500 coups de pioche
```
2. Vérifier les résultats du recyclage
   ```bash
   !rust destroy stone wall !rust recycle metal pipe
   ```
   Résultat :
   ```bash
    Recycler un tuyau métallique donne :
    - 10 fragments de métal
    - 1 ferraille
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
   ```bash
    pip install -r requirements.txt
   ```
3. Créez un fichier .env avec le token de votre bot Discord :
   ```bash
    DISCORD_TOKEN=votre_token_bot_ici
   ```
4. python bot.py
   ```bash
    python bot.py
   ```
