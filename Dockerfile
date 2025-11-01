FROM mcr.microsoft.com/playwright/python:v1.55.0-jammy

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN apt-get update && \
    apt-get install -y openjdk-17-jre wget && \
    wget -qO- https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz | \
    tar -xz -C /opt/ && \
    ln -s /opt/allure-2.27.0/bin/allure /usr/local/bin/allure

CMD ["sh", "-c", "pytest; allure serve /app/allure-results -h 0.0.0.0 -p 8080"]