"""CLI for Streaming Columnar Chunker."""
import argparse
from .core import StreamingColumnarChunker

def main():
    parser = argparse.ArgumentParser(description="Streaming Columnar Chunker CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate tabular chunking")
    args = parser.parse_args()

    chunker = StreamingColumnarChunker(max_rows_per_chunk=2)
    schema = ["id", "status", "latency_ms"]
    records = [
        {"id": 1, "status": "ok", "latency_ms": 12},
        {"id": 2, "status": "ok", "latency_ms": 15},
        {"id": 3, "status": "err", "latency_ms": 120},
    ]

    chunks = chunker.chunk_records(schema, records)
    for c in chunks:
        print(c.to_formatted_text())
        print()

if __name__ == "__main__":
    main()
