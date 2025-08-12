# ml-course-innovista

# Create a virtual environment

python -m venv venv

# Activate the virtual environment

# Windows (PowerShell)

.\venv\Scripts\Activate

# Mac/Linux:

source venv/bin/activate

# Install dependencies (e.g., uvicorn & friends)

pip install --upgrade pip
pip install uvicorn fastapi

# Save your dependencies

pip freeze > requirements.txt

# Now your requirements.txt holds the exact versions.

# Later, if you move to another system:

pip install -r requirements.txt

# Run uvicorn

uvicorn app:app --reload

# Here:

# app:app means "module_name:FastAPI_instance".

# --reload automatically restarts when files change (handy for dev).

# Deactivate when done

deactivate

# If you don’t want to activate the venv each time, you can run commands inside it directly:

venv/Scripts/python -m uvicorn app:app --reload # Windows
venv/bin/python -m uvicorn app:app --reload # Mac/Linux
