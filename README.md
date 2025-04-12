# AI Sandbox – No-Code Stack do Generowania i Testowania Kodu z LLM

## Co to jest?

AI Sandbox to aplikacja do:
- Generowania kodu (HTML/JS/TSX/React/SQL) przez modele LLM
- Wizualizacji, edycji i eksportu bloków kodu
- Testowania kodu na żywo w przeglądarce (sandbox/iframe)
- Tworzenia pipeline'ów z wielu modeli jednocześnie

## Stack technologiczny

| Warstwa     | Technologia                     |
|-------------|----------------------------------|
| Frontend    | React + Tailwind + Monaco + Vite |
| Backend     | FastAPI + Python + Pydantic      |
| Sandbox     | iframe + sandbox/index.html      |
| LLM Router  | YAML + REST API (OpenAI, Ollama…)|
| Baza danych | PostgreSQL (z opcją in-memory)   |
| Orkiestracja| Docker + Docker Compose          |

## Wymagania

- Docker + Docker Compose
- API key dla OpenAI / Together / Claude (opcjonalnie)
- Node.js (jeśli rozwijasz frontend lokalnie)

## Instalacja

```bash
git clone https://github.com/optiq-ai/optiq-ai
cd sandbox-ai-app
cp .env.example .env
./setup.sh
