"""Scheduler package for the Nvoid bot."""

from typing import Callable


def schedule_task(task: Callable[[], None], interval_seconds: int) -> None:
    """Schedule a simple recurring task."""
    print(f"Scheduled task {task.__name__} every {interval_seconds} seconds.")
