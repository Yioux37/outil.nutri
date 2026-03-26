# Roadmap produit — Outil.Nutri

## Objectif global
Construire un outil de plan de ravitaillement multi-sport fiable, lisible et progressivement personnalisable pour le trail, la course sur route, le cyclisme et le triathlon.

---

## Phase 0 — Cadrage stratégique
### Objectif
Figer le projet avant tout développement.

### À faire
- choisir le nom provisoire du projet
- écrire la promesse centrale
- définir la cible de lancement
- définir le périmètre exact du MVP
- définir ce que le produit ne fait pas

### Livrables
- note de cadrage
- proposition de valeur courte
- cible prioritaire
- anti-périmètre du MVP

---

## Phase 1 — Validation terrain
### Objectif
Vérifier qu’il existe une vraie douleur utilisateur.

### À faire
- mener 15 à 30 interviews
- interroger trailers, coureurs route, cyclistes, triathlètes
- recueillir les problèmes réels rencontrés
- identifier les méthodes actuelles utilisées
- comprendre ce qui ferait gagner du temps ou éviter les erreurs

### Livrables
- synthèse des interviews
- top 10 des problèmes récurrents
- hiérarchie des cas d’usage
- vocabulaire utilisateur

---

## Phase 2 — Socle scientifique et règles métier
### Objectif
Transformer la recherche en règles exploitables.

### À faire
- formaliser glucides, hydratation, sodium, formes d’ingestion
- distinguer les règles par sport
- distinguer les règles par durée, chaleur, intensité et niveau
- créer une logique de score de risque digestif
- définir les contraintes spécifiques du triathlon

### Livrables
- matrice des règles métier par sport
- matrice par durée
- matrice par niveau
- score digestif v1
- document des hypothèses moteur

---

## Phase 3 — Architecture fonctionnelle et data
### Objectif
Structurer le produit avant de coder.

### À faire
- dessiner l’arborescence du produit
- définir le user flow
- définir les entités de données
- séparer entrées, calculs internes, sorties visibles et feedbacks
- prévoir la place future du GPX

### Livrables
- arbre fonctionnel du MVP
- user flow complet
- schéma de données
- liste des tables
- liste des champs principaux

---

## Phase 4 — Prototype du moteur
### Objectif
Tester le cerveau du produit sans dépendre de l’interface.

### À faire
- coder un prototype Python ou un tableur logique
- injecter des cas d’usage réels
- vérifier la cohérence des plans
- corriger les règles incohérentes
- tester les cas limites

### Cas tests minimaux
- trail 2 h
- trail long chaud
- marathon
- sortie vélo 4 h
- cyclosportive montagne
- triathlon M
- triathlon long
- sortie avec faible tolérance digestive

### Livrables
- prototype moteur v1
- bibliothèque de cas tests
- tableau sortie attendue / sortie obtenue
- journal des corrections

---

## Phase 5 — Prototype UX
### Objectif
Rendre le moteur lisible et compréhensible.

### À faire
- concevoir les écrans principaux
- tester la compréhension du plan
- définir l’ordre d’affichage des informations
- éviter l’effet mur de texte

### Écrans MVP
- onboarding
- profil
- nouvelle activité
- résultat du plan
- historique
- feedback post-effort

### Livrables
- wireframes
- logique de navigation
- structure d’affichage du plan
- principes UX de lecture terrain

---

## Phase 6 — Développement du MVP
### Objectif
Construire la première version fonctionnelle du produit.

### À faire
- développer le front web
- développer le backend API
- isoler le moteur métier
- connecter la base de données
- gérer l’authentification
- enregistrer les activités, plans et feedbacks

### MVP inclus
- profil utilisateur
- création d’une activité
- calcul du plan
- sortie avant / pendant / après
- répartition par contenant
- sauvegarde
- historique
- feedback simple

### MVP exclu
- live
- notifications intelligentes
- Garmin / Wahoo
- marketplace produits
- machine learning
- import GPX avancé

### Livrables
- MVP web fonctionnel
- base de données propre
- moteur intégré
- historique simple
- feedback basique

---

## Phase 7 — Bêta test terrain
### Objectif
Mettre le produit face à des utilisateurs réels.

### À faire
- faire tester le MVP à 10 à 20 utilisateurs
- relever les incompréhensions
- relever les sorties absurdes
- mesurer l’adhérence au plan
- lister les données manquantes

### Livrables
- tableau de feedbacks
- classement des bugs
- classement des irritants UX
- liste des demandes récurrentes
- décisions de correction

---

## Phase 8 — Personnalisation par logs utilisateurs
### Objectif
Passer du plan générique au plan personnalisé.

### À faire
- structurer le questionnaire post-effort
- enregistrer les retours digestifs
- enregistrer la fatigue, la soif, l’écœurement et l’adhérence
- ajuster les profils utilisateurs
- créer un historique de tolérance

### Livrables
- formulaire post-course
- score digestif
- score d’adhérence
- logique d’ajustement du profil
- premiers profils types

---

## Phase 9 — Contextualisation GPX
### Objectif
Adapter le plan au parcours réel.

### À faire
- importer un GPX
- parser le tracé
- récupérer distance et dénivelé
- découper le parcours en segments utiles
- créer des fenêtres de ravitaillement
- lier le plan nutritionnel au terrain

### Livrables
- parser GPX
- segmentation du parcours
- règles de ravito par segment
- affichage du plan contextualisé

---

## Phase 10 — Intégrations externes
### Objectif
Brancher les intégrations réellement utiles.

### Ordre logique
1. météo
2. Strava
3. Garmin / Wahoo plus tard

### À faire
- connecter une API météo
- tester récupération de routes ou d’activités
- définir les limites techniques
- chiffrer les coûts
- documenter les dépendances

### Livrables
- liste des APIs
- faisabilité
- coûts
- ordre d’intégration

---

## Phase 11 — Business, légal et lancement
### Objectif
Préparer une mise sur le marché crédible.

### À faire
- choisir le modèle économique
- cadrer les disclaimers
- rédiger les CGU et la politique de confidentialité
- définir la niche de lancement
- préparer une page de présentation
- rédiger les premiers cas d’usage démonstratifs

### Livrables
- hypothèses de pricing
- scénario freemium / unitaire / abonnement
- documents légaux minimaux
- message de lancement
- landing page simple

---

## Priorités absolues
L’ordre à respecter est :

1. cadrage  
2. douleur marché  
3. règles métier  
4. moteur  
5. UX  
6. MVP  
7. tests  
8. personnalisation  
9. GPX  
10. intégrations  
11. business

---

## Vision d’exécution
Le produit doit d’abord être exact.  
Ensuite compréhensible.  
Ensuite utile.  
Ensuite personnalisable.  
Ensuite contextualisé au terrain.  
Ensuite connecté à un écosystème externe.