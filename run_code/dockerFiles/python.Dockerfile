FROM python:3.9

WORKDIR /app

COPY run_code.py /app/run_code.py

CMD ["python3", "run_code.py"]
