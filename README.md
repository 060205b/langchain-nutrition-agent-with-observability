---

# 🤖 LangChain-Powered Nutrition Agent with LangSmith Observability

This project is an AI-powered backend application that provides personalized meal suggestions using large language models, vector similarity search, and nutritional data. Built with LangChain, OpenAI, and FAISS, the app intelligently recommends meals based on user input like age, weight, and dietary preferences.

The goal is to demonstrate a real-world AI orchestration system, where a user’s input is transformed into relevant food suggestions by querying a nutrition-based vector database through a question-answering chain. The frontend is intentionally kept minimal to emphasize the backend intelligence and LLM workflow design.

> ⚠️ **Note:** The frontend is intentionally minimal - the core focus is on **AI agent integration**, data handling, and vector search logic rather than UI/UX.

> 🛠️ **Note:** This project is currently in progress. While the core functionality is implemented, final touches and full deployment are still underway. Details of the completed features are explained below.

---

## 🚀 Features

- 🧠 LangChain-based agent for dynamic meal recommendation
- 📈 LangSmith integrated for full chain observability
- 🗃️ FAISS-powered vector database built on real nutritional data
- 📊 Personalized filtering by age, weight, and dietary preferences
- ⚡ FastAPI backend with simple Jinja2 frontend

---

## 🖼️ Frontend Overview

The frontend is a basic form built with **HTML + Jinja2** rendered using FastAPI. Users fill out:
- **Age**
- **Weight** (kg)
- **Dietary Preferences** (e.g., Vegan, Keto, Gluten-Free)

When the form is submitted, the backend fetches personalized meal plans using vector similarity search and large language model processing - then displays them as a clean HTML list.

---

## 🧠 How It Works (Backend Logic)

1. **Indexing:**  
   - Run `generate_index.py` to load your nutrition dataset (CSV), convert each row into a document, and embed them using OpenAI Embeddings.
   - The embeddings are stored in a FAISS vector database (`your_index/`), enabling fast semantic search over your real data.

2. **Retrieval and Generation:**  
   - When a user submits the form, their input (age, weight, preferences) is used to construct a natural language query.
   - This query is embedded and used to search for the most relevant meal/nutrition documents in the FAISS vector database.
   - The top results are passed as context to a LangChain QA chain, which uses an OpenAI LLM to generate a personalized meal recommendation.
   - All steps are traced with LangSmith for observability and debugging.

---

## 🗂️ Project Structure

```
langchain-nutrition-bot/
├── app/
│   ├── data/
│   │   └── foundation_food.csv         # 🥗 Your nutrition dataset
│   ├── templates/
│   │   └── index.html                  # Frontend HTML form
│   └── lib.py                          # LangChain, FAISS, and meal logic
├── main.py                             # FastAPI backend routes
├── generate_index.py                   # FAISS index creation from your dataset
├── your_index/                         # ✅ Pre-generated FAISS vector index
├── .env
├── requirements.txt                    # Dependencies
└── README.md                           # 📘 This file
```

---

## 📊 Dataset

We use a structured CSV file called `foundation_food.csv` located at `app/data/foundation_food.csv`.

This dataset contains:

- Food name
- Calories
- Diet type (e.g., Vegan, Keto)
- Macronutrients

You can replace this dataset with your own, just maintain the same column structure for compatibility with the logic in `lib.py`.

---

## 🧠 Vector Index

The FAISS vector index (`your_index/`) is built from your real dataset.  
To regenerate it (for example, after updating your CSV), run:

```bash
python generate_index.py
```

---

## 📦 Tech Stack

| Layer     | Tech                         |
|-----------|------------------------------|
| Backend   | FastAPI                      |
| Frontend  | Jinja2 + HTML                |
| AI Chain  | LangChain (`load_qa_chain`)  |
| Tracing   | LangSmith (`@traceable`)     |
| Embedding | OpenAI Embeddings            |
| VectorDB  | FAISS                        |
| Data      | pandas, CSV files            |

---

## 🧪 Sample Test Input

| Age | Weight | Preferences   |
|-----|--------|----------------|
| 30  | 75 kg  | Gluten-Free    |
| 22  | 60 kg  | Vegan          |
| 45  | 85 kg  | Low-Carb       |

---

## 🚀 Installation & Usage

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/langchain-nutrition-bot.git
    cd langchain-nutrition-bot
    ```

2. **Create Virtual Environment**
    ```bash
    python -m venv .venv
    source .venv/bin/activate      # On Windows: .venv\Scripts\activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Your OpenAI API Key**
    ```bash
    # Bash / macOS / Linux
    export OPENAI_API_KEY="your-key"

    # Windows PowerShell
    $env:OPENAI_API_KEY="your-key"
    ```

5. **Generate the Vector Index**
    ```bash
    python generate_index.py
    ```

6. **Run the App**
    ```bash
    uvicorn main:app --reload
    ```
    Then visit 👉 http://localhost:8000

---

## ✅ TODO / Improvements

- Add image previews for meals
- Dockerize the project for easier deployment
- Replace HTML with a React or Svelte frontend
- Add login/authentication support
- Integrate calorie tracker or macro calculator

---

## 📬 Contact

**Bhuvaneshwari Balaji**

- 🔗 [GitHub](https://github.com/060205b)
- 💼 [LinkedIn](https://www.linkedin.com/in/bhuvaneshwari-balaji-79972726a/)
- 📧 bhuvaneshwaribalaji06@gmail.com

---
