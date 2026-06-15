from pathlib import Path

def load_repo_text(repo_path=".", max_files=30):
    repo = Path(repo_path)
    files = []

    for f in repo.rglob("*"):
        if len(files) >= max_files:
            break

        if f.is_file():
            if ".git" in str(f):
                continue

            try:
                content = f.read_text(errors="ignore")
                files.append({
                    "path": str(f),
                    "content": content[:3000]
                })
            except:
                pass

    return files