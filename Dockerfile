FROM python:3.11-slim
WORKDIR /app
COPY *.py .
COPY discounts/ discounts/
COPY products/ products/
CMD ["python", "main.py"]
