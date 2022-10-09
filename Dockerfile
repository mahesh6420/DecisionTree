FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install numpy
RUN pip install -r requirements.txt

COPY . .

ENV PORT=80
ENV MONGO_URL=

EXPOSE 8080

ENTRYPOINT [ "python" ]
CMD ["run.py"]
