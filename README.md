# CTRLtek Live

Site statique one-page pour CTRLtek Live.

## Publication GitHub Pages

1. Créer un dépôt GitHub public, par exemple `ctrltek-live`.
2. Ajouter les fichiers de ce dossier à la branche `main`.
3. Dans GitHub, ouvrir `Settings` puis `Pages`.
4. Choisir `GitHub Actions` comme source de déploiement pour le workflow de collaborations.
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

## Collaborations Trello → site

Tableau : https://trello.com/b/P1ctZHx1/collabs-artist-ctrlteklive

Chaque carte est un **projet musical**, pas une fiche artiste. Dupliquer la carte « MODÈLE — Projet de collaboration » et remplir ses champs. Le pipeline actif est : Idées / à qualifier → En création → Mixage / mastering → À valider pour le site → Publié sur CTRLtek.live. Les anciennes listes de production vides ont été archivées (elles restent récupérables).

Pour publier : renseigner le titre public, les artistes, les résumés FR et EN, indiquer `Accord de publication obtenu auprès des artistes : Oui`, puis déplacer la carte dans « Publié sur CTRLtek.live ». Le visuel et l'écoute sont facultatifs mais doivent être des liens HTTPS publics. Une carte incomplète reste invisible. Les chemins Windows, liens privés et notes de production ne sont jamais exportés.

Le script `scripts/sync_trello.py` écrit uniquement les champs publics dans `data/collaborations.json`. Le site affiche les projets dans les sections FR et EN. Le workflow `.github/workflows/sync-collaborations.yml` synchronise chaque heure et déploie par GitHub Pages. Pour l'activer, créer les **secrets Actions du dépôt** `TRELLO_API_KEY` et `TRELLO_TOKEN` sous Settings → Secrets and variables → Actions, ajouter la variable Actions `TRELLO_SYNC_ENABLED` avec la valeur `true`, puis sélectionner **GitHub Actions** comme source dans Settings → Pages. Tant que la variable n'est pas `true`, les exécutions planifiées et manuelles sont ignorées. Utiliser une clé et un jeton Trello ayant seulement l'accès nécessaire ; ne jamais les mettre dans les cartes, le site ou Git. Lancer une première fois le workflow via Actions → Publish approved collaborations → Run workflow afin de vérifier la connexion et le domaine. Si ces secrets manquent, le workflow échoue clairement sans remplacer les données publiques.
