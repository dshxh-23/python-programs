import pytest
from problem import numCells


def test_numCells():
    assert numCells([[1,2,3], [4,9,5], [6,7,8], [9]]) == 2
    assert numCells([[3]]) == 1
    assert numCells([[9,9,9], [1,8,7], [3,9,8], [3,3,9], [1,6,8]]) == 0
    assert numCells([[3,2,5,6], [1,1,8], [5,9,4], [5,7,3,9,4], [6,4,2,2,8,6,7,1], [4,3,8], [9]]) == 6
    