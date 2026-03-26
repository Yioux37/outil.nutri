# Arbre fonctionnel du MVP — Outil.Nutri

## Objectif
Définir la structure fonctionnelle minimale du produit pour la première version exploitable.

---

## 1. Vue d’ensemble

Outil.Nutri
- Onboarding
- Profil utilisateur
- Création d’une activité
- Génération du plan
- Résultat du plan
- Historique
- Feedback post-effort
- Réglages simples

---

## 2. Onboarding

### Objectif
Récupérer les informations minimales nécessaires au moteur.

### Données à collecter
- poids
- niveau utilisateur
- sport principal
- tolérance digestive
- contenants disponibles

### Sortie attendue
- profil initial utilisateur

---

## 3. Profil utilisateur

### Objectif
Centraliser les données de base de l’athlète.

### Contenu
- informations physiques
- niveau
- profil digestif simple
- matériel / contenants
- historique des activités
- historique des feedbacks

### Fonctions
- modifier le profil
- enregistrer les changements
- afficher l’état du profil

---

## 4. Création d’une activité

### Objectif
Créer une nouvelle demande de plan.

### Champs minimaux
- sport
- durée estimée
- intensité estimée
- température
- distance si utile
- dénivelé si utile
- contenants utilisés pour l’activité

### Résultat
- activité enregistrée
- données prêtes pour le moteur

---

## 5. Génération du plan

### Objectif
Transformer les données utilisateur et activité en plan de ravitaillement.

### Calculs attendus
- glucides / h
- hydratation / h
- sodium / h ou / L
- formes d’ingestion
- score de risque digestif

### Sorties
- plan avant
- plan pendant
- plan après
- répartition par contenant

---

## 6. Résultat du plan

### Objectif
Afficher clairement le plan généré.

### Sections attendues
- résumé de l’activité
- besoins globaux
- plan avant effort
- plan pendant effort
- plan après effort
- répartition par contenant
- alertes simples

### Principes UX
- information hiérarchisée
- pas de mur de texte
- actions concrètes
- vocabulaire simple

---

## 7. Historique

### Objectif
Retrouver les activités et plans déjà générés.

### Contenu
- liste des activités passées
- accès au plan enregistré
- accès au feedback associé
- statut : plan généré / feedback donné ou non

---

## 8. Feedback post-effort

### Objectif
Enregistrer le retour utilisateur après usage du plan.

### Questions minimales
- as-tu eu un problème digestif ?
- as-tu manqué d’énergie ?
- as-tu eu trop soif ?
- as-tu respecté le plan ?
- as-tu terminé ce que tu avais prévu ?

### Utilité
- affiner le profil utilisateur
- préparer la personnalisation future
- améliorer la pertinence du moteur

---

## 9. Réglages simples

### Contenu
- modification du profil
- gestion des contenants
- préférences simples
- suppression ou archivage éventuel

---

## 10. Hors périmètre MVP
Le MVP n’inclut pas :
- notifications live
- intégration Garmin / Wahoo
- machine learning
- recommandations par marque
- import GPX avancé
- adaptation en temps réel

---

## 11. User flow simplifié

1. L’utilisateur crée ou complète son profil  
2. L’utilisateur crée une activité  
3. Le moteur calcule un plan  
4. Le plan est affiché clairement  
5. L’utilisateur enregistre ou consulte le plan  
6. Après l’effort, l’utilisateur remplit un feedback  
7. Le système prépare la personnalisation future