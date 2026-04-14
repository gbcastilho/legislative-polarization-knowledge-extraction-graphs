FROM python:3.13-trixie

## Build
RUN python -m venv ./.venv
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir data
RUN mkdir data/raw

## Run
COPY db/ ./db/

CMD [ "python", "db/generate_database.py" ]
