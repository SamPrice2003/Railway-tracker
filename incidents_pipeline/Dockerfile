FROM python:latest

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY incidents_extract.py .

COPY incidents_transform.py .

COPY load.py .

COPY alert.py .

COPY pipeline.py .

CMD ["python", "pipeline.py"]