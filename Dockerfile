FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install numpy
RUN pip install -r requirements.txt

COPY . .

EXPOSE 3000

ENV MONGO_URL=mongodb+srv://admin:gBeCjN6Gm9thjsP9@cluster0.ecsej3g.mongodb.net/?retryWrites=true&w=majority

ENTRYPOINT [ "python" ]
CMD ["run.py"]
