# pangea-proxy

This project exposes a simple Flask API that scrapes information from an
external page and returns it as JSON. It is meant as an example of a very
small application using Flask, Requests and BeautifulSoup.

## Requirements

- Python 3.8+
- Packages listed in `requirements.txt`

## Installation

Create a virtual environment (optional) and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the server

Execute `app.py` directly to start the development server on port 5000:

```bash
python app.py
```

For production-like environments you can use Gunicorn:

```bash
gunicorn app:app
```

## Running the tests

Install the test dependencies and run `pytest`:

```bash
pip install -r requirements-dev.txt
pytest
```

