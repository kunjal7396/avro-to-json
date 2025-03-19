import fastavro
import json
from io import BytesIO

def convert_avro_to_json(avro_file):
    """Convert AVRO file content to JSON."""
    avro_reader = BytesIO(avro_file.getvalue())
    records = []
    
    with fastavro.reader(avro_reader) as reader:
        for record in reader:
            records.append(record)

    return records
