import subprocess
import json
import os
import sys
import re

def run_cmd(cmd, cwd=None):
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            shell=True,
            check=False
        )
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return 1, "", str(e)

def scan_credential_leaks(repo_path):
    patterns = [
        r"(?i)(api[_-]?key|secret[_-]?key|auth[_-]?token|password|private[_-]?key)\s*[:=]\s*['\"]?[A-Za-z0-9%_\-]{16,}['\"]?",
        r"sk-[A-Za-z0-9]{24,}",
        r"ghp_[A-Za-z0-9]{36,}"
    ]
    leaks = []
    
    # Check untracked and modified files
    code, out, _ = run_cmd("git status --porcelain", cwd=repo_path)
    if code == 0 and out:
        lines = out.splitlines()
        for line in lines:
            status = line[:2].strip()
            filepath = line[3:].strip()
            full_path = os.path.join(repo_path, filepath)
            
            # Skip ignored or binary or common safe files
            if filepath.startswith(".git") or filepath.endswith((".png", ".jpg", ".docx", ".pdf")):
                continue
                
            if os.path.isfile(full_path):
                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        for pattern in patterns:
                            matches = re.findall(pattern, content)
                            if matches:
                                leaks.append(f"Potential secret pattern found in file: {filepath}")
                                break
                except Exception:
                    pass
    return leaks

def check_fiction_updates():
    repo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    
    # Verify git repo
    code, branch, _ = run_cmd("git rev-parse --abbrev-ref HEAD", cwd=repo_path)
    if code != 0:
        return {
            "status": "error",
            "message": "Directory is not a valid git repository",
            "repo_path": repo_path
        }
    
    # Credential scan
    leaks = scan_credential_leaks(repo_path)
    if leaks:
        return {
            "status": "security_warning",
            "message": "Potential credential leaks detected in local changes!",
            "leaks": leaks,
            "can_update": False
        }
        
    # Fetch remote
    code, _, err = run_cmd("git fetch origin", cwd=repo_path)
    if code != 0:
        return {
            "status": "error",
            "message": f"Failed to fetch from remote origin: {err}",
            "repo_path": repo_path
        }
        
    # Compare local vs remote
    code, local_hash, _ = run_cmd("git rev-parse HEAD", cwd=repo_path)
    code, remote_hash, _ = run_cmd(f"git rev-parse origin/{branch}", cwd=repo_path)
    
    if local_hash == remote_hash:
        return {
            "status": "up_to_date",
            "message": "Fiction Book Agent Skills is up to date.",
            "branch": branch,
            "local_hash": local_hash[:7],
            "has_updates": False
        }
        
    # Get commit log behind
    code, log_out, _ = run_cmd(f"git log HEAD..origin/{branch} --oneline", cwd=repo_path)
    commits = log_out.splitlines() if log_out else []
    
    return {
        "status": "update_available",
        "message": f"New updates available for Fiction Book Agent Skills on branch '{branch}'!",
        "branch": branch,
        "local_hash": local_hash[:7],
        "remote_hash": remote_hash[:7],
        "commits_behind": len(commits),
        "commit_log": commits,
        "has_updates": True,
        "can_update": True
    }

if __name__ == "__main__":
    res = check_fiction_updates()
    print(json.dumps(res, indent=2))
