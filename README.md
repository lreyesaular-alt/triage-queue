# Hospital Triage Queue 🏥

A Python-based hospital triage queue management system that prioritizes patients according to medical urgency.

## Features

- Register patients with name, urgency level, and arrival timestamp.
- Manage three priority levels.
- Attend critical patients first.
- Preserve FIFO order within each priority level.
- Display waiting patients.
- View queue statistics.
- Interactive command-line menu.
- Automated unit tests.

## Priority Levels

| Level | Priority |
|---|---|
| 1 | Critical |
| 2 | Urgent |
| 3 | Standard |

## Requirements

Python 3.10 or newer. No external dependencies are required.

## How to Run

```bash
python triage_queue.py
```

## Run Tests

```bash
python -m unittest -v
```

## Project Structure

```text
triage-queue/
├── triage_queue.py
├── test_triage_queue.py
├── DESIGN.md
└── README.md
```

## Implementation

The application uses Python's `deque` data structure to implement efficient FIFO queues for each priority level.

See `DESIGN.md` for architecture decisions and complexity analysis.

## Test Results

Six automated unit tests passed successfully.

## Author

GitHub: lreyesaular-alt