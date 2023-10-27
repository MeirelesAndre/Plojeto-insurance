# Projeto Insurance

## 1- Create Python environment

```bash
conda create -n ml python=3.8
conda activate ml
pip install -r requirements.txt
```

## 2- Streamlit

```bash
conda create -n stenv python=3.8
conda activate stenv
pip install -r requirements.txt
```

### Referências Steamlit

- [Streamlit Documentation](https://docs.streamlit.io/library/api-reference/widgets)
- [30 Days of Streamlit](https://30days.streamlit.app/)
- [Data Science Portfolio Project From Scratch | Building a YouTube Data Dashboard with Streamlit](https://www.youtube.com/watch?v=Yk-unX4KnV4)

## 3- REST API

```bash
conda create -n fastAPI python=3.8
conda activate fastAPI
pip install -r requirements.txt
```

```bash
conda create -n flask python=3.8
conda activate flask
pip install -r requirements.txt
```

## 4- PyCaret

```bash
conda create -n autoML python=3.8
conda activate autoML
pip install -r requirements.txt
```

## 5- Google_Cloud

- [Upload Cloud](https://console.cloud.google.com/welcome/new?authuser=1&cloudshell=true&project=model-deployment-403118)

## 6- Docker


### Ubuntu
- [Docker Engine](https://docs.docker.com/engine/install/ubuntu/#set-up-the-repository)
- [Docker Desktop](https://docs.docker.com/desktop/install/ubuntu/)

Se usando Windows, utilizar o WSL2 (Windows Subsystem for Linux). Veja as instruções de instalação [neste link](https://learn.microsoft.com/pt-br/windows/wsl/install) (tutorial Microsoft) ou [deste link](v) (tutorial Linux).

### Criar imagem Docker
```
docker build -t fastapi-app .
docker run --name insurance_project -d -p 8000:8000 fastapi-app
```

## 7- MLFlow

```bash
conda create -n mlflow python=3.8
conda activate mlflow
pip install -r requirements.txt