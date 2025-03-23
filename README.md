# 🥗 Personalized Nutrition Assistant using langchain and langsmith

This is an AI-powered full-stack web application that generates **personalized meal plans** based on user inputs like age, weight, and dietary preferences. It uses **LangChain**, **LangSmith**, and **FAISS** to provide intelligent recommendations by querying a vector database built from a nutritional dataset.

---

## 🚀 Features

- 🧠 **AI-generated meal plans** using LangChain + OpenAI
- 📊 Input-based filtering: age, weight, and dietary preferences
- 🗃️ **FAISS-powered vector store** with nutritional content
- 🔍 LangSmith integration for chain tracing and observability
- ⚡ Built with **FastAPI** for fast backend development
- 🖥️ Clean Jinja2 HTML interface

---

## 🖼️ Frontend Overview

The frontend is a basic form built with **HTML + Jinja2** rendered using FastAPI. Users fill out:
- **Age**
- **Weight** (kg)
- **Dietary Preferences** (e.g., Vegan, Keto, Gluten-Free)

When the form is submitted, the backend fetches personalized meal plans using vector similarity search and large language model processing — then displays them as a clean HTML list.

---

## 🧠 How It Works (Backend Logic)

1. The form sends user inputs (age, weight, preferences) to `/generate`.
2. These inputs are used to filter and retrieve relevant meals from a **pandas DataFrame** loaded from `foundation_food.csv`.
3. Relevant results are passed into a **LangChain QA chain** backed by OpenAI's LLM.
4. A FAISS vector database is queried using **OpenAI Embeddings**.
5. The best results are traced and returned using **LangSmith**, if enabled.

---

## 🗂️ Project Structure

    langchain-nutrition-bot/
    ├── app/
    │   ├── data/
    │   │   └── foundation_food.csv         # 🥗 Dataset with nutrition info
    │   ├── templates/
    │   │   └── index.html                  # Frontend HTML form
    │   └── lib.py                          # LangChain, FAISS, and meal logic
    ├── main.py                             # FastAPI backend routes
    ├── generate_index.py                   # FAISS index creation from dummy docs
    ├── your_index.py                       # Optional: FAISS generation from Document objects
    ├── your_index/                         # ✅ Pre-generated FAISS vector index
    ├── requirements.txt                    # Dependencies
    └── README.md                           # 📘 This file

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

The FAISS vector index (`your_index/`) is already included for convenience.

However, if you'd like to regenerate it (e.g., using your own documents), you can run:

```bash
python generate_index.py
```

 ## Installation & Usage
1. Clone the Repository
```bash
git clone https://github.com/yourusername/langchain-nutrition-bot.git
cd langchain-nutrition-bot
```

2. Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Set Your OpenAI API Key
```bash
# Bash / macOS / Linux
export OPENAI_API_KEY="your-key"

# Windows PowerShell
$env:OPENAI_API_KEY="your-key"
```

5. Run the App
```bash
uvicorn main:app --reload
```
Then visit 👉 http://localhost:8000

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


## 🧪 Sample Test Input

| Age | Weight | Preferences   |
|-----|--------|----------------|
| 30  | 75 kg  | Gluten-Free    |
| 22  | 60 kg  | Vegan          |
| 45  | 85 kg  | Low-Carb       |

## ✅ TODO / Improvements

Add image previews for meals
Dockerize the project for easier deployment
Replace HTML with a React or Svelte frontend
Add login/authentication support
Integrate calorie tracker or macro calculator

📬 Contact
Made with 💻 by Bhuvaneshwari Balaji

🔗 GitHub: [@060205b](https://github.com/060205b)

💼 LinkedIn: [linkedin.com/in/yourlinkedin](https://www.linkedin.com/in/bhuvaneshwari-balaji-79972726a/)

📧 Email: bhuvaneshwaribalaji06@gmail.com
