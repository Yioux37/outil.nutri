# Schéma de données v1 — Outil.Nutri

## Objectif
Définir les principales entités nécessaires au MVP.

---

## 1. Principes
Le modèle de données doit distinguer :
- les données utilisateur
- les données d’activité
- les calculs produits
- les sorties visibles
- les feedbacks post-effort

---

## 2. Entités principales

### 2.1. User
Informations générales sur l’utilisateur.

Champs principaux :
- id
- first_name
- last_name
- email
- weight_kg
- level
- main_sport
- digestive_tolerance
- created_at
- updated_at

---

### 2.2. Container
Contenants disponibles pour l’utilisateur.

Champs principaux :
- id
- user_id
- type
- volume_ml
- quantity
- notes

Exemples de type :
- bidon
- flasque
- ceinture
- poche

---

### 2.3. Activity
Effort pour lequel un plan est généré.

Champs principaux :
- id
- user_id
- sport
- duration_minutes
- intensity_level
- temperature_c
- distance_km
- elevation_gain_m
- notes
- created_at

---

### 2.4. ActivityContainer
Association entre une activité et les contenants réellement utilisés.

Champs principaux :
- id
- activity_id
- container_id
- quantity_used

---

### 2.5. NutritionPlan
Résultat global du moteur pour une activité.

Champs principaux :
- id
- activity_id
- carbs_per_hour
- fluids_ml_per_hour
- sodium_mg_per_l
- risk_level
- pre_effort_plan
- during_effort_plan
- post_effort_plan
- packaging_plan
- created_at

---

### 2.6. Feedback
Retour utilisateur après l’activité.

Champs principaux :
- id
- activity_id
- digestive_issue_score
- energy_issue_score
- thirst_issue_score
- adherence_score
- completed_plan
- notes
- created_at

---

## 3. Relations principales

- un User possède plusieurs Containers
- un User possède plusieurs Activities
- une Activity peut utiliser plusieurs Containers
- une Activity possède un NutritionPlan
- une Activity peut recevoir un Feedback

---

## 4. Champs structurants à standardiser

### level
Valeurs possibles :
- beginner
- intermediate
- advanced

### digestive_tolerance
Valeurs possibles :
- low
- medium
- high

### intensity_level
Valeurs possibles :
- low
- moderate
- high

### sport
Valeurs possibles :
- trail
- running
- cycling
- triathlon

### risk_level
Valeurs possibles :
- low
- medium
- high

---

## 5. Données hors périmètre v1
Ne pas intégrer tout de suite :
- fichiers GPX
- routes détaillées
- produits par marque
- météo live
- données Garmin / Strava
- historique avancé de personnalisation

---

## 6. Évolution prévue
Plus tard, le schéma devra pouvoir accueillir :
- Route
- Segment
- ProductReference
- WeatherSnapshot
- RecommendationEvent
- UserToleranceHistory