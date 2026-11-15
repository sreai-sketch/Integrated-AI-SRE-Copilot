def validate_diagnosis(data):
    required={"summary","possible_cause","recommended_checks"}
    if required-data.keys(): raise ValueError("Diagnosis is missing required fields")
    if not isinstance(data["recommended_checks"],list): raise ValueError("recommended_checks must be a list")
