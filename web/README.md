# Daily Sleep/Work Time Visualization

This project visualizes daily time spent on sleep or work using an interactive web-based line chart. Data is loaded from a JSON file (`data.json`) and displayed with **Chart.js**.

## Features

- Converts time strings like `7h30min` into decimal hours.
- Ignores invalid or `"delete"` entries.
- Responsive line chart with gradient fill.
- Tooltips show hours per day.
- Easy to extend for more datasets.

## Requirements

- Python 3 (to serve files locally)
- Modern web browser (Chrome, Firefox, Edge, Safari)
- `data.json` in the same folder as `index.html`

## Installation / Setup

1. Place `index.html` and `data.json` in the same folder.
2. Start a local server using Python:

```bash
python -m http.server 8000
