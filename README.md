# CTRLtek Live

Site statique one-page pour CTRLtek Live.

## Publication GitHub Pages

1. Créer un dépôt GitHub public, par exemple `ctrltek-live`.
2. Ajouter les fichiers de ce dossier à la branche `main`.
3. Dans GitHub, ouvrir `Settings` puis `Pages`.
4. Choisir `Deploy from a branch`, branche `main`, dossier `/root`.
5. Vérifier que le fichier `CNAME` contient `ctrltek.live`.
6. Dans `Settings` puis `Pages`, confirmer le domaine personnalisé `ctrltek.live`.
7. Activer `Enforce HTTPS` une fois le certificat disponible.

## DNS IONOS à préparer

Ne modifier les DNS qu'après confirmation explicite.

Pour le domaine racine `ctrltek.live`, ajouter ou vérifier ces enregistrements A :

```text
@  A  185.199.108.153
@  A  185.199.109.153
@  A  185.199.110.153
@  A  185.199.111.153
```

Pour `www.ctrltek.live`, ajouter :

```text
www  CNAME  <utilisateur-github>.github.io
```

Remplacer `<utilisateur-github>` par le compte ou l'organisation GitHub qui possède le dépôt.

## Décisions

- Site statique gratuit compatible GitHub Pages.
- Domaine personnalisé prévu : `ctrltek.live`.
- Founder affiché : IssamFire uniquement.
- Aucun candidat n'est présenté comme membre tant qu'il n'a pas accepté.
