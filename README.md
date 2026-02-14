# github-code-visualizer
A Python tool to visualize code execution from GitHub repositories using step-by-step tracing and line-by-line analysis.

## Features

- **CLI Interface (Day 1)**: Fetch Python code from GitHub raw URLs and trace execution line-by-line
- **FastAPI Backend (Day 2)**: REST API endpoints for programmatic access
- **Step-by-step tracing**: See variables and execution flow at each line
- **GitHub integration**: Works with any public Python file on GitHub

## Quick Start

### Installation

```bash
git clone https://github.com/Unceas/github-code-visualizer
cd github-code-visualizer
pip install -r requirements.txt
```

### CLI Usage

```bash
python -m app.main
```

Enter a raw GitHub URL when prompted:
```
https://raw.githubusercontent.com/Unceas/github-code-visualizer/main/examples/sample1.py
```

### FastAPI Backend

```bash
python -m app.server
```

Then visit: http://localhost:8000/docs

**POST /trace**
```json
{
  "github_url": "https://raw.githubusercontent.com/...",
  "func_name": "main"
}
```

## Project Progress

- ✅ **Day 1**: CLI tracer with GitHub fetch
- ✅ **Day 2**: FastAPI backend with /trace endpoint
- 🔄 **Day 3**: Web UI (Basic)
- 📋 **Day 4**: Interactive Web UI
- 📋 **Day 5**: Enhanced Tracer
- 📋 **Day 6**: Documentation & Polish
- 📋 **Day 7**: Deployment & CI/CD
