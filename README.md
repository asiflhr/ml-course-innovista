````markdown
# 🚀 ML Course — Innovista

Welcome to **ML Course — Innovista**!  
This repository contains the environment setup and quick-start instructions for building **Machine Learning applications** with **FastAPI**, **Uvicorn**, and Python 🐍.

Whether you're a beginner in machine learning or an experienced developer looking for a quick refresh, this guide will get your development environment up and running **in minutes**.

---

## 📦 Prerequisites

- Python 3.8+ installed
- Basic understanding of virtual environments
- Familiarity with FastAPI (optional but helpful)

---

## 🛠 Step 1 — Create a Virtual Environment

```bash
python -m venv venv
```
````

This creates a `venv` folder containing an **isolated Python environment** for your project.

---

## 🔑 Step 2 — Activate the Virtual Environment

**Windows (PowerShell)**:

```powershell
.\venv\Scripts\Activate
```

**Mac/Linux**:

```bash
source venv/bin/activate
```

When activated, your terminal prompt will show `(venv)` at the start.

---

## 📥 Step 3 — Install Dependencies

Upgrade `pip` and install required packages:

```bash
pip install --upgrade pip
pip install uvicorn fastapi
```

---

## 📜 Step 4 — Save Your Dependencies

```bash
d
```

This will store exact package versions in `requirements.txt`.

To install them later on another system:

```bash
pip install -r requirements.txt
```

---

## 🚀 Step 5 — Run the Server

Start the FastAPI server with **Uvicorn**:

```bash
uvicorn app:app --reload
```

- **`app:app`** → `"module_name:FastAPI_instance"`
- **`--reload`** → Automatically restarts on code changes (useful for development)

---

## 📴 Step 6 — Deactivate the Environment

When done, simply run:

```bash
deactivate
```

---

## 💡 Pro Tip — Run Without Activating the venv

**Windows**:

```powershell
venv\Scripts\python -m uvicorn app:app --reload
```

**Mac/Linux**:

```bash
venv/bin/python -m uvicorn app:app --reload
```

---

## 📚 About This Course

This course covers:

- Python essentials for ML
- Machine Learning fundamentals
- API development with FastAPI
- Deploying ML models in production

Perfect for **students, developers, and AI enthusiasts** looking to build scalable ML apps with modern Python frameworks.

---

## 🔍 SEO Keywords

`machine learning course` · `python fastapi tutorial` · `uvicorn setup` · `fastapi machine learning` · `python venv guide` · `ml course innovista`

---

### 📄 License

This project is licensed under the **MIT License** — feel free to use and modify.

---
