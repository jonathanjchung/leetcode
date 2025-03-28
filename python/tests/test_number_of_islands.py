from python.number_of_islands import numIslands


def test_one():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert numIslands(grid) == 1


def test_two():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert numIslands(grid) == 3


def test_three():
    grid = [["1", "1", "1"],
            ["0", "1", "0"],
            ["1", "1", "1"]]
    assert numIslands(grid) == 1


def test_four():
    grid = [
        ["1", "1", "1", "0", "0"],
        ["0", "1", "0", "0", "0"],
        ["1", "1", "1", "0", "1"],
        ["0", "0", "0", "1", "1"]
    ]
    assert numIslands(grid) == 2
