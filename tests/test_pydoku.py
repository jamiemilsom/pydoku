import pytest
import numpy as np
from src.pydoku import Pydoku

def test_initialization(pydoku_instance, sample_puzzle):
    """Test proper initialization of Pydoku instance."""
    assert isinstance(pydoku_instance, Pydoku)
    assert np.array_equal(pydoku_instance.puzzle, sample_puzzle)
    assert pydoku_instance.puzzle_num == 0
    assert not pydoku_instance.solved

def test_set_puzzle_invalid_index(pydoku_instance):
    """Test setting invalid puzzle indices."""
    with pytest.raises(ValueError):
        pydoku_instance.set_puzzle(-1)
    
    with pytest.raises(ValueError):
        pydoku_instance.set_puzzle(1000000)
    
    with pytest.raises(TypeError):
        pydoku_instance.set_puzzle("not an index")

def test_find_empty(pydoku_instance):
    """Test finding empty cells."""
    # First empty cell in sample puzzle should be at (0, 0)
    empty_pos = pydoku_instance.find_empty(pydoku_instance.puzzle)
    assert empty_pos is not None
    assert empty_pos == (0, 0)
    
    # Test with full grid
    full_grid = np.ones((9, 9))
    assert pydoku_instance.find_empty(full_grid) is None

def test_is_valid(pydoku_instance):
    """Test move validation."""
    # Test valid move
    assert pydoku_instance.is_valid(8, (0, 0), pydoku_instance.puzzle)
    
    # Test invalid row
    pydoku_instance.puzzle[0, 8] = 8
    assert not pydoku_instance.is_valid(8, (0, 0), pydoku_instance.puzzle)
    
    # Test invalid column
    pydoku_instance.puzzle[0, 8] = 0
    pydoku_instance.puzzle[8, 0] = 8
    assert not pydoku_instance.is_valid(8, (0, 0), pydoku_instance.puzzle)
    
    # Test invalid box
    pydoku_instance.puzzle[8, 0] = 0
    pydoku_instance.puzzle[1, 1] = 8
    assert not pydoku_instance.is_valid(8, (0, 0), pydoku_instance.puzzle)

def test_solve(pydoku_instance, sample_solution):
    """Test puzzle solving."""
    assert pydoku_instance.solve()
    assert pydoku_instance.solved
    assert np.array_equal(pydoku_instance.puzzle, sample_solution)

def test_verify_solution(pydoku_instance, sample_solution):
    """Test solution verification."""
    # Initial puzzle should not match solution
    assert not pydoku_instance.verify_solution()
    
    # After solving, should match solution
    pydoku_instance.solve()
    assert pydoku_instance.verify_solution()
    
    # Modify puzzle to not match solution
    pydoku_instance.puzzle[0, 0] = 5
    assert not pydoku_instance.verify_solution()