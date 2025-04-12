#!/bin/bash

echo "Tworzenie sieci Docker: optiq_prod..."
docker network create optiq_prod 2>/dev/null || echo "Sieć już istnieje."

echo "Budowanie i uruchamianie kontenerów..."
docker-compose up --build -d

echo "Czekam na Postgresa..."
sleep 10

echo "Preload modeli Ollama (codellama, mistral)..."
curl http://localhost:11434/api/pull -d '{"name": "codellama"}'
curl http://localhost:11434/api/pull -d '{"name": "mistral"}'

echo "System gotowy. Frontend na: http://localhost:3000"
