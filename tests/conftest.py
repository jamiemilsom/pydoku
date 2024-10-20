import pytest
import numpy as np
import pandas as pd
from pathlib import Path

@pytest.fixture
def sample_puzzle_csv(tmp_path):
    """Create a temporary CSV file with sample puzzles."""
    csv_path = tmp_path / "sample_puzzles.csv"
    
    # Sample puzzle and solution
    puzzle = "004300209005009001070060043006002087190007400050083000600000105003508690042910300"
    solution = "864371259325849761971265843436192587198657432257483916689734125713528694542916378"
    
    # Create DataFrame and save to CSV
    df = pd.DataFrame({
        'quizzes': [puzzle],
        'solutions': [solution]
    })
    df.to_csv(csv_path, index=False)
    return csv_path

@pytest.fixture
def sample_puzzle():
    """Return a sample puzzle as numpy array."""
    puzzle = "004300209005009001070060043006002087190007400050083000600000105003508690042910300"
    return np.array([int(x) for x in puzzle]).reshape(9, 9)

@pytest.fixture
def sample_solution():
    """Return the solution to sample puzzle as numpy array."""
    solution = "864371259325849761971265843436192587198657432257483916689734125713528694542916378"
    return np.array([int(x) for x in solution]).reshape(9, 9)

@pytest.fixture
def pydoku_instance(sample_puzzle_csv):
    """Create a Pydoku instance with sample puzzle."""
    from src.pydoku import Pydoku
    return Pydoku(sample_puzzle_csv)