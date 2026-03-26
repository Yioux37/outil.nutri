# Template Race Sheet — Outil.Nutri

## Objectif
Définir le format standard d’une fiche course afin de transformer un parcours brut en document utile pour le moteur et pour l’utilisateur.

Une Race Sheet doit résumer une course de manière exploitable.
Elle ne doit pas être une simple reprise du site organisateur.

---

## 1. Informations générales

### Champs
- nom de la course
- édition
- sport
- format
- date
- organisateur
- site officiel
- statut de vérification

### Exemple
- Course : Marmotte Granfondo Alpes
- Édition : 2026
- Sport : cycling
- Format : long
- Statut : verified

---

## 2. Profil général

### Champs
- distance totale
- dénivelé positif total
- dénivelé négatif total
- altitude maximale
- terrain dominant
- nombre de ravitaillements
- durée cible estimative
- difficulté globale

### Difficulté globale
- moderate
- hard
- very_hard
- extreme

### Utilité
Donner immédiatement la structure de l’épreuve.

---

## 3. Résumé exécutable

### Objectif
Donner une lecture simple et utile.

### Exemple de contenu
- effort long avec forte contrainte énergétique
- longues ascensions régulières
- nécessité d’une hydratation structurée
- importance du ravitaillement avant les sections clés
- risque digestif modéré à élevé selon chaleur et intensité

---

## 4. Sections clés

### Objectif
Identifier les moments qui changent réellement la stratégie.

Pour chaque section clé, renseigner :
- nom de section
- km début
- km fin
- type de section
- intensité attendue
- contrainte nutritionnelle
- note libre

### Types de section
- montée longue
- montée raide
- descente technique
- section roulante
- transition
- zone exposée à la chaleur
- zone favorable au ravitaillement

### Exemple
- Col principal
- km 42 à 60
- montée longue
- intensité soutenue
- éviter les solides sur le final

---

## 5. Zones de vigilance

### Objectif
Renseigner les points à surveiller.

### Catégories
- vigilance hydrique
- vigilance sodium
- vigilance digestive
- vigilance logistique
- vigilance énergétique

### Exemples
- longue section sans ravitaillement
- forte exposition au soleil
- enchaînement de montées
- descente technique rendant l’alimentation difficile
- transition vélo → course

---

## 6. Logistique terrain

### Objectif
Décrire les contraintes concrètes.

### Champs
- nombre et type de ravitaillements
- distance max sans assistance
- besoin potentiel de recharge
- contraintes de transport
- recommandations de setup

### Exemples
- 2 bidons recommandés
- recharge liquide nécessaire au km 80
- gels facilement accessibles à prévoir
- attention à l’ouverture des emballages en descente

---

## 7. Hypothèse de stratégie de base

### Objectif
Créer une stratégie initiale non personnalisée.

### Champs
- fourchette glucides
- fourchette hydratation
- fourchette sodium
- formats dominants
- points de bascule possibles

### Exemple
- 60 à 80 g/h
- 500 à 750 ml/h
- 700 à 900 mg/L
- liquide + gel
- solide possible uniquement sur sections roulantes

### Important
Cette stratégie n’est pas le plan final.
Elle sert de base à personnaliser selon l’athlète.

---

## 8. Points de vigilance digestifs

### Objectif
Anticiper les erreurs les plus probables.

### Exemples
- trop forte concentration dans les bidons
- absence d’eau claire avec les gels
- utilisation de solides avant une section intense
- sous-estimation de la chaleur
- ravitaillement trop tardif avant une longue montée

---

## 9. Données manquantes / niveau de confiance

### Objectif
Rendre la fiche honnête.

### Champs
- source principale
- niveau de confiance
- données à confirmer
- date de dernière vérification

### Niveau de confiance
- low
- medium
- high

### Utilité
Éviter de présenter comme “vrai” un parcours insuffisamment vérifié.

---

## 10. Structure synthétique recommandée

```text
Race Sheet
├── infos générales
├── profil général
├── résumé exécutable
├── sections clés
├── zones de vigilance
├── logistique terrain
├── stratégie de base
├── vigilance digestive
└── niveau de confiance