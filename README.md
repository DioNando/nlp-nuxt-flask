# **Text Analysis Application** 📊

## **Description**  
Cette application permet d'effectuer plusieurs analyses de texte en ligne, notamment :  
- Analyse de sentiments  
- Reconnaissance des entités nommées  
- Résumé de texte  
- Traduction de texte  

Le frontend est développé avec **Nuxt.js**, tandis que le backend utilise **Flask** pour gérer les traitements NLP.  

---

## **Fonctionnalités**  
### Frontend (Nuxt.js)  
- Interface utilisateur intuitive et responsive.  
- Prise en charge de l'entrée de texte et affichage des résultats d'analyse.  

### Backend (Flask)  
- **Analyse de sentiments** : Détection du sentiment global d'un texte (positif, négatif, neutre).  
- **Reconnaissance d'entités nommées** : Extraction des noms propres, lieux, organisations, etc.  
- **Résumé de texte** : Génération de résumés basés sur des algorithmes NLP.  
- **Traduction** : Traduction automatique en utilisant des modèles ou des services disponibles.  

## **Technologies utilisées**  
### Frontend  
- **Nuxt.js** (Vue 3, Tailwind CSS)  
- **Axios** pour les appels API  

### Backend  
- **Flask**  
- **Flask-CORS** pour la gestion des cross-origin requests  
- Bibliothèques NLP :  
  - `nltk` pour l'analyse de sentiments  
  - `bert-extractive-summarizer` pour le résumé de texte  
  - `googletrans` pour la traduction  

## **Installation et configuration**  
### **Prérequis**  
- Node.js v16+  
- Python 3.9+  
- Docker  

## **API Endpoints**  
| Méthode | Endpoint                  | Description                              | Exemple de body          |
|---------|---------------------------|------------------------------------------|--------------------------|
| `POST`  | `/sentiment_analysis`     | Analyse le sentiment d'un texte          | `{ "text": "I love this!" }` |
| `POST`  | `/named_entity_recognition` | Identifie les entités nommées dans un texte | `{ "text": "John lives in Paris." }` |
| `POST`  | `/text_summarization`     | Génère un résumé pour le texte fourni    | `{ "text": "Long text here..." }` |
| `POST`  | `/language_translation`   | Traduit un texte dans une autre langue   | `{ "text": "Hello", "target_lang": "fr" }` |

## **Contributions**  
Les contributions sont les bienvenues !  
1. Forkez le repo  
2. Créez une branche : `git checkout -b feature/nom-de-la-fonctionnalite`  
3. Soumettez une pull request  

---

## **Auteur**  
**RAZAFIMAHEFA Tolotra David Fernando**  

N'hésitez pas à me contacter pour toute question ou suggestion. 🚀  