# Règles métier v1 — Outil.Nutri

## Objectif
Définir les règles métier initiales permettant de générer un plan de ravitaillement cohérent pour le trail, la course sur route, le cyclisme et le triathlon.

---

## 1. Principes généraux

### 1.1. Variables d’entrée principales
- sport
- durée estimée
- intensité estimée
- température
- poids utilisateur
- niveau utilisateur
- tolérance digestive
- contenants disponibles

### 1.2. Variables de sortie principales
- glucides par heure
- hydratation par heure
- sodium par heure ou par litre
- formes d’ingestion recommandées
- répartition avant / pendant / après
- score de risque digestif

---

## 2. Règles de base par sport

| Sport | Glucides / h | Hydratation / h | Sodium / L | Formes privilégiées |
|---|---:|---:|---:|---|
| Trail | 40 à 60 g/h | 500 à 800 ml/h | 500 à 800 mg/L | liquide, gel, purée |
| Course sur route | 30 à 60 g/h | 400 à 700 ml/h | 400 à 700 mg/L | liquide, gel |
| Cyclisme | 60 à 90 g/h | 500 à 900 ml/h | 600 à 1000 mg/L | liquide, gel, solide |
| Triathlon | segmenté | segmenté | segmenté | mixte selon segment |

---

## 3. Règles de base par durée

### Effort inférieur à 1 h 30
- ravitaillement léger
- priorité à l’hydratation
- glucides utiles surtout si intensité élevée

### Effort entre 1 h 30 et 3 h
- mise en place d’une stratégie glucidique structurée
- prise régulière
- surveillance simple de l’hydratation

### Effort entre 3 h et 5 h
- stratégie complète nécessaire
- importance du sodium
- nécessité de répartition par contenant

### Effort supérieur à 5 h
- stratégie renforcée
- risque digestif plus élevé
- rotation des formats et des saveurs à prévoir
- surveillance accrue de l’hydratation et du sodium

---

## 4. Règles par intensité

### Intensité faible à modérée
- meilleure tolérance digestive
- formats variés autorisés selon sport
- concentration glucidique plus souple

### Intensité élevée
- prudence digestive renforcée
- priorité aux formes liquides ou semi-liquides
- réduction ou suppression des solides selon sport

---

## 5. Règles par tolérance digestive

### Tolérance faible
- rester dans la borne basse des glucides recommandés
- privilégier liquide, gel simple, purée
- éviter les prises trop concentrées
- limiter les solides

### Tolérance moyenne
- appliquer les recommandations standards
- surveiller la concentration des boissons
- adapter les formes selon durée et intensité

### Tolérance élevée
- possibilité d’approcher les bornes hautes
- diversité de formats plus large
- possibilité d’intensifier l’apport si gut training validé

---

## 6. Règles par sport détaillées

### 6.1. Trail
- digestion plus fragile à cause des chocs mécaniques et du dénivelé
- prudence sur les solides
- priorité aux liquides, gels, purées
- si effort long : vigilance forte sur sodium et écœurement
- si chaleur + durée longue : renforcement hydratation et sodium

### 6.2. Course sur route
- effort souvent plus régulier que le trail
- stratégie simple mais stricte
- gels et liquides prioritaires
- prudence accrue à allure de compétition
- peu de place pour l’improvisation sur les prises

### 6.3. Cyclisme
- meilleure tolérance digestive globale
- glucides plus élevés possibles
- solides mieux tolérés
- logistique plus simple grâce aux bidons et poches
- hydratation à surveiller malgré sensation de fraîcheur liée au vent

### 6.4. Triathlon
- logique segmentée
- vélo = segment principal de l’apport énergétique
- course à pied = segment à digestion plus fragile
- réduction des solides avant la transition vers la course
- stratégie pensée sur l’ensemble de l’épreuve, pas segment par segment isolé

---

## 7. Règles spécifiques triathlon

### Segment natation
- pas de ravitaillement pendant l’effort
- préparation avant le départ uniquement

### Segment vélo
- segment prioritaire pour les glucides et l’hydratation
- possibilité d’intégrer des solides si tolérance suffisante
- structuration forte de la prise

### Transition vélo → course
- réduire ou supprimer les solides avant la fin du vélo
- préparer une transition digestive plus légère
- privilégier gel ou liquide si besoin

### Segment course à pied
- digestion plus fragile
- revenir à des formes simples et digestes
- sécuriser plutôt qu’optimiser agressivement

---

## 8. Règles de sécurité digestive

- éviter de superposer boisson très concentrée + gel sans eau claire si risque digestif élevé
- éviter les solides à intensité élevée chez les profils sensibles
- réduire la concentration glucidique si signes digestifs antérieurs
- ne pas recommander des apports élevés sans gut training validé
- ne pas pousser des recommandations agressives chez un utilisateur novice

---

## 9. Gut training

### Utilisateur non entraîné digestivement
- rester prudent sur les glucides élevés
- ne pas viser directement les bornes hautes
- proposer une montée progressive

### Utilisateur entraîné digestivement
- autoriser une montée des glucides selon sport et tolérance
- valider les niveaux élevés uniquement si déjà testés

---

## 10. Règles de score de risque digestif v1

Le score de risque digestif dépend de :
- la durée
- l’intensité
- la température
- le sport
- la tolérance digestive
- le niveau utilisateur

### Logique simple v1
- risque faible : effort modéré, tolérance correcte, conditions stables
- risque moyen : durée longue ou chaleur ou intensité élevée
- risque élevé : combinaison chaleur + durée + intensité + faible tolérance digestive

### Conséquences
- risque faible : stratégie standard
- risque moyen : prudence sur concentration et formats
- risque élevé : sécuriser le plan, réduire l’agressivité nutritionnelle

---

## 11. Hors périmètre v1
Les règles suivantes ne sont pas encore gérées dans cette version :
- lecture GPX détaillée
- segmentation fine du parcours
- recommandations par marque ou produit précis
- adaptation live
- machine learning
- intégration Garmin / Wahoo / Strava

---

## 12. But de la version v1
La version v1 doit permettre :
- de générer un plan cohérent
- de rester prudente sur la digestion
- de différencier proprement les 4 sports
- de préparer la future personnalisation par logs utilisateur