# app/main.py
import runpy
import types
from typing import List

from .github_client import fetch_code_from_raw_url
from .tracer import trace_function, steps_to_dict_list

def load_function_from_code(code: str, func_name: str = "main"):
    module_dict = {}
    exec(code, module_dict)
    func = module_dict.get(func_name)
    if not isinstance(func, types.FunctionType):
        raise ValueError(f"Function '{func_name}' not found in code.")
    return func

def main():
    raw_url = input("Enter raw GitHub URL to a .py file: ").strip()
    func_name = input("Enter function name to run (default: main): ").strip() or "main"

    print("\nFetching code...")
    code = fetch_code_from_raw_url(raw_url)

    print("Loading function...")
    func = load_function_from_code(code, func_name)

    print("Tracing execution...\n")
    steps = trace_function(func)

    dict_steps: List[dict] = steps_to_dict_list(steps)
    for i, step in enumerate(dict_steps, start=1):
        print(f"Step {i}:")
        print(f"  event:     {step['event']}")
        print(f"  line_no:   {step['line_no']}")
        print(f"  func_name: {step['func_name']}")
        print(f"  locals:    {step['locals']}")
        print()

if __name__ == "__main__":
    main()
