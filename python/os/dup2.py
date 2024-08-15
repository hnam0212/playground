import os

# Open a file for writing
fd1 = os.open('output.txt', os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)

# Duplicate the file descriptor fd to standard output (fd 1)
os.dup2(fd1, 1)

# Now, all output to standard output will go to 'output.txt'
print("This will be written to the file 'output.txt'.")

# Close the file descriptor
os.close(fd1)

"""
os.dup2 is used to duplicate the file descriptor in this case fd1 to 1 (stdin)
Use case:
- Redirecting standard output or standard error to a file
"""