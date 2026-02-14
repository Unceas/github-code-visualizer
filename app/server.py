# app/server.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any

from .github_client import fetch_code_from_raw_url, GitHubFetchError
from .tracer import trace_function, steps_to_dict_list, TraceStep

app = FastAPI(
    title="GitHub Code Visualizer",
    description="Visualize Python code execution from GitHub repositories",
    version="1.0.0"
)

class TraceRequest(BaseModel):
    github_url: str
    func_name: str = "main"

class TraceResponse(BaseModel):
    success: bool
    steps: List[Dict[str, Any]] = []
    error: str = None

@app.get("/")
def read_root():
    return {
        "message": "GitHub Code Visualizer API",
        "endpoints": {
            "POST /trace": "Trace a function from a GitHub repository",
            "GET /docs": "API documentation"
        }
    }

@app.post("/trace", response_model=TraceResponse)
def trace_endpoint(request: TraceRequest):
    try:
        # Fetch code from GitHub
        code = fetch_code_from_raw_url(request.github_url)
        
        # Load the function from code
        module_dict = {}
        exec(code, module_dict)
        func = module_dict.get(request.func_name)
        
        if func is None:
            raise ValueError(f"Function '{request.func_name}' not found in code")
        
        if not callable(func):
            raise ValueError(f"'{request.func_name}' is not callable")
        
        # Trace the function
        steps = trace_function(func)
        dict_steps = steps_to_dict_list(steps)
        
        return TraceResponse(
            success=True,
            steps=dict_steps
        )
    
    except GitHubFetchError as e:
        raise HTTPException(status_code=400, detail=f"GitHub fetch error: {str(e)}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Code error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Execution error: {str(e)}")

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
