# Thermal Power Plant Simulator

**Fall 2026**  
Official course website for the *Thermal Power Plant Simulator* course.

This website was built using [Quarto](https://quarto.org) with Python dependencies managed by [`uv`](https://github.com/astral-sh/uv).

## Features

- Clean, professional course website
- Lecture and laboratory materials
- Executable Python simulations including Rankine cycle calculations and performance analysis
- Responsive design with smooth scrolling

## Development Workflow

### Prerequisites

- [Quarto](https://quarto.org) installed
- [uv](https://github.com/astral-sh/uv) installed (for Python environment management)

### Initial Setup

```bash
# Clone the repository
git clone https://github.com/volumen25/thermal-power-plant-simulator.git
cd thermal-power-plant-simulator
```

### Install Python Dependencies

```bash
uv sync
uv sync --group dev
```

### Preview Website

```bash
uv run quarto preview
```

### Render Static Site

```bash
uv run quarto render
```
