
FROM registry.access.redhat.com/ubi8/python-311
WORKDIR /opt/app-root/src
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["uvicorn", "main.app:app", "--host", "0.0.0.0", "--port", "8080"]