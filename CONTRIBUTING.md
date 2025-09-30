# Contributing — FocusEd Renderer
**EN:** Thanks for helping improve the FocusEd renderer.  
**BR:** Obrigado por colaborar com o renderer do FocusEd.

## How to work locally
```bash
docker network create focused-net || true
docker build -t focused-renderer:0.1.0 .
docker run --name renderer --rm   --env-file .env   --network focused-net   -p 8002:8002   focused-renderer:0.1.0
```
- **Docs:** http://localhost:8002/docs  
- **Health:** `GET /health`

## Branch & commit style
- Branches: `feat/<topic>`, `fix/<bug>`, `docs/<area>`
- Commits: Conventional Commits

## Code style
- FastAPI idioms; small handlers
- Validate `Content-Type: application/json`
- Return explicit status codes and error shapes

## Tests & checks
- `POST /render` with sample HTML should return a valid PDF
- Add fonts if your templates need specific glyphs

## Definition of done
- Builds & runs via Docker
- `/health` and `/docs` pass manual checks
- README/CHANGELOG updated