# Design Notes: Triage Queue

## Overview

This project implements a hospital triage queue using Python. Patients are attended according to their urgency level, while maintaining arrival order among patients with the same priority.

## Data Structures

The implementation uses a dictionary containing three `deque` collections from Python's `collections` module.

- **Level 1:** Critical patients, highest priority.
- **Level 2:** Urgent patients.
- **Level 3:** Standard patients, lowest priority.

Each level follows the FIFO (First In, First Out) principle.

## Classes

### Patient

Stores the patient's name, triage level, and arrival timestamp. It validates the name and urgency level.

### TriageQueue

Manages patient registration and attention through five operations:

- `enqueue()`: Adds a patient to the appropriate priority queue.
- `dequeue()`: Removes and returns the highest-priority waiting patient.
- `peek()`: Returns the next patient without removing them.
- `list_queue()`: Lists patients in attention order.
- `stats()`: Returns the number of waiting patients per priority level.

## Time Complexity

| Operation | Complexity |
|---|---|
| enqueue | O(1) |
| dequeue | O(1) |
| peek | O(1) |
| list_queue | O(n) |
| stats | O(1) |

There are always three priority levels, so checking them takes constant time.

## Edge Cases

The implementation handles empty queues, invalid priority levels, empty patient names, and FIFO ordering within the same priority level.

## Testing

Six automated unit tests verify priority ordering, FIFO behavior, peek functionality, empty queues, statistics, and invalid priority levels.

All six tests passed successfully.