def unsupported_claims(claims,evidence):
    text=" ".join(evidence).lower()
    return [c for c in claims if c.lower() not in text]
