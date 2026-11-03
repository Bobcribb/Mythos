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
