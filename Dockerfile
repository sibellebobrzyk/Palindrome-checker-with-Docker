FROM python:3.13.1-slim
WORKDIR /main
COPY main.py requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
