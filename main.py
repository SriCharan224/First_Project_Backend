from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data import (
    points_table,
    top_scorers,
    top_wicket_takers,
    playoff_results,
    season_highlights,
    season_summary
)

app = FastAPI(
    title="IPL 2025 Dashboard API",
    description="REST API serving IPL 2025 season data",
    version="1.0.0"
)

# Allow frontend (HTML file) to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "IPL 2025 Dashboard API is running", "version": "1.0.0"}


@app.get("/api/summary")
def get_summary():
    """Returns season summary: winner, orange cap, purple cap, highest score"""
    return season_summary


@app.get("/api/points-table")
def get_points_table():
    """Returns full points table for all 10 teams"""
    return {"data": points_table, "total_teams": len(points_table)}


@app.get("/api/points-table/{team_code}")
def get_team(team_code: str):
    """Returns points table entry for a specific team e.g. /api/points-table/RCB"""
    team = next((t for t in points_table if t["team"].upper() == team_code.upper()), None)
    if not team:
        return {"error": f"Team '{team_code}' not found"}
    return team


@app.get("/api/top-scorers")
def get_top_scorers():
    """Returns top 5 run scorers of the season"""
    return {"data": top_scorers, "count": len(top_scorers)}


@app.get("/api/top-wicket-takers")
def get_top_wicket_takers():
    """Returns top 5 wicket takers of the season"""
    return {"data": top_wicket_takers, "count": len(top_wicket_takers)}


@app.get("/api/playoffs")
def get_playoffs():
    """Returns all playoff match results including the final"""
    return {"data": playoff_results, "count": len(playoff_results)}


@app.get("/api/highlights")
def get_highlights():
    """Returns season highlights: most sixes, best figures, best SR, best economy"""
    return {"data": season_highlights}
