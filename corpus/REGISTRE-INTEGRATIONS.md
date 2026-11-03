# MYTHOS — Registre des intégrations contrôlées

Ce registre sert à éviter les doublons et à distinguer les contenus effectivement présents sur GitHub des manuscrits uniquement signalés en conversation ou en Bibliothèque. Une intégration est validée ici uniquement lorsque le texte de la source a été lu intégralement, que la comparaison du texte nettoyé est concluante et que les pages et sommaires ont été reliés.

## 3 novembre 2026 — Migration des monographies

| Cote | Titre | Manuscrit d'origine | Page publiée | Contrôle de reprise |
|---|---|---|---|---|
| MG-02.A | Aphrodite — monographie universitaire intégrale | `MYTHOS-aphrodite-2026-10-28.md` (Bibliothèque) | [Dossier Aphrodite](mythologie-grecque/02-dieux-et-divinites/aphrodite-etude-integrale.html) | Correspondance exacte du texte lisible : 19 755 caractères après suppression des commentaires de blocs WordPress et ajout des ancres de navigation. Bibliographie et exercices conservés. |
| CIV-01 | Perse et Iran ancien — étude de Behistun | `MYTHOS-perse-iran-ancien-2026-10-28.md` (Bibliothèque) | [Dossier Perse et Iran](civilisations/perse-iran-ancien-behistun.html) | Correspondance exacte du texte lisible : 16 929 caractères ; seuls les commentaires Gutenberg et deux chemins internes obsolètes ont été adaptés. Bibliographie et exercices conservés. |

Ces deux pages sont aussi reliées depuis les sommaires thématiques et le sommaire général ; Aphrodite est indexée dans la rubrique Philosophie par une **ancre vers sa propre étude**, sans copie supplémentaire du texte. Les métadonnées de provenance sont conservées dans les pages publiées.

### Portée du contrôle

Le contrôle porte sur **l'intégrité textuelle et la navigation**, non sur la vérification scientifique exhaustive. Les citations anciennes, références, attributions et droits d'illustration exigent une révision savante distincte. Aucune autre section annoncée dans les conversations n'est considérée comme transférée par le présent registre.

### Règles pour les prochaines intégrations

1. Chercher d'abord si la source figure dans ce registre, puis si elle existe déjà dans l'arborescence GitHub.
2. Lire le manuscrit intégral et vérifier le début, la fin, les sources et la bibliographie avant de créer une page.
3. Conserver le texte et son schéma de numérotation d'origine ; créer une cote éditoriale explicite plutôt qu'une renumérotation arbitraire.
4. Ajouter sommaire, références croisées et lien de retour, sans recopier le même contenu sur plusieurs pages.
5. Comparer la version publiée au manuscrit, contrôler l'absence de liens locaux manquants et compléter ce registre uniquement en cas de succès.


## Contrôle du 3 novembre 2026 — exécution suivante

**Inventaire réellement inspecté :** racine du dépôt, `contenus/philosophie/`, `corpus/`, `corpus/mythologie-grecque/`, le registre des récupérations et le sommaire général.

- **Aucun nouveau manuscrit intégral publié lors de cette exécution.** Le document [Homère et Hésiode](../contenus/philosophie/homere-hesiode-dossier-preparatoire.md) est explicitement un *dossier éditorial de préparation*, composé de pistes de développement, d'une bibliographie à compléter et d'une iconographie non vérifiée. Il ne peut pas remplacer les trois études intégrales attendues.
- **Chiron et chapitres 118–133 :** signalés dans [le registre de récupération](mythologie-grecque/REGISTRE-RECUPERATION.md), mais non disponibles sous forme de manuscrits complets dans les sources inspectées ; aucun texte n'a été reconstitué à partir d'un résumé.
- **Aphrodite (MG-02.A) et Perse (CIV-01) :** déjà inscrits et publiés dans ce registre, donc exclus d'une nouvelle migration pour éviter les doublons.
- **Travail technique effectué :** mise à jour de `assets/mythos-reference.css` (grilles mobiles, retour à la ligne, repères de focus et préférence de mouvement réduit). Les fichiers historiques n'ont pas été supprimés, déplacés ou écrasés.
- **Limite de vérification :** le commit CSS peut être confirmé dans GitHub ; aucune capture navigateur réelle ni validation visuelle du déploiement public n'a été réalisée dans cette exécution.

**Action éditoriale suivante :** retrouver le fichier source intégral d'un volume non publié, puis vérifier titres, début, fin, notes, bibliographie et correspondance textuelle avant toute mise en ligne.
