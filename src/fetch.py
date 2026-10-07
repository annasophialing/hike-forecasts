import requests
import pandas as pd

def fetch_history(lat, lon, start="2015-01-01", end="2025-12-31"):
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start,
        "end_date": end,
        "hourly": "temperature_2m,precipitation,cloud_cover,wind_speed_10m,relative_humidity_2m",
        "timezone": "auto",
    }
    r = requests.get(url, params=params, timeout=60)
    r.raise_for_status()
    df = pd.DataFrame(r.json()["hourly"])
    df["time"] = pd.to_datetime(df["time"])
    return df