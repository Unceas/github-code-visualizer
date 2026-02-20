# GitHub Code Visualizer - Roadmap

## Project Overview

A 7-day sprint to build a Python tool that visualizes code execution from GitHub repositories with step-by-step tracing and interactive visualization.

---

## ✅ Completed

### Day 1: CLI Tracer (Completed)
**Goal**: Build core execution tracer
- ✅ Created CLI interface
- ✅ Implemented sys.settrace tracing
- ✅ Fetch code from GitHub raw URLs
- ✅ Display step-by-step execution
- **Commits**: Initial CLI tracer with GitHub fetch

### Day 2: FastAPI Backend (Completed)
**Goal**: Wrap CLI tracer as REST API
- ✅ Added FastAPI server
- ✅ Created `/trace` POST endpoint
- ✅ Proper error handling with HTTP exceptions
- ✅ Pydantic models for request/response
- **Commits**: Day 2: Add FastAPI backend with /trace endpoint

### Day 3: Web UI - Basic (Completed)
**Goal**: Create user-friendly web interface
- ✅ Beautiful HTML/CSS frontend
- ✅ Form for GitHub URL and function name input
- ✅ Real-time validation
- ✅ Async JavaScript to call `/trace` API
- ✅ Display trace results in cards
- ✅ Error messages with user-friendly alerts
- ✅ Static file serving from FastAPI
- **Commits**: 
  - Day 3: Add beautiful web UI with form and trace display
  - Day 3: Mount static files for web UI
  - Day 3: Update README - Mark Day 3 complete

---

## 🔄 In Progress

### Day 4: Web UI - Interactive (Next)
**Goal**: Add step-by-step execution controls

**Features to Add**:
1. **Play/Pause Button**
   - Auto-play through steps with configurable speed
   - Pause and resume at any point
   
2. **Step Controls**
   - Previous/Next step buttons
   - Jump to specific step number
   - Progress bar showing current position
   
3. **Enhanced Display**
   - Highlight current step visually
   - Show variable changes between steps
   - Display function call stack
   - Timeline of execution
   
4. **Speed Control**
   - Slider to adjust playback speed (0.5x - 2x)
   - Slow-motion for better learning

**Implementation Plan**:
- Update `static/index.html` with new controls
- Add JavaScript for state management (current step, playing, speed)
- Enhance CSS with timeline/progress visualization
- Add keyboard shortcuts (Space for play/pause, arrows for next/prev)

**Estimated Time**: 1-2 hours

---

## 📋 Planned

### Day 5: Enhanced Tracer
**Goal**: Support more Python features
- Support functions with parameters and return values
- Better error handling and edge cases
- Support for loops and conditional branches
- Track exception handling

### Day 6: Documentation & Polish
**Goal**: Professional project presentation
- Write comprehensive documentation
- Add demo GIFs/screenshots
- Create example files
- Add contributing guidelines
- Setup CI/CD workflows

### Day 7: Deployment & Polish
**Goal**: Make it production-ready and accessible
- Deploy to Render/Heroku
- Add GitHub Actions for testing
- Docker support
- Performance optimizations
- Public demo link

---

## Tech Stack

- **Backend**: FastAPI, Python 3.8+
- **Frontend**: Vanilla HTML5, CSS3, JavaScript (ES6+)
- **Core**: `sys.settrace` for execution tracing
- **Deployment**: Can deploy to any Python-compatible platform

---

## How to Use (Current State)

```bash
# Clone the repo
git clone https://github.com/Unceas/github-code-visualizer
cd github-code-visualizer

# Install dependencies
pip install -r requirements.txt

# Run the server
python -m app.server

# Open browser
# http://localhost:8000
```

---

## Learning Outcomes

This project demonstrates:
- ✅ Python execution tracing with sys.settrace
- ✅ RESTful API design with FastAPI
- ✅ Frontend-Backend integration
- ✅ Interactive UI/UX development
- ✅ Software project management
- ✅ Git workflow and documentation

---

## Metrics

- **Lines of Code**: ~1500+ (Python + JS)
- **Days to Complete**: 7
- **GitHub Commits**: 10+
- **Features Implemented**: 15+

---

## Status: Active 🟢

**Latest Update**: February 20, 2026

### ✅ Status Update
- Day 1-3: Fully completed and tested ✅
- Web UI is live and functional at http://localhost:8000
- API endpoints tested and working
- All static files properly mounted
- Ready to begin Day 4: Interactive controls

### 🚀 Next Immediate Steps (Day 4)
1. Add Play/Pause button functionality
2. Implement step controls (Previous/Next/Jump)
3. Add speed slider for playback
4. Create progress bar visualization
5. Add keyboard shortcuts

Estimated completion: Next session

Last Updated: February 19, 2026
Next Update: Day 4 completion
