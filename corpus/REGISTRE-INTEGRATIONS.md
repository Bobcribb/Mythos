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


## Iconographie philosophique — contrôle de l'exécution du 3 novembre 2026

**Pages réellement identifiées dans `main` :** `/philosophie-iliade.html` (12 sections d'étude), `/philosophie-odyssee.html` (12 sections) et `/philosophie-theogonie.html` (13 sections). Chacune contenait trois figures documentaires avant cette opération. Le document `contenus/philosophie/homere-hesiode-dossier-preparatoire.md` reste séparé, sans duplication de ses paragraphes.

**Ajouts vérifiés après écriture GitHub :**
- `/assets/philosophie/iliade-parcours-ethique.svg` inséré dans `/philosophie-iliade.html` — mênis, choix de la destinée, violence contre Hector, reconnaissance avec Priam.
- `/assets/philosophie/odyssee-identite-reconnaissance.svg` inséré dans `/philosophie-odyssee.html` — Calypso, mêtis, cicatrice, lit conjugal.
- `/assets/philosophie/theogonie-succession-pouvoir.svg` inséré dans `/philosophie-theogonie.html` — puissance primordiale, Ouranos, Cronos et Zeus.
- `/assets/mythos-iconographie.css` enrichi d'un affichage adapté au format des schémas et d'un lien de zoom accessible.

**Statut documentaire :** trois schémas vectoriels originaux édités en 2026 ; ni photographies antiques ni rendus produits par intelligence artificielle. Chaque page contient désormais quatre figures balisées en HTML (trois iconographies documentaires préexistantes + un schéma nouveau). Les SVG portent leurs références aux passages homériques ou hésiodiques ; les textes des études, titres et ancres ont été préservés. Les nombres 12, 12 et 13 désignent des sections, **pas** un nombre de pages A4 certifié : l'exigence de dix pages imprimées par étude reste à vérifier par un contrôle de pagination.

**Vérification :** fichiers et insertions relus depuis l'API GitHub après les commits ; exécution GitHub Pages `41644417144` terminée avec conclusion `success` sur `e7718f2dd656d3cdf1fc4bafb3aa168286638748`. L'accès public au domaine `bobmythos.fr` et le rendu sur navigateur n'ont pas pu être vérifiés via le réseau de cette exécution. Ne pas assimiler le build réussi à une inspection visuelle. L'enrichissement des autres pages se poursuit à partir du catalogue existant `assets/mythos-iconographie.js` ; éviter les doublons de visuels déjà déclarés.


## 3 novembre 2026 — Intégration ODS-S28 : tome XXVIII

| Cote | Document source | Fichiers sur GitHub | Contrôle d'intégrité |
|---|---|---|---|
| **ODS-S28** | `MYTHOS_Origines_du_sacre_Tome_XXVIII_Ch363-370_2026-11-01.md` (Bibliothèque, dossier `MYTHOS-suivi-editorial`, 1er novembre 2026) | [Page de lecture](origines-du-sacre/tome-XXVIII-chapitres-363-370.html) ; [copie Markdown exacte](origines-du-sacre/tome-XXVIII-chapitres-363-370.md) | Source complète lue : **54 221 caractères**, 379 lignes, huit chapitres **363–370**, bibliographie **[S1]–[S19]** et état éditorial terminal conservés. La copie Markdown a été relue depuis GitHub et comparée caractère par caractère à la source : identité exacte. La version HTML est une conversion de lecture avec sommaire, sans suppression volontaire de texte, plus avertissement éditorial ajouté. |

Cette livraison appartient à la **série de suivi** des *Origines du sacré*. Les cotes `ODS-Sxx` distinguent cette série de l'édition cumulative I–XXVII, dont la numérotation ne doit pas être recalculée sans concordance critique. Le manuscrit source était signalé comme non publié sur WordPress au 1er novembre ; il est désormais transféré sur la branche par défaut GitHub au 3 novembre. Son avertissement originel est reproduit tel quel, avec cette clarification en tête de l'HTML.

**Vérifications effectuées :** URL du document source GitHub accessible dans le dépôt ; HTML récupéré de GitHub après création et comparé exactement à la chaîne écrite ; dix liens de sommaire pointent vers des en-têtes générés, dont huit chapitres. Index ODS, sommaire général et page d'accueil mis à jour. **Contrôles restant nécessaires :** bibliographie et identifications scientifiques, apparence navigateur, liens externes, déploiement sur `bobmythos.fr`.

**Aucun doublon des tomes existants n'a été créé.** Les archives historiques I–XXVII restent inchangées.


## 3 novembre 2026 — Iconographie des monographies, contrôle complémentaire

**Base inspectée avant modification :** `philosophie-iliade.html`, `philosophie-odyssee.html`, `philosophie-theogonie.html`, tous présents sur la branche par défaut avec respectivement 12, 12 et 13 sections et **7 figures HTML chacun**. Les images et schémas déjà présents ont été identifiés avant tout ajout ; aucune ancienne figure n'a été remplacée.

**Trois nouvelles figures vectorielles intégrées et relues après commit :**

| Page et chapitre | Fichier SVG ajouté | Source primaire vérifiée | Nature documentaire |
| --- | --- | --- | --- |
| *Iliade*, étude 09 (bouclier d'Achille) | `assets/philosophie/iliade-bouclier-monde.svg` | Homère, *Iliade* XVIII, 478–608 ; [texte de référence](https://www.theoi.com/Text/HomerIliad18.html) | Schéma conceptuel des motifs poétiques, **non** restitution archéologique ; assistance IA déclarée. |
| *Odyssée*, analyse 02 (Télémachie) | `assets/philosophie/odyssee-telemachie-memoire.svg` | Homère, *Odyssée* I–IV, surtout III et IV ; [texte du chant III](https://www.theoi.com/Text/HomerOdyssey3.html), [chant IV](https://www.theoi.com/Text/HomerOdyssey4.html) | Schéma interprétatif de la mémoire et de l'action de Télémaque, **non** carte historique ; assistance IA déclarée. |
| *Théogonie*, étude 11 (Zeus et Métis) | `assets/philosophie/theogonie-zeus-metis.svg` | Hésiode, *Théogonie* 886–900 ; [texte de référence](https://adfonteslibrary.org/work-hesiod-theogony) | Schéma analytique de la souveraineté et de la contrainte, **non** objet antique ; assistance IA déclarée. |

**Contrôle d'intégrité :** l'HTML précédent a été conservé **à l'identique** hors insertion d'une figure `<figure>` avec lien SVG, `<img>` doté de texte alternatif et dimensions, sources, datation de création (2026), légende et déclaration d'assistance IA. Chacune des trois pages comporte maintenant **8 figures**, soit **24 figures au total pour ces trois monographies**. Les six fichiers (trois HTML et trois SVG) ont été relus depuis GitHub après écriture. Aucun titre, texte préexistant, identifiant de section, sommaire, numérotation ni automatisation n'a été modifié.

**Limites de ce contrôle :** sections ≠ pages imprimées ; le minimum de dix pages A4 doit être vérifié en sortie PDF/navigateur. L'API GitHub atteste les fichiers et commits, non l'affichage public. Les tentatives de consultation de `bobmythos.fr` n'ont pas permis d'inspecter la page ou le SVG sur le domaine ; aucun état de déploiement public n'est certifié ici. Pour les prochaines exécutions, reprendre l'inventaire de chaque rubrique avant insertion et ne jamais dupliquer les figures existantes.
