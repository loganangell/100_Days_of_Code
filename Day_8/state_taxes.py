"""

State Lottery Tax Rates
This module contains a dictionary of U.S. states with their corresponding lottery tax rates.
Each state is represented by its two-letter code, full name, and lottery tax rate percentage.
States that do not allow lottery play have a tax rate of None.
Data as of 2024 - https://blog.jackpocket.com/how-are-lottery-winnings-taxed-by-state/


"""

lottery_tax_rates = {
    "AL": {"name": "Alabama", "rate_pct": None}, # Does not allow lottery play
    "AK": {"name": "Alaska", "rate_pct": None}, # Does not allow lottery play
    "AZ": {"name": "Arizona", "rate_pct": 4.8},
    "AR": {"name": "Arkansas", "rate_pct": 4.4},
    "CA": {"name": "California", "rate_pct": 0.0},
    "CO": {"name": "Colorado", "rate_pct": 4.0},
    "CT": {"name": "Connecticut", "rate_pct": 6.99},
    "DC": {"name": "Washington, DC", "rate_pct": 8.5},
    "DE": {"name": "Delaware", "rate_pct": 6.6},
    "FL": {"name": "Florida", "rate_pct": 0.0},
    "GA": {"name": "Georgia", "rate_pct": 5.49},
    "HI": {"name": "Hawaii", "rate_pct": None}, # Does not allow lottery play
    "ID": {"name": "Idaho", "rate_pct": 6.93},
    "IL": {"name": "Illinois", "rate_pct": 4.95},
    "IN": {"name": "Indiana", "rate_pct": 3.23},
    "IA": {"name": "Iowa", "rate_pct": 5.0},
    "KS": {"name": "Kansas", "rate_pct": 5.0},
    "KY": {"name": "Kentucky", "rate_pct": 6.0},
    "LA": {"name": "Louisiana", "rate_pct": 4.25},
    "ME": {"name": "Maine", "rate_pct": 7.15},
    "MD": {"name": "Maryland", "rate_pct": 8.75},
    "MA": {"name": "Massachusetts", "rate_pct": 5.0},
    "MI": {"name": "Michigan", "rate_pct": 4.25},
    "MN": {"name": "Minnesota", "rate_pct": 7.25},
    "MS": {"name": "Mississippi", "rate_pct": 3.0},
    "MO": {"name": "Missouri", "rate_pct": 4.0},
    "MT": {"name": "Montana", "rate_pct": 6.9},
    "NE": {"name": "Nebraska", "rate_pct": 5.0},
    "NV": {"name": "Nevada", "rate_pct": None}, # Does not allow lottery play
    "NH": {"name": "New Hampshire", "rate_pct": 0.0},
    "NJ": {"name": "New Jersey", "rate_pct": 8.0},
    "NM": {"name": "New Mexico", "rate_pct": 6.0},
    "NY": {"name": "New York", "rate_pct": 10.9},
    "NC": {"name": "North Carolina", "rate_pct": 4.75},
    "ND": {"name": "North Dakota", "rate_pct": 2.9},
    "OH": {"name": "Ohio", "rate_pct": 4.0},
    "OK": {"name": "Oklahoma", "rate_pct": 4.75},
    "OR": {"name": "Oregon", "rate_pct": 8.0},
    "PA": {"name": "Pennsylvania", "rate_pct": 3.07},
    "RI": {"name": "Rhode Island", "rate_pct": 5.99},
    "SC": {"name": "South Carolina", "rate_pct": 7.0},
    "SD": {"name": "South Dakota", "rate_pct": 0.0},
    "TN": {"name": "Tennessee", "rate_pct": 0.0},
    "TX": {"name": "Texas", "rate_pct": 0.0},
    "UT": {"name": "Utah", "rate_pct": None}, # Does not allow lottery play
    "VT": {"name": "Vermont", "rate_pct": 6.0},
    "VA": {"name": "Virginia", "rate_pct": 4.0},
    "WA": {"name": "Washington", "rate_pct": 0.0},
    "WV": {"name": "West Virginia", "rate_pct": 6.5},
    "WI": {"name": "Wisconsin", "rate_pct": 7.65},
    "WY": {"name": "Wyoming", "rate_pct": 0.0}
}
