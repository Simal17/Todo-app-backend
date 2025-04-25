# 📝 Todo App Backend – FastAPI + Strawberry GraphQL

This is the **backend** portion of a full-stack Todo application, built using:

- **Framework**: FastAPI
- **GraphQL**: Strawberry
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **AI Integration**: Public LLM API (via OpenAI)

---

## 🚀 Getting Started (Windows)

Follow these steps to run the backend locally.

---

### 1️⃣ Set Up Virtual Environment

# Create a virtual environment
python -m venv .venv or python3

# Activate it (Windows)
.venv\Scripts\activate

# Or activate on Mac/Linux
source .venv/bin/activate

# Install Dependencies
pip install -r requirements.txt

# Add Environment Variables
Create a .env file and add:
OPENAI_API_KEY=sk-abc-YOUROPENAIKEY

# Run the Server
uvicorn main:app --reload

➡️ Server will run at: http://localhost:8000
➡️ GraphQL Playground available at: http://localhost:8000/graphql
