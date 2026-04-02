<<<<<<< HEAD
# mini-ovh-ai-agent
AI-powered cloud recommendation API (FastAPI + OpenAI)
=======
#  Mini OVH AI Agent

Prototype d’agent backend capable d’analyser un besoin client en infrastructure cloud et de proposer des solutions adaptées.

Ce projet simule un cas d’usage proche d’un environnement comme OVHcloud : aider des équipes (commerciales ou techniques) à qualifier rapidement un besoin et suggérer des architectures.

---

##  Objectif

Créer une API capable de :

- Recevoir une demande client (ex: SaaS, sécurité, stockage)
- Identifier les besoins techniques (scalability, security, etc.)
- Proposer des solutions cloud pertinentes
- Fournir une justification et une prochaine étape

---

##  Fonctionnement

Le système repose sur deux modes :

### 1. Analyse IA (si disponible)
Utilise un modèle OpenAI pour analyser la demande et générer une réponse structurée.

### 2. Fallback intelligent
Si l’API IA est indisponible (quota, erreur, etc.), un moteur local basé sur des mots-clés prend le relais.

>>> Cela garantit que l’application reste fonctionnelle en toutes circonstances.

---

## ⚙️ Stack technique

- Python 3.12
- FastAPI
- Uvicorn
- Pydantic
- OpenAI API
- python-dotenv

---

## 📁 Structure du projet

    mini_ovh/
    │
    ├── app/
    │   ├── main.py
    │   ├── schemas.py
    │   └── services/
    │       └── ai_service.py
    │
    ├── .env
    ├── requirements.txt
    └── README.md

---

##  Installation

    git clone <repo>
    cd mini_ovh

    python3 -m venv venv
    source venv/bin/activate

    pip install -r requirements.txt

---

##  Configuration

Créer un fichier `.env` :

    OPENAI_API_KEY=your_api_key_here

---

##  Lancer le projet

    python3 -m uvicorn app.main:app --reload

---

## 🌐 Accéder à l’API

    http://127.0.0.1:8000/docs

---

##  Exemple de requête

POST `/analyze`

    {
      "customer_request": "I need a scalable and secure infrastructure for my SaaS app"
    }

---

##  Exemple de réponse

    {
      "needs": ["scalability", "security"],
      "suggested_solutions": ["Public Cloud", "Private Network"],
      "justification": "Suggested solutions were selected based on the customer's infrastructure needs.",
      "next_step": "Clarify expected traffic, security constraints, and storage requirements."
    }

---

## 💡 Ce que j’ai appris

- Structurer une API propre avec FastAPI
- Gérer des réponses typées avec Pydantic
- Intégrer une IA dans un backend
- Gérer les erreurs (quota, API down)
- Concevoir un fallback robuste
- Penser produit plutôt que simple code

---

##  Améliorations possibles

- Intégration LangChain / LangGraph (agents avancés)
- Ajout de mémoire (historique client)
- Interface frontend (React)
- Connexion à de vraies APIs cloud (OVH, AWS)
- Multi-agent orchestration (analyse, pricing, architecture)

---

## 👤 Auteur

Van BUI  
Étudiant à l’école 42  
Passionné par les systèmes, l’IA et les architectures scalables

---

## ⚡ Note

Ce projet est un prototype pédagogique visant à démontrer une approche agent-based appliquée au cloud.
>>>>>>> 6bce8c9 (Initial commit - FastAPI AI agent)
