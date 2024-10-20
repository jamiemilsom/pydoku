import numpy as np
import pandas as pd
from typing import Optional, Tuple

class Pydoku:
    def __init__(self, puzzle_bank_path: str) -> None:
        """Initialize Sudoku solver with puzzle database.
        
        Args:
            puzzle_bank_path (str): Path to CSV file containing puzzles
        """
        self.puzzle_bank_df = pd.read_csv(puzzle_bank_path)
        self.puzzle_num = 0
        self._load_puzzle(self.puzzle_num)
        
    def _load_puzzle(self, index: int) -> None:
        """Load puzzle and convert to 2D numpy array."""
        puzzle_str = self.puzzle_bank_df['quizzes'][index]
        solution_str = self.puzzle_bank_df['solutions'][index]
        self.puzzle = np.array([int(x) for x in puzzle_str]).reshape(9, 9)
        self.solution = np.array([int(x) for x in solution_str]).reshape(9, 9)
        self.solved = False

    def set_puzzle(self, puzzle_index: int) -> None:
        """Set active puzzle by index."""
        if not isinstance(puzzle_index, int):
            raise TypeError("Puzzle index must be an integer")
        if puzzle_index < 0 or puzzle_index >= len(self.puzzle_bank_df):
            raise ValueError(f"Puzzle index must be between 0 and {len(self.puzzle_bank_df)-1}")
        self.puzzle_num = puzzle_index
        self._load_puzzle(puzzle_index)

    def is_valid(self, num: int, pos: Tuple[int, int], grid: np.ndarray) -> bool:
        """Check if a number is valid in the given position.
        
        Args:
            num (int): Number to check (1-9)
            pos (tuple): (row, col) position to check
            grid (np.ndarray): Current puzzle state
            
        Returns:
            bool: True if the number is valid at the position
        """
        row, col = pos
        
        if num in grid[row]:
            return False
            
        if num in grid[:, col]:
            return False

        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        box = grid[box_row:box_row + 3, box_col:box_col + 3]
        if num in box:
            return False
            
        return True

    def find_empty(self, grid: np.ndarray) -> Optional[Tuple[int, int]]:
        """Find an empty cell in the puzzle.
        
        Args:
            grid (np.ndarray): Current puzzle state
            
        Returns:
            Optional[Tuple[int, int]]: (row, col) of empty cell, or None if no empty cells
        """
        for i in range(9):
            for j in range(9):
                if grid[i, j] == 0:
                    return (i, j)
        return None

    def solve(self) -> bool:
        """Solve the current puzzle using backtracking.
        
        Returns:
            bool: True if solution was found
        """
        empty = self.find_empty(self.puzzle)
        if not empty:
            self.solved = True
            return True
            
        row, col = empty
        
        for num in range(1, 10):
            if self.is_valid(num, (row, col), self.puzzle):
                self.puzzle[row, col] = num
                
                if self.solve():
                    return True
                    
                self.puzzle[row, col] = 0
                
        return False

    def verify_solution(self) -> bool:
        """Verify if current state matches known solution.
        
        Returns:
            bool: True if current state matches solution
        """
        return np.array_equal(self.puzzle, self.solution)

    def show_9x9_grid(self, values: np.ndarray) -> None:
        """Display 9x9 grid with formatting."""
        for i in range(9):
            if i > 0 and i % 3 == 0:
                print('-' * 21)
            row = values[i]
            row_str = ' | '.join(' '.join(str(x) for x in row[j:j+3]) for j in (0,3,6))
            print(row_str)

    def show_puzzle(self) -> None:
        """Display current puzzle state."""
        print("\nPuzzle:")
        self.show_9x9_grid(self.puzzle)

    def show_solution(self) -> None:
        """Display known solution."""
        print("\nSolution:")
        self.show_9x9_grid(self.solution)