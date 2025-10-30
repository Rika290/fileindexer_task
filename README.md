# File Indexer

## Description:
This Python package scans a directory and indexes file metadata, including file name, size, type, dates, and checksum. It supports searching files by extension and exporting results in JSON format.

## Folder Structure:
fileindexer/
├── modules/
│ ├── init.py
│ ├── indexer.py
│ └── search.py
├── cli.py
tests/

## Usage: 
- python -m fileindexer.cli --scan testfolder
- python -m fileindexer.cli --search_type .txt

## Notes:
- Only basic unit tests are included.
- Docker containerization not included.
