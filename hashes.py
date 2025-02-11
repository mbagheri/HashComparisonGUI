import hashlib

# Error Handling for missing filepath and missing hash algorithm
class Hashes:
    def get_file_hash(self, file_path, hash_algorithm, buffer_size=65536):
        hash_object = hashlib.new(hash_algorithm)

        if file_path is not None:
            with open(file_path, 'rb') as file:
                while chunk := file.read(buffer_size):
                    hash_object.update(chunk)
        else:
            return

        return hash_object.hexdigest()
