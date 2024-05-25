import os
import re
import sys
import hashlib

def file_hash(file_path):
    """Generate hash of a file."""
    with open(file_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def remove_duplicates(paths):
    """Remove duplicate files."""
    file_hashes = {}
    for path in paths:
        for root, _, files in os.walk(path):
            for file in files:
                file_name = os.path.join(root, file)
                file_base_name, file_extension = os.path.splitext(file_name)
                match = re.search(r'\(\d+\)$', file_base_name)  # Match "(x)" pattern
                if match:
                    # If file name contains (x), skip it
                    continue
                # Calculate hash of file content
                hash_value = file_hash(file_name)
                # If hash already exists, remove the file
                if hash_value in file_hashes:
                    print(f"Removing duplicate: {file_name}")
                    os.remove(file_name)
                else:
                    file_hashes[hash_value] = file_name

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py directory1 directory2 ...")
        sys.exit(1)
    
    directories = sys.argv[1:]
    remove_duplicates(directories)
