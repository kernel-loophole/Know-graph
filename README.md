# Graph Processor

## Introduction

This Python script, `graph_processor.py`, is designed to process graph data stored in a JSON file and perform Breadth-First Search (BFS) related operations.

## Features

- **Build Graph from JSON:** Reads a JSON file containing node and edge information and builds a graph structure.

- **BFS Related Nodes:** Performs BFS traversal starting from a specified keyword and returns the matching nodes.

- **Get Labels by IDs:** Retrieves labels for given node IDs.

## Requirements

- Python 3.x
- `graph_show` 
## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/kernel-loophole/Know-graph.git
    cd Know-graph
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:

    ```bash
    python graph_processor.py
    ```

## Usage

1. Ensure you have a valid `graph_data.json` file containing node and edge information.

2. Instantiate the `GraphProcessor` class with the JSON file path:

    ```python
    processor = GraphProcessor('graph_data.json')
    ```

3. Use the provided methods:

    ```python
    keyword_id = processor.find_matching_id('YourKeyword')
    related_ids = processor.bfs_related_nodes(keyword_id)
    matching_labels = processor.get_labels_by_ids(related_ids)
    ```

## Example

```python
processor = GraphProcessor('graph_data.json')
json_data = read_json_file('graph_data.json')
keyword_id = find_matching_id(json_data, 'Colombo')
related_ids = processor.bfs_related_nodes(keyword_id)
matching_labels = processor.get_labels_by_ids(related_ids)

print("Matching labels:")
print(matching_labels)
