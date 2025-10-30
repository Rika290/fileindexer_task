import os
from fileindexer.modules.indexer import scan_directory
from fileindexer.modules.search import search_by_type

def test_file_indexing():
    os.makedirs("test_data", exist_ok=True)
    test_file = "test_data/test.txt"

    with open(test_file, "w") as f:
        f.write("hello")

    scan_directory("test_data")

    result = search_by_type(".txt")

    assert len(result) >= 1  

