# app/tracer.py
import sys
from dataclasses import dataclass, asdict
from types import FrameType
from typing import Any, Dict, List, Callable

@dataclass
class TraceStep:
    event: str
    line_no: int
    func_name: str
    locals: Dict[str, Any]

def _make_trace_step(frame: FrameType, event: str) -> TraceStep:
    return TraceStep(
        event=event,
        line_no=frame.f_lineno,
        func_name=frame.f_code.co_name,
        locals={k: repr(v) for k, v in frame.f_locals.items()},
    )

def trace_function(func: Callable, *args, **kwargs) -> List[TraceStep]:
    steps: List[TraceStep] = []

    def tracer(frame: FrameType, event: str, arg):
        if event in ("line", "return"):
            steps.append(_make_trace_step(frame, event))
        return tracer

    old_trace = sys.gettrace()
    try:
        sys.settrace(tracer)
        func(*args, **kwargs)
    finally:
        sys.settrace(old_trace)

    return steps

def steps_to_dict_list(steps: List[TraceStep]) -> List[Dict[str, Any]]:
    return [asdict(s) for s in steps]
