FROM python:3.12

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY Dashboard.py .
COPY database_connection.py .
COPY incidents_page.py .
COPY map_visualisation.py .
COPY metrics.py .
COPY subscribe_page.py .
COPY unsubscribe_page.py .
COPY visualisations.py .

CMD ["streamlit", "run", "Dashboard.py"]
