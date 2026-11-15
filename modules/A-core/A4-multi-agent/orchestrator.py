from investigation_agent import run as investigate
from knowledge_agent import run as knowledge
from rca_agent import run as rca
from remediation_agent import run as remediate
def run_team(incident):
    i=investigate(incident); k=knowledge(incident)
    r=rca(i["content"],k["content"]); m=remediate(r["content"])
    return [i,k,r,m]
if __name__=="__main__":
    for item in run_team({"reason":"OOMKilled","exit_code":137}): print(item)
