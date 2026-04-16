FROM python:3.13-trixie

WORKDIR /app

## Build
RUN python -m venv ./.venv
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir -p data/raw

## Run
COPY db/ ./db/

CMD [ "python", "db/generate_database.py" ]
