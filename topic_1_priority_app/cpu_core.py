"""Data, FCFS/SJF/SRTF, and metrics for a single CPU."""

from dataclasses import dataclass
from typing import Callable

MAX_JOBS = 60
MAX_TIME = 1_000_000
INPUT_ORDER = "Input order"
PROCESS_ID = "Process ID"


@dataclass(frozen=True)
class Process:
    pid: str
    arrival: int
    burst: int
    priority: int = 0


@dataclass(frozen=True)
class Slice:
    pid: str | None   # None marks CPU idle time.
    start: int
    end: int
    remaining: int | None = None


@dataclass(frozen=True)
class Metrics:
    process: Process
    completion: int
    turnaround: int
    waiting: int
    response: int


@dataclass(frozen=True)
class Schedule:
    name: str
    slices: list[Slice]
    metrics: list[Metrics]
    detail: str

    @property
    def averages(self) -> tuple[float, float, float]:
        count = len(self.metrics)
        return (
            sum(row.turnaround for row in self.metrics) / count,
            sum(row.waiting for row in self.metrics) / count,
            sum(row.response for row in self.metrics) / count,
        )


