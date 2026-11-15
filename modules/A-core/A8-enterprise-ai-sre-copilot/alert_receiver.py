def normalize_alert(payload):
    return {k:payload.get(k) for k in ("service","pod","reason","exit_code")}
