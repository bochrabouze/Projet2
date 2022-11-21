FROM python:3.11
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY coinmarketcap.py .
CMD ["python3", "coinmarketcap.py"]