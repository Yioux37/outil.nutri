# Logique moteur v1 — Outil.Nutri

## Objectif
Décrire la logique générale du moteur de calcul avant implémentation technique.

---

## 1. Entrées du moteur

### Profil utilisateur
- poids
- niveau
- sport principal
- tolérance digestive

### Données activité
- sport
- durée
- intensité
- température
- distance éventuelle
- dénivelé éventuel

### Données logistiques
- contenants disponibles
- volumes disponibles

---

## 2. Pipeline global

1. récupérer les données utilisateur  
2. récupérer les données activité  
3. appliquer les règles métier selon le sport  
4. calculer les besoins de base  
5. ajuster selon intensité et durée  
6. ajuster selon tolérance digestive  
7. calculer le score de risque digestif  
8. choisir les formes d’ingestion  
9. répartir le plan dans les contenants  
10. générer le plan avant / pendant / après

---

## 3. Étape 1 — Validation des entrées
Vérifier :
- présence du sport
- durée valide
- température valide
- poids utilisateur disponible
- niveau renseigné
- tolérance digestive renseignée

Si données insuffisantes :
- bloquer le calcul
- ou appliquer une valeur prudente par défaut

---

## 4. Étape 2 — Application des règles par sport
Selon le sport :
- trail : prudence digestive renforcée
- running : stratégie plus simple, gels/liquides privilégiés
- cycling : apports glucidiques plus élevés possibles
- triathlon : logique segmentée simplifiée dès la v1

---

## 5. Étape 3 — Calcul des besoins de base

### 5.1. Glucides
Déterminer une plage de glucides par heure selon :
- sport
- durée
- intensité
- niveau

### 5.2. Hydratation
Déterminer une plage de ml/h selon :
- sport
- durée
- température

### 5.3. Sodium
Déterminer une plage de sodium selon :
- sport
- température
- durée
- logique prudente v1

---

## 6. Étape 4 — Ajustement digestif
Si tolérance digestive faible :
- rester sur la borne basse
- limiter les solides
- limiter les stratégies agressives

Si tolérance moyenne :
- appliquer le standard

Si tolérance élevée :
- autoriser la borne haute selon contexte

---

## 7. Étape 5 — Score de risque digestif
Le score dépend de :
- durée
- intensité
- température
- sport
- tolérance digestive
- niveau

### Résultat simplifié
- low
- medium
- high

### Conséquence
- low : plan standard
- medium : plan prudent
- high : plan sécurisé

---

## 8. Étape 6 — Choix des formes d’ingestion
Le moteur choisit ou recommande :
- liquide
- gel
- purée
- solide

En fonction de :
- sport
- intensité
- tolérance digestive
- durée
- risque digestif

---

## 9. Étape 7 — Répartition logistique
Le moteur traduit le besoin théorique en plan concret :
- combien emporter
- dans quel contenant
- sous quelle forme

Exemples :
- flasques trail
- bidons vélo
- gels à emporter
- répartition simple avant / pendant / après

---

## 10. Étape 8 — Génération de la sortie
Le moteur doit produire :

### Résumé
- sport
- durée
- intensité
- température
- niveau de risque

### Plan avant effort
- hydratation pré-effort
- prise éventuelle de glucides

### Plan pendant effort
- glucides / h
- hydratation / h
- sodium
- formes conseillées

### Plan après effort
- récupération hydrique
- récupération énergétique

### Plan de colisage
- répartition dans les contenants

---

## 11. Pseudo-logique simplifiée

```text
input user
input activity
validate data
load sport rules
compute carbs target
compute fluids target
compute sodium target
adjust for digestive tolerance
compute risk score
select intake formats
build packaging plan
generate final output