import fastavro
import json
from io import BytesIO

def convert_avro_to_json(avro_file):
    """Convert AVRO file content to JSON."""
    avro_reader = BytesIO(avro_file.getvalue())  # Read uploaded file into BytesIO
    
    try:
        records = []
        reader = fastavro.reader(avro_reader)  # Create AVRO reader
        for record in reader:
            records.append(record)
        return records  # Return JSON-compatible list of records
    except Exception as e:
        return {"error": str(e)}  # Return error message for debugging
