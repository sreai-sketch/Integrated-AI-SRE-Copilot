def recent_logs(text,max_lines=20): return [x for x in text.splitlines() if x.strip()][-max_lines:]
