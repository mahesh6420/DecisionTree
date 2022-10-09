FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install numpy
RUN pip install -r requirements.txt

COPY . .

EXPOSE 3000

ENV MONGO_URL=

ENTRYPOINT [ "python" ]
CMD ["run.py"]
