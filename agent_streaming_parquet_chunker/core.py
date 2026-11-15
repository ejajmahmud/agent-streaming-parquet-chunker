"""Core streaming columnar chunker implementation."""
from typing import List, Dict, Any

class ColumnarChunk:
    def __init__(self, chunk_id: int, schema: List[str], rows: List[List[Any]]):
        self.chunk_id = chunk_id
        self.schema = schema
        self.rows = rows

    def to_formatted_text(self) -> str:
        header = " | ".join(self.schema)
        sep = " | ".join(["---"] * len(self.schema))
        row_lines = [" | ".join(str(item) for item in r) for r in self.rows]
        return "\n".join([f"### Chunk {self.chunk_id}", header, sep] + row_lines)

class StreamingColumnarChunker:
    def __init__(self, max_rows_per_chunk: int = 5):
        self.max_rows = max_rows_per_chunk

    def chunk_records(self, schema: List[str], records: List[Dict[str, Any]]) -> List[ColumnarChunk]:
        chunks = []
        curr_rows = []
        chunk_idx = 1

        for r in records:
            row_vals = [r.get(col, "") for col in schema]
            curr_rows.append(row_vals)
            if len(curr_rows) >= self.max_rows:
                chunks.append(ColumnarChunk(chunk_idx, schema, curr_rows))
                chunk_idx += 1
                curr_rows = []

        if curr_rows:
            chunks.append(ColumnarChunk(chunk_idx, schema, curr_rows))

        return chunks
