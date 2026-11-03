# Théâtre grec — Registre des intégrations contrôlées

## 3 novembre 2026 — Daidalos, dossier TH-COM-DAI

### Source et statut antérieur

Source intégralement lue : `Bobcribb/Bobcribb.github.io`, `chapitres/comedies/volume-026-aristophane-daidalos.md`, version `f865cd391413301f9f2788c2caf4026c257a28c4`.

Ce manuscrit existait déjà dans le dépôt historique. Il s'agit d'une **nouvelle intégration dans Bobcribb/Mythos**, non d'une nouvelle rédaction ni de la découverte d'un texte antique. Avant cette intégration, la rubrique `theatre-grec.html` de Mythos ne proposait que des entrées d'inventaire ; aucune page Daidalos n'y était présente.

Archive locale exacte : [daidalos-source.md](comedies/daidalos-source.md). Taille : **18 594 octets, 18 028 caractères, 202 lignes**. Empreinte Git de la source originale et de la copie : **7e700ab6e72f26208e47d6e3eb600e41f95af78c**. SHA-256 : `a60bd8b676b534e3ff444823112f50acd04847905a671575b191e7dc1966f4c1`.

### Classement sans mélange des genres

- **TH-03-DAI — Étude critique** : sections I–XVII, XXI–XXII ; 19 sections, dont le bilan et la bibliographie. Lecture : `comedies/daidalos-etude.html`.
- **TH-02-DAI — Scènes modernes** : sections XVIII–XX ; trois créations contemporaines explicitement signalées comme non antiques. Lecture : `comedies/daidalos-scenes-modernes.html`.

Les 22 sections et le préambule sont conservés sans résumé. Une comparaison locale indépendante avec MarkdownIt et BeautifulSoup a confirmé l'identité de tous les textes lisibles de section : **22/22**. Le classement du site ne remplace pas les numéros historiques, conservés comme métadonnées de provenance. Les deux parcours ont des liens réciproques ; la bibliographie reste unique dans l'étude.

### Publication reproductible

`python3 scripts/build-daidalos.py` produit les deux pages HTML statiques et `daidalos-controle.json` dans le répertoire des sources, avant l'envoi de l'artefact GitHub Pages. **Les pages sont générées au déploiement** : le texte maître est le Markdown versionné, jamais une copie abrégée. Le script ne dépend ni du réseau ni de bibliothèques tierces. Une empreinte source inattendue, une section absente, un mauvais classement [C] ou une ancre locale manquante bloque la génération.

Les entrées Théâtre et Philosophie renvoient au même dossier. L'étude est classée parmi les analyses liées aux pièces, pas parmi les études philosophiques autonomes. Le sommaire général préexistant ouvre déjà la rubrique Théâtre ; chaque lecteur retourne également au sommaire général.

### Graphisme et contrôles

Nouveau lecteur noir et or, motif existant `assets/mythos-hero.svg` (statue stylisée à gauche, temple à droite), deux cartes illustrées, sommaire repliable, repères de focus, largeur de lecture limitée et styles d'impression. Les motifs sont décoratifs, **pas des restitutions archéologiques**.

Rendus locaux inspectés en Chromium à 360, 390, 768 et 1 440 pixels, sur les deux pages : huit tests sans débordement horizontal. Les ressources locales ont été incorporées au document de test afin de ne pas utiliser de réseau ; ce contrôle ne prouve pas l'affichage du domaine public.

### Limites explicites

Le contrôle établit la fidélité au manuscrit et sa répartition, pas une validation scientifique exhaustive. Les réserves du manuscrit sur la collation des fragments et l'interprétation moderne sont conservées. Aucune nouvelle scène n'a été inventée pendant cette intégration. Le succès du déploiement doit être vérifié séparément dans GitHub Actions ; l'accès indépendant à bobmythos.fr n'est pas certifié par ce registre.

Les tomes des Origines du sacré déjà intégrés, tous les anciens textes et toutes les archives demeurent inchangés. Aucun autre dépôt n'a été modifié. Aucune programmation horaire MYTHOS n'a été changée.

## 3 novembre 2026 — Polyidos, dossier TH-COM-POL

### Source et conservation

Source : `Bobcribb/Bobcribb.github.io`, `chapitres/comedies/volume-025-aristophane-polyidos.md`, version `fafe12416fc918d2576116cd0a4e0a9a2836ee11`. Manuscrit préexistant, absent de la collection Théâtre du dépôt cible lors du contrôle ; nouvelle intégration dans Mythos, non nouvelle rédaction.

[Manuscrit source intégral](comedies/polyidos-source.md) : **16 288 octets, 15 806 caractères, 165 lignes, 19 sections**. Empreinte Git originale et copie : `46c2cd20c5d797aee436bd83b429a8ffeef0e76b`. SHA-256 : `02e0491573f1f495cf993124f5bf45a7b564c776368ff09de37bc19df53885e2`.

### Lectures et classement

- **TH-03-POL** : [étude critique](comedies/polyidos-etude.html), sections I–XIII et XVII–XIX, soit 16 sections, préambule, bibliographie et conclusion conservés.
- **TH-02-POL** : [scènes modernes](comedies/polyidos-scenes-modernes.html), sections XIV–XVI, soit trois dialogues contemporains expressément non antiques.

Aucune section n'est abrégée, omise ou publiée deux fois dans les lecteurs. Les repères du volume source XXV sont conservés. La copie Markdown contient aussi le front matter et les liens historiques originaux. Les URL de navigation sont adaptées uniquement dans le rendu, avec renvoi aux archives historiques pour les dossiers non transférés.

### Génération, navigation et graphisme

`python3 scripts/build-polyidos.py`, après `build-daidalos.py`, génère les deux lecteurs et le rapport technique. Il insère les cartes dans Théâtre, le renvoi dans Philosophie parmi les analyses liées aux pièces, l'entrée au sommaire général et les liens réciproques depuis Daidalos. Ces ajouts sont produits dans l'artefact Pages : les sources HTML préexistantes restent conservées dans Git. Une seconde génération ne crée aucun doublon.

Bandeau noir et or avec le SVG existant (statue stylisée à gauche, temple à droite), cartes illustrées décoratives, raccourcis vers texte/bibliographie/source, sommaire repliable et zones de navigation tactile d'au moins 44 pixels dans le lecteur. Aucun visuel n'est présenté comme une reconstitution archéologique.

### Contrôles et limites

Comparaison indépendante locale avec MarkdownIt et BeautifulSoup : **19 sections sur 19 et préambule identiques en texte lisible**. Empreinte source exacte, séparation des trois sections [C], ancres, absence de doublons et idempotence contrôlées. Huit essais Chromium sur les deux lecteurs, à 360, 390, 768 et 1 440 pixels : aucun débordement horizontal, premier lien du sommaire fonctionnel. [Résultats locaux](comedies/polyidos-verifications-locales.json).

Les essais locaux incorporent les CSS et le SVG exacts du dépôt ; les pages de destination hors lecteurs sont des fixtures locales et ne prouvent pas le déploiement. GitHub Actions vérifie séparément les vrais fichiers de destination et les ancres, puis publie l'artefact. Le rapport `comedies/polyidos-controle.json` est généré à cette étape. La comparaison de texte ne constitue pas une collation scientifique exhaustive des fragments. La disponibilité du domaine public doit être confirmée indépendamment du succès de Pages.

Toutes les archives précédentes restent conservées. Aucun autre dépôt ni aucune programmation MYTHOS n'a été modifié.
