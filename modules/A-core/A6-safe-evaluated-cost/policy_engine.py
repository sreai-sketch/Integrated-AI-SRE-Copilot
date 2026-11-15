def check_change(resource):
    warnings=[]
    if resource.get("kind") not in {"Deployment","StatefulSet"}: warnings.append("Resource kind needs review")
    return warnings
