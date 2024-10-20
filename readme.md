# Pydoku

A Simple Python-based Sudoku solver using backtracking algorithm.

## Installation

```bash
git clone https://github.com/yourusername/pydoku.git
cd pydoku
pip install -e .
```

## Usage

```python
from pydoku import Pydoku

# Initialize solver with the puzzle database
solver = Pydoku('puzzles.csv')

# Change the puzzle to any number in the puzzle database
solver.set_puzzle(20)

# Show the puzzle in a 9x9 grid if you want to give it a go
solver.show_puzzle()

# Solve current puzzle
solver.solve()

# Display solution
solver.show_solution()
```

## Development

Run tests:
```bash
pytest tests/ -v
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.