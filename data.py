# IPL 2025 Season Data

season_summary = {
    "season": "IPL 2025",
    "total_matches": 74,
    "winner": {
        "team": "Royal Challengers Bengaluru",
        "short": "RCB"
    },
    "orange_cap": {
        "player": "Virat Kohli",
        "team": "RCB",
        "runs": 741
    },
    "purple_cap": {
        "player": "Jasprit Bumrah",
        "team": "MI",
        "wickets": 28
    },
    "highest_team_score": {
        "score": "286/4",
        "match": "SRH vs MI"
    }
}

points_table = [
    {"rank": 1, "team": "RCB", "full_name": "Royal Challengers Bengaluru", "color": "#C71C23", "matches": 14, "won": 9, "lost": 5, "nrr": "+0.48", "points": 18, "qualified": True},
    {"rank": 2, "team": "MI",  "full_name": "Mumbai Indians",              "color": "#004C93", "matches": 14, "won": 9, "lost": 5, "nrr": "+0.31", "points": 18, "qualified": True},
    {"rank": 3, "team": "CSK", "full_name": "Chennai Super Kings",         "color": "#FDB913", "matches": 14, "won": 8, "lost": 6, "nrr": "+0.21", "points": 16, "qualified": True},
    {"rank": 4, "team": "SRH", "full_name": "Sunrisers Hyderabad",         "color": "#FF822A", "matches": 14, "won": 8, "lost": 6, "nrr": "+0.14", "points": 16, "qualified": True},
    {"rank": 5, "team": "DC",  "full_name": "Delhi Capitals",              "color": "#1D4289", "matches": 14, "won": 7, "lost": 7, "nrr": "-0.09", "points": 14, "qualified": False},
    {"rank": 6, "team": "KKR", "full_name": "Kolkata Knight Riders",       "color": "#3A225D", "matches": 14, "won": 7, "lost": 7, "nrr": "-0.17", "points": 14, "qualified": False},
    {"rank": 7, "team": "LSG", "full_name": "Lucknow Super Giants",        "color": "#45B4C5", "matches": 14, "won": 6, "lost": 8, "nrr": "-0.22", "points": 12, "qualified": False},
    {"rank": 8, "team": "RR",  "full_name": "Rajasthan Royals",            "color": "#EA1A85", "matches": 14, "won": 5, "lost": 9, "nrr": "-0.35", "points": 10, "qualified": False},
    {"rank": 9, "team": "PBKS","full_name": "Punjab Kings",                "color": "#0078BC", "matches": 14, "won": 5, "lost": 9, "nrr": "-0.38", "points": 10, "qualified": False},
    {"rank":10, "team": "GT",  "full_name": "Gujarat Titans",              "color": "#D71920", "matches": 14, "won": 4, "lost":10, "nrr": "-0.61", "points":  8, "qualified": False},
]

top_scorers = [
    {"rank": 1, "player": "Virat Kohli",     "initials": "VK", "team": "RCB",  "runs": 741},
    {"rank": 2, "player": "Shubman Gill",    "initials": "SG", "team": "GT",   "runs": 694},
    {"rank": 3, "player": "Ruturaj Gaikwad", "initials": "RG", "team": "CSK",  "runs": 652},
    {"rank": 4, "player": "Kumar Abhishek",  "initials": "KA", "team": "LSG",  "runs": 618},
    {"rank": 5, "player": "Hardik Pandya",   "initials": "HH", "team": "MI",   "runs": 589},
]

top_wicket_takers = [
    {"rank": 1, "player": "Jasprit Bumrah",  "initials": "JB", "team": "MI",   "wickets": 28},
    {"rank": 2, "player": "Yuzvendra Chahal","initials": "YC", "team": "PBKS", "wickets": 24},
    {"rank": 3, "player": "Varun Chakravarthy","initials":"MV", "team": "KKR", "wickets": 22},
    {"rank": 4, "player": "Akeal Hosein",    "initials": "AK", "team": "SRH",  "wickets": 21},
    {"rank": 5, "player": "Kuldeep Yadav",   "initials": "KY", "team": "DC",   "wickets": 20},
]

playoff_results = [
    {
        "stage": "Qualifier 1",
        "team1": "RCB", "score1": "187/5",
        "team2": "MI",  "score2": "164/9",
        "winner": "RCB", "result": "RCB won by 23 runs"
    },
    {
        "stage": "Eliminator",
        "team1": "CSK", "score1": "172/6",
        "team2": "SRH", "score2": "168/8",
        "winner": "CSK", "result": "CSK won by 4 runs"
    },
    {
        "stage": "Qualifier 2",
        "team1": "CSK", "score1": "189/4",
        "team2": "MI",  "score2": "182/7",
        "winner": "CSK", "result": "CSK won by 7 runs"
    },
    {
        "stage": "Final",
        "venue": "Narendra Modi Stadium",
        "team1": "RCB", "score1": "201/5",
        "team2": "CSK", "score2": "196/7",
        "winner": "RCB", "result": "RCB won by 5 runs"
    },
]

season_highlights = [
    {"category": "Most Sixes",                    "player": "Hardik Pandya",       "team": "MI",   "value": "54 sixes"},
    {"category": "Best Bowling Figures",          "player": "Jasprit Bumrah",      "team": "MI",   "value": "5/10 vs RCB"},
    {"category": "Best Strike Rate (min 200 runs)","player": "Sanju Samson",       "team": "RR",   "value": "SR 184.3"},
    {"category": "Best Economy (min 10 overs)",   "player": "Ravi Bishnoi",        "team": "LSG",  "value": "Econ 6.84"},
]
