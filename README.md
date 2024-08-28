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

# Update firewall rules to add server port

```
sudo firewall-cmd --list-all # To check existing added ports
sudo firewall-cmd --zone=public --permanent --add-port 8000/tcp
sudo firewall-cmd --reload
sudo firewall-cmd --list-all # Confirm that port has been added.
```
