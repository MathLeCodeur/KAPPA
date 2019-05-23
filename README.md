# KAPPA

## Installation

### Prérequis

- Installer `cmake`
- Installer `conda`

### Installation des librairies

```bash
conda env create -f env.yml
```

### Chargement initial des tags

Nécessaire seulement en cas de recréation de la base de données :

```bash
python src/init_databas.py
```

## Exécution

```bash
python src/main.py
```

Au premier lancement, aucune photo n'est contenue dans la base de données, il faut donc cliquer sur le bouton d'import d'un dossier d'image.
