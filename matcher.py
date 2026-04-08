"""Match jobs to candidate profiles."""

from typing import Dict


def match_job_to_candidate(job: Dict[str, str], candidate_profile: Dict[str, str]) -> bool:
    """Return True when a job matches the simple candidate profile."""
    title = job.get("title", "").lower()
    skills = candidate_profile.get("skills", "").lower().split(",")
    return any(skill.strip() and skill.strip() in title for skill in skills)
