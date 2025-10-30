import argparse
import json
from fileindexer.modules.indexer import scan_directory
from fileindexer.modules.search import search_by_type

def main():
    parser = argparse.ArgumentParser(description="File Indexer CLI")

    parser.add_argument("--scan", help="Directory to scan")
    parser.add_argument("--search_type", help="Search files by extension")

    args = parser.parse_args()

    if args.scan:
        scan_directory(args.scan)
        print(f"Scanned: {args.scan}")

    if args.search_type:
        result = search_by_type(args.search_type)
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()

