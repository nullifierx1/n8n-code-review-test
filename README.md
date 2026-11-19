# Dota Hero Builds

Dependency-free Python HTTP service with static starter builds for 40 Dota 2
heroes: 10 Strength, 10 Agility, 10 Intelligence, and 10 Universal heroes.
The project is suitable for testing an n8n GitHub PR workflow.

## Run

```powershell
python app.py
```

## Endpoints

- `GET /health` — service status.
- `GET /build` — Axe's offlane starter build.
- `GET /build?hero=crystal-maiden` — Crystal Maiden's support build.
- `GET /heroes` — heroes grouped by primary attribute.
- `GET /heroes?attribute=agility` — the ten Agility heroes.

## Build source

The short item sets are a static demo snapshot informed by the public
[Dota2ProTracker Pro Builds catalogue](https://dota2protracker.com/builds).
They are not patch-locked advice: consult current guides before a real match.
