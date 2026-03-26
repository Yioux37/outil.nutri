# Outil.Nutri

Outil.Nutri est un projet de moteur de plan de ravitaillement multi-sport pour les athlètes d’endurance.

Le projet vise à transformer des données simples sur l’athlète et l’effort en un plan de ravitaillement concret, cohérent et exécutable.

Sports couverts à ce stade :
- Trail
- Course sur route
- Cyclisme
- Triathlon

---

## 1. Vision du projet

La plupart des sportifs d’endurance préparent encore leur nutrition de manière :
- approximative
- trop générique
- difficile à exécuter sur le terrain
- peu adaptée à leur profil digestif
- peu adaptée à leur logistique réelle

Outil.Nutri vise à corriger cela.

L’idée n’est pas de produire un simple calculateur théorique.
L’idée est de construire progressivement un système capable de répondre à cette question :

> Quel plan de ravitaillement est cohérent pour cet athlète, sur cet effort, avec cette logistique ?

---

## 2. Ligne conductrice du projet

Le projet suit une logi — Cadrage
Définir clairement :
- le problème
- la cible
- le périmètre MVP
- la promesse produit

### Étape 2 — Règles métier
Formaliser des règles nutritionnelles simples mais cohérentes selon :
- le sport
- la durée
- l’intensité
- la température
- la tolérance digestive

### Étape 3 — Moteur minimal
Construire un moteur capable de produire :
- glucides / h
- hydratation / h
- sodium / L
- formats recommandés
- niveau de risque digestif

### Étape 4 — Maturité athlète
Intégrer des éléments comme :
- gut training
- volume d’entraînement
- séance longue récente
- niveau utilisateur

### Étape 5 — Packaging plan
Passer du besoin théorique à un plan d’emport réel :
- total fluides
- total glucides
- capacité portée
- nombre estimé de gels
- nombre estimé de bidons / flasques
- besoin de refill ou non

### Étape 6 — Future contextualisation
Préparer ensuite :
- le modèle athlète enrichi
- la Race Library
- les fiches course
- le système d’ingestion parc
Le projet est volontairement construit dans cet ordre :
1. exactitude
2. stabilité
3. utilité
4. personnalisation
5. contextualisation terrain
6. intégrations

---

## 3. État actuel du projet

À ce stade, le dépôt contient :

### Documentation produit
- cadrage
- proposition de valeur
- roadmap
- guide d’interviews
- règles métier v1
- arbre fonctionnel MVP
- schéma de données v1
- logique moteur v1
- grille de feedback bêta
- modèle athlète v2
- Race Library v1
- template Race Sheet
- système d’ingestion parcours v1
- modèle de recommandation course-athlète

### Moteur Python minimal
Le moteur sait actuellement produire :
- une cible glucidique par heure
- une cible hydrique par heure
- une cible sodium par litre
- des formats d’ingestion recommandés
- un niveau de risque digestif
- un plan logistique minimal de packaging

### Couverture de tests
Le projet possède une base de tests automatisés couvrant :
- cas par sport
- chaleur
- faible tolérance digestive
- effort court
- efng
- charge d’entraînement
- packaging
- capacité insuffisante
- profil sous-préparé
- profil préparé

---

## 4. Architecture actuelle

```text
outil.nutri/
├── docs/
│   ├── 01_note_de_cadrage.md
│   ├── 02_proposition_de_valeur.md
│   ├── 03_roadmap_produit.md
│   ├── 04_guide_interviews_utilisateurs.md
│   ├── 05_regles_metier_v1.md
│   ├── 06_arbre_fonctionnel_mvp.md
│   ├── 07_schema_de_donnees_v1.md
│   ├── 08_logique_moteur_v1.md
│   ├── 09_grille_feedback_beta.md
│   ├── 10_modele_athlete_v2.md
│   ├── 11_race_library_v1.md
│   ├── 12_race_sheet_template.md
│   ├── 13_systeme_ingestion_parcours_v1.md
│   └── 14_modele_recommandation_course_athlete.md
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── engine/
│   │   ├── __init__.py
│   │   ├── carbs.py
│   │   ├── digestion.py
│   │   ├── hydration.p─ .gitignore
└── README.md

