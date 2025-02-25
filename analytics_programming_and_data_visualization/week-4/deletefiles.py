import os

def delete_all_sample_files():
    for file in os.listdir():
        if file.startswith("sample") and os.path.isfile(file):
            os.remove(file)
            print(f"Deleted: {file}")


delete_all_sample_files()