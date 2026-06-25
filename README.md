# IPL 2025 Dashboard - Backend API

A FastAPI backend serving IPL 2025 season data as REST API endpoints.

## Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the server
uvicorn main:app --reload
```

Server runs at: http://127.0.0.1:8000

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/api/summary` | Season summary (winner, caps, highest score) |
| GET | `/api/points-table` | Full points table |
| GET | `/api/points-table/{team_code}` | Single team e.g. `/api/points-table/RCB` |
| GET | `/api/top-scorers` | Top 5 run scorers |
| GET | `/api/top-wicket-takers` | Top 5 wicket takers |
| GET | `/api/playoffs` | Playoff results |
| GET | `/api/highlights` | Season highlights |

## Interactive Docs

Once running, visit:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Project Structure

```
ipl-backend/
├── main.py          # FastAPI app and routes
├── data.py          # All IPL 2025 data
├── requirements.txt # Dependencies
└── README.md        # This file
```
