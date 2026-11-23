"""Install and activate scheduled fork updates during the student's initial sync."""

import json
import subprocess
import tempfile

try:
    from .course_automation import COURSE_REPOSITORY, sync_branches
except ImportError:
    from course_automation import COURSE_REPOSITORY, sync_branches


def github(repo_dir, *args, data=None):
    result = subprocess.run(
        ["gh", "api", *args, *(["--input", "-"] if data is not None else [])],
        cwd=repo_dir, input=json.dumps(data) if data is not None else None,
        capture_output=True, text=True, check=False,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "Unable to enable scheduled fork updates.")
    return json.loads(result.stdout) if result.stdout.strip() else {}


def enable_fork_sync(repo_dir):
    """Use the student's existing login; never require a shared instructor token."""
    origin = subprocess.run(
        ["git", "remote", "get-url", "origin"], cwd=repo_dir,
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    # Ignore local test remotes and non-GitHub repositories.
    if not origin.startswith(("https://github.com/", "git@github.com:")):
        return
    slug = origin.removeprefix("https://github.com/").removeprefix("git@github.com:").removesuffix(".git")
    if slug.lower() == COURSE_REPOSITORY.lower():
        return
    metadata = github(repo_dir, f"repos/{slug}")
    if metadata.get("parent", {}).get("full_name", "").lower() != COURSE_REPOSITORY.lower():
        raise RuntimeError("Scheduled sync requires a direct fork of the course repository.")
    # Scheduled workflows run from the default branch, not workspace. Merge both
    # branches without resetting student work before activating the workflow.
    with tempfile.TemporaryDirectory(prefix="enable-course-sync-") as directory:
        sync_branches(directory, f"https://github.com/{COURSE_REPOSITORY}.git", origin)
    settings = github(repo_dir, f"repos/{slug}/actions/permissions")
    if not settings["enabled"]:
        github(repo_dir, f"repos/{slug}/actions/permissions", "--method", "PUT", data={"enabled": True})
    github(repo_dir, f"repos/{slug}/actions/workflows/course-sync.yml/enable", "--method", "PUT")


if __name__ == "__main__":
    import os

    enable_fork_sync(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
