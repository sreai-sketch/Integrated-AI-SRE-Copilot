"""Plan-only integration: does not write to GitHub."""
def create_pr_plan(branch,title,body): return {"branch":branch,"title":title,"body":body,"status":"plan_only"}
