"""Automated test suite for Streaming Columnar Chunker."""
import unittest
from agent_streaming_parquet_chunker.core import StreamingColumnarChunker

class TestStreamingColumnarChunker(unittest.TestCase):
    def test_chunking_and_formatting(self):
        chunker = StreamingColumnarChunker(max_rows_per_chunk=2)
        schema = ["a", "b"]
        records = [{"a": 1, "b": 2}, {"a": 3, "b": 4}, {"a": 5, "b": 6}]
        chunks = chunker.chunk_records(schema, records)

        self.assertEqual(len(chunks), 2)
        self.assertEqual(len(chunks[0].rows), 2)
        self.assertEqual(len(chunks[1].rows), 1)
        self.assertIn("### Chunk 1", chunks[0].to_formatted_text())
