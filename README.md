# game-testing-ai

> 🚧 Geliştirme aşamasında

An AI system that plays a 2D game and automatically detects bugs.

## Overview
- A simple grid-based 2D game built with **Pygame**, with intentionally planted bugs
- Exploration agents: a **random agent** and a **reinforcement learning agent** (PPO + novelty-based exploration reward)
- An **oracle layer** that detects crashes, softlocks, and invariant violations
- Reproducible bug reports (seed + action log) and a **Streamlit dashboard**

## Results
_Coming soon._

## Setup
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
```

## Roadmap
See [ROADMAP.md](ROADMAP.md).
