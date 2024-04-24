
FROM python:3.8-slim


WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip install --no-cache-dir nltk

EXPOSE 80

ENV NAME World

CMD ["python", "./process_text.py"]
