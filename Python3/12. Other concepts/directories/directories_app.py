from pathlib import Path

# Absolute Path
# Relative Path

path = Path("\directories")

# print(path.mkdir()) # make directory

# print(path.rmdir()) # remove directory

for file in path.glob("*.py"):
    print(file)