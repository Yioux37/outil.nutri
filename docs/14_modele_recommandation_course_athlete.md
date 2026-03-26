# Modèle de recommandation course-athlète — Outil.Nutri

## Objectif
Définir le modèle qui relie un athlète, une course et des contraintes réelles pour produire une recommandation personnalisée.

Le moteur final ne doit pas raisonner sur un parcours seul.
Il doit raisonner sur la rencontre entre :
- un athlète donné
- une course donnée
- une logistique donnée
- des conditions données

---

## 1. Rôle du modèle

Le modèle de recommandation course-athlète sert à :
- adapter la stratégie de base d’une course au profil réel de l’utilisateur
- transformer un résumé de course en plan exécutable
- filtrer les recommandations irréalistes
- préparer la future logique par segment

---

## 2. Entrées principales

### 2.1. Entrées athlète
- sport principal
- niveau
- expérience course
- charge habituelle
- profil digestif
- gut training level
- profil hydrique / sodium
- préférences logistiques

### 2.2. Entrées course
- sport
- distance
- D+
- altitude
- type de terrain
- sections clés
- ravitaillements
- contraintes logistiques
- stratégie de base éventuelle

### 2.3. Entrées contextuelles
- météo prévue
- température
- objectif utilisateur
- contenants choisis
- niveau d’ambition de la stratégie

---

## 3. Logique générale

Le moteur doit répondre à cette question :

“Quelle stratégie de ravitaillement est cohérente pour cet athlète sur cette course, dans ces conditions ?”

---

## 4. Pipeline de recommandation

1. charger le profil athlète  
2. charger la course ou le parcours  
3. charger les contraintes contextuelles  
4. calculer les besoins théoriques  
5. ajuster selon l’athlète  
6. ajuster selon la course  
7. ajuster selon la logistique  
8. produire une stratégie personnalisée  
9. attribuer un niveau de confiance et un niveau de risque

---

## 5. Ajustements côté athlète

Le moteur doit moduler selon :
- niveau réel
- expérience sur effort similaire
- maturité digestive
- volume d’entraînement
- formats tolérés
- charge d’entraînement habituelle

### Exemples
- novice = prudence accrue
- athlète expérimenté = fenêtre d’optimisation plus large
- faible gut training = limitation des stratégies agressives
- faible tolérance digestive = simplification des formats

---

## 6. Ajustements côté course

Le moteur doit moduler selon :
- durée probable
- intensité attendue
- profil global
- ravitaillements disponibles
- sections critiques
- difficulté logistique

### Exemples
- longue montée = vigilance sur le timing
- longue section sans ravitaillement = anticipation hydrique
- parcours très technique = accès aux apports plus difficile
- triathlon = bascule vélo → course à anticiper

---

## 7. Ajustements côté logistique

Le moteur doit moduler selon :
- nombre de bidons / flasques
- possibilité de recharge
- accès aux apports pendant l’effort
- besoin de formats simples
- préférences utilisateur

### Résultat attendu
Le moteur ne donne pas seulement un besoin théorique.
Il donne un plan réellement transportable et exécutable.

---

## 8. Sorties du modèle

Le modèle de recommandation doit produire :

### 8.1. Résumé stratégique
- niveau d’ambition
- niveau de risque
- stratégie dominante

### 8.2. Besoins cibles
- glucides
- hydratation
- sodium

### 8.3. Formats recommandés
- liquide
- gel
- purée
- solide

### 8.4. Plan logistique
- quoi emporter
- comment répartir
- quand recharger si besoin

### 8.5. Niveau de confiance
- low
- medium
- high

---

## 9. Trois niveaux de stratégie

### Stratégie prudente
- priorité à la sécurité digestive
- faible agressivité
- formats simples

### Stratégie standard
- équilibre entre performance et sécurité
- recommandation par défaut

### Stratégie optimisée
- réservée aux profils entraînés
- demande gut training et expérience suffisante
- plus sensible au risque de mauvaise exécution

---

## 10. Niveau de confiance de la recommandation

Le moteur doit indiquer si la recommandation repose sur :
- des données solides
- des hypothèses moyennes
- des données partielles

### Exemple
- athlète connu + course connue + logistique claire = confiance élevée
- athlète peu renseigné + course inconnue = confiance faible

---

## 11. Limites v1
Le modèle v1 ne gère pas encore :
- personnalisation live
- adaptation en temps réel
- segmentation automatique poussée
- apprentissage automatique
- intégrations externes avancées

---

## 12. But du modèle
Passer d’un calcul générique à une recommandation contextualisée.

Le modèle course-athlète doit être le point de rencontre entre :
- la théorie nutritionnelle
- la réalité du terrain
- la capacité réelle de l’utilisateur