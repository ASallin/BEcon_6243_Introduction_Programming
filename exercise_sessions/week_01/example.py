import time
from rich.progress import track

print("Hello world")

"""
# Modules and packages
A module is a single file (which must be a .py file) that contains Python code. A package is a 
collection of modules organized in directories that give a package hierarchy.

In this example, rich is a package - it's a third-party library for creating rich text and beautiful formatting
in terminal applications. The rich package contains multiple modules, one of which is progress. The progress 
module provides functionality for displaying progress bars in the terminal.

time is also considered a package (technically a built-in module), but it's part of Python's standard library.

# Dependencies
Dependencies are external packages or libraries that your code relies on to function correctly. In this example,
the rich package is a dependency because the code uses it to create a progress bar.
"""

for i in track(range(20), description="For example:"):
    time.sleep(0.05)
