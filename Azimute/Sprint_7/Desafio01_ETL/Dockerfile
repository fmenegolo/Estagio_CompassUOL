
FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install boto3

EXPOSE 8080

CMD ["python", "azimute.py"]