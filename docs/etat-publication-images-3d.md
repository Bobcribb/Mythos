# MYTHOS — Carnet de publication des images 3D photoréalistes
Mise à jour : 3 novembre 2026 (Europe/Paris).

## Règles éditoriales impératives
- Ne publier que des images photoréalistes de reconstitution, avec vues architecturales et plans larges.
- Interdire tout menu, bandeau de site, légende, texte, cartouche ou infographie incorporé aux pixels du fichier public. Légende, datation, méthode, limites et sources doivent apparaître séparément dans le HTML.
- Ne pas utiliser de vues 2,5D ou de pseudo-schéma en remplacement des photographies de synthèse.
- Ne jamais déclarer une image « publiée » à la seule création de sa notice ou au seul commit du manifeste ; vérifier le fichier et son affichage sur le domaine public.
- Préserver les pages existantes, le thème anthracite/ivoire/or et les numéros des dossiers ; aucune duplication de slug.

## Audit des fichiers réellement publiés
Contrôle du domaine https://bobmythos.fr/Mythos/reconstitutions-photorealistes.html via navigateur le 3 novembre 2026 : une image de galerie se charge et s'affiche, « Athènes — Acropole classique », au chemin `/Mythos/assets/reconstitutions-3d/athenes-acropole.webp`.
Sur la branche main, au même contrôle, le dossier `assets/reconstitutions-3d/` contenait le seul WebP `athenes-acropole.webp` et le manifeste JSON d'une entrée. Aucune photographie de Delphes ou Némée n'était visible dans la galerie à ce contrôle.

## Lot source prioritaire : 13 planches
Archive conservée dans la Bibliothèque de fichiers ChatGPT : `MYTHOS_reconstitutions_3D_photorealistes.zip` (42 431 058 octets).
**Attention : cette archive contient treize planches composites PNG (montages à deux ou quatre vues et/ou affiches avec titres et encarts) ; il ne s'agit pas de treize fichiers photographiques autonomes, sans interface.**
Il faut réaliser des vues autonomes non annotées ou reprendre les scènes propres et contrôler chacune avant mise en ligne ; ne pas afficher les montages d'infographies avec menu ou encart comme « photo photoréaliste sans texte ».

Fichiers source :
1. `delphi_sanctuary_in_four_views.png` — Delphes, montage 4 vues ;
2. `mythos_nemea_s_ancient_wonders.png` — Némée, 2 vues et encarts ;
3. `ancient_corinth_temples_and_fountains.png` — Corinthe, 2 vues et encarts ;
4. `ancient_messene_sanctuaries_and_stadium.png` — Messène, 2 vues et textes ;
5. `mythos_sounion_temples_by_the_aegean.png` — Sounion, 2 vues avec cartouches ;
6. `mythos_brauron_sanctuary_of_artemis.png` — Brauron, 2 vues avec cartouches ;
7. `dodone_theater_and_sacred_oak_sanctuary.png` — Dodone, 2 vues avec textes ;
8. `mythos_bassae_temple_of_apollo.png` — Bassae, vue du temple et intérieur, avec cartouches ;
9. `a_detailed_illustrated_infographic_poster_no_webs.png` — Mycènes, panneau infographique ;
10. `a_detailed_illustrated_infographic_poster_in_black.png` — Olympie, panneau infographique ;
11. `a_highly_detailed_infographic_poster_in_dark_black.png` — Épidaure, panneau infographique ;
12. `a_detailed_high_detail_infographic_poster_in_a_bl.png` — Épidaure, second panneau, visuels partiellement similaires ;
13. `a_richly_detailed_high_resolution_illustrated_pos.png` — Tirynthe, panneau infographique.

## Visuels autonomes prêts à importer, distincts des treize planches
- Delphes, temple d'Apollon — `DEL-001_delphes_temple_apollon.webp` : image originale disponible dans les fichiers de conversation ; notice scientifique et garde-fous iconographiques prêts.
- Delphes, plan large panoramique — photo de synthèse créée le 3 novembre 2026 ; distinguer la réalité topographique (vallée du Pleistos, terrasses) de la distribution conjecturale des édifices.
- Samos, Héraion de Rhoikos — `heraion-samos-rhoikos-560-avjc.webp` : archive indépendante `MYTHOS_Heraion_Samos_photorealiste_pret_a_publier.zip` avec notice et source UNESCO.
**Ces fichiers ne sont pas déclarés en ligne** : un commit binaire puis un contrôle sur le domaine public sont nécessaires.

## Blocage technique vérifié
La connexion GitHub permet les opérations de texte et la création de blobs depuis une chaîne base64 fournie, mais aucun chemin de transfert automatique du fichier binaire local de ChatGPT vers cette action n'est établi pour l'instant. Il ne faut pas remplacer la photographie par un fichier texte/placeholder, ni annoncer la publication.
Le workflow GitHub Actions `generate-reconstitution.yml` dispose de `OPENAI_API_KEY` (dernier générateur exécuté avec succès le 3 novembre 2026) et crée de nouveaux WebP depuis l'API ; cela ne transfère pas les visuels préexistants de l'archive. Le workflow d'import `import-reconstitution.yml` peut importer une image depuis une URL HTTPS publique directe, quand une telle URL existe.

## Contrôles de validation avant toute annonce
1. WebP original présent dans `assets/reconstitutions-3d/` et taille non nulle.
2. Entrée de manifeste unique par slug, légende datée et source institutionnelle.
3. Page de galerie liée, sans bandeau intégré aux pixels.
4. Réponse 200 pour l'URL publique exacte et vérification dans un navigateur de `img.complete` et `img.naturalWidth > 0`.
5. Indiquer publiquement « publié » seulement après le point 4, sinon « fichier prêt à publier ».
