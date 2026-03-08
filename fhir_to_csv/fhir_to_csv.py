import json
import csv

def parse_fhir_bundle(bundle_path: str, output_path: str):
    """
    Parse a FHIR JSON bundle and convert it into CSV format.
    """
    with open(bundle_path, "r") as f:
        data = json.load(f)

    # TODO: implement flattening logic
    with open(output_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id", "resourceType", "field1", "field2"])  # example header
        # writer.writerow([...])
