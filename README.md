# rag-tutorial-v2

## Create new .env

```
python -m venv .venv
source .venv/bin/activate
.venv/bin/python
python3 -m pip install --upgrade pip
```

## Install requirements

```
python3 -m pip install -r requirements.txt
```

## Install Ollama (Linux)

```
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.1
ollama pull nomic-embed-text
```

## Populate Database

```
python3 populate_database.py
```

## Run

```
python query_data.py "I want to generate images"
```
