"""Rank each ready process by its assigned priority."""

from cpu_core import Process, Schedule, schedule_by_rank, summarize

NON_PREEMPTIVE = "Non-preemptive"
PREEMPTIVE = "Preemptive"
LOW_FIRST = "Smaller number first"
HIGH_FIRST = "Larger number first"
