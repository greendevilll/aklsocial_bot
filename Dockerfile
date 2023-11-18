FROM python:3.11.5

WORKDIR /app

COPY . .

ARG bot_token=6764593170:AAGyvOrY2meiVnyAdu0PkkABYUc0iAj3KRs
ARG admins=6551145249
ARG db_fn=data/main.db
ARG yaml=ru_RU.yaml

ENV bot_token=$bot_token
ENV admins=$admins
ENV db_fn=$db_fn
ENV yaml=$yaml

RUN python -m pip install -r req.txt

CMD [ "python", "main.py" ]