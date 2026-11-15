def verify(ready,desired): return {"healthy":desired>0 and ready==desired,"ready":ready,"desired":desired}
