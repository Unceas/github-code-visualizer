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
- 🔄✅**Day 3**: Web UI with form and trace results
- 📋 **Day 4**: Interactive Web UI
- - 🔄 **Day 4**: Interactive UI with play/pause/step controls
- 📋 **Day 5**: Enhanced Tracer with parameter support
- 📋 **Day 6**: Documentation & Polish
- 📋 **Day 7**: Deployment & CI/CD

## Tech Stack

- **Backend**: FastAPI + Python
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **Core**: sys.settrace for execution tracing
- **Hosting**: Can deploy to any Python-compatible platform

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Local Development

```bash
# Clone the repo
git clone https://github.com/Unceas/github-code-visualizer
cd github-code-visualizer

# Install dependencies
pip install -r requirements.txt

# Run the server
python -m app.server

# Open in browser
# http://localhost:8000
```

## Usage Example

1. Start the server
2. Go to http://localhost:8000
3. Enter a raw GitHub URL: `https://raw.githubusercontent.com/user/repo/branch/path/file.py`
4. Enter the function name (default: `main`)
5. Click "Trace Code"
6. View step-by-step execution with variables!
- 📋 **Day 5**: Enhanced Tracer
- 📋 **Day 6**: Documentation & Polish
- 📋 **Day 7**: Deployment & CI/CD
