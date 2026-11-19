# Dota Hero Builds

Небольшой Python HTTP-сервис с примером стартового билда для героя Dota 2.
Подходит для тестирования GitHub PR-триггера в n8n и не требует зависимостей.

## Run

```powershell
python app.py
```

## Endpoints

- `GET /health` — статус сервиса.
- `GET /build` — стартовый билд для Axe на оффлейне.
