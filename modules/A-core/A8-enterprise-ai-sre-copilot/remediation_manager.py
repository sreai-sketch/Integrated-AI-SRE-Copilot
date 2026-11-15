def prepare_proposal(diagnosis,proposed_yaml,rollback_yaml):
    return {"diagnosis":diagnosis,"proposed_yaml":proposed_yaml,"rollback_yaml":rollback_yaml,
            "executed":False,"approval_required":True}
