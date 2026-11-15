from pathlib import Path
def read_document(path): return Path(path).read_text(encoding="utf-8")
