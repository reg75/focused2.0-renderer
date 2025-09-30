# FocusEd Renderer (FastAPI + WeasyPrint)
**EN:** Converts HTML into PDF bytes. Used by the Mailer and (optionally) Backend.  
**BR:** Converte HTML em PDF. Usado pelo Mailer e (opcionalmente) pelo Backend.

## Quick Start (Docker)
```bash
# EN: 1) Create the shared Docker network (only once)
# BR: 1) Criar a rede Docker compartilhada (apenas uma vez)
docker network create focused-net || true

# EN: 2) Build the renderer image
# BR: 2) Construir a imagem do renderer
docker build -t focused-renderer:0.1.0 .

# EN: 3) Run the container on port 8002
# BR: 3) Executar o contêiner na porta 8002
docker run --name renderer --rm   --env-file .env   --network focused-net   -p 8002:8002   focused-renderer:0.1.0
```

- **Swagger / OpenAPI:** <http://localhost:8002/docs>  
- **Health:** `GET /health`

## Environment
See `.env.example`. Key settings:
- `RENDERER_HOST` (default `0.0.0.0`)
- `RENDERER_PORT` (default `8002`)
- `LOG_LEVEL` (default `INFO`)

## Architecture
```mermaid
graph TB
  FE[Frontend (Nginx :80)] -->|/api proxy (CRUD: GET/POST/PUT/DELETE)| BE[Backend (FastAPI :8000)]
  BE -->|X-API-KEY auth| M[Mailer (FastAPI :8001)]
  M -->|POST /render| R[Renderer (WeasyPrint :8002)]
  M -->|Send email| SG[(SendGrid API)]
  BE -->|SQLite file (app.db)| DB[(SQLite)]
```

**External component:** WeasyPrint (HTML/CSS to PDF engine).

## API Overview
| Method | Path    | Description                           |
|-------:|---------|---------------------------------------|
| GET    | /health | Health probe                          |
| POST   | /render | Render `{ "html": "<…>" }` to PDF     |

**POST /render** (example)
```bash
curl -sS -X POST http://localhost:8002/render   -H "Content-Type: application/json"   -d '{"html":"<h1>Hello PDF</h1><p>From renderer</p>"}'   -o /tmp/test.pdf
```
_Response:_ `application/pdf`.

## Troubleshooting
- **422/400:** Ensure body is JSON with an `html` string.  
- **Missing glyphs:** Install fonts in the image (default DejaVu Sans); add additional fonts if needed.  
- **Large HTML:** Keep HTML/CSS minimal; inline critical CSS to improve render speed.

## Development Notes
- **EN:** Keep responses small and streaming safe; return clear JSON errors on failures.  
- **BR:** Mantenha respostas pequenas; retorne erros JSON claros em falhas.

## License
MIT — see `LICENSE`.

## Contributing
See `CONTRIBUTING.md`.