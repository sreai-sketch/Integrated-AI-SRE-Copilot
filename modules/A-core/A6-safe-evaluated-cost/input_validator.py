def validate_incident(data):
    missing={"service","pod","reason"}-data.keys()
    if missing: raise ValueError(f"Missing fields: {sorted(missing)}")
