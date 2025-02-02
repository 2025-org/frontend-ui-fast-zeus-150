from base64 import b64decode, b64encode
from json import dumps, loads
from zlib import compress, decompress

def compress_json(obj) -> str:
    obj_json = dumps(obj)
    encoded_obj_json = obj_json.encode(encoding="utf-8")
    compressed_json = compress(encoded_obj_json)
    b64_compressed_json = b64encode(compressed_json)
    return b64_compressed_json.decode("utf-8")

# Load JSON data from a file
def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return loads(file.read())

# Save the compressed JSON data to a file
def save_compressed_json(file_path, compressed_data):
    with open(file_path, 'w') as file:
        file.write(compressed_data)

# Main function to read, compress, and save JSON data
def main(input_file_path, output_file_path):
    json_data = load_json_file(input_file_path)
    compressed_data = compress_json(json_data)
    save_compressed_json(output_file_path, compressed_data)
    print(f"Compressed data saved to {output_file_path}")

# Example usage
input_file_path = 'input.json'  # Path to the input JSON file
output_file_path = 'compressed_output.txt'  # Path to save the compressed output
main(input_file_path, output_file_path)
