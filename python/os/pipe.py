"""
Reference: https://www.tutorialspoint.com/python/os_pipe.htm
os.pipe() method of OS moduile creates a pipe for inter-process communication, allow set of data to be passed from one process to another
This process is possible because it returns a pair of fiole descriptors namely "r" and "w" usable for reading an writing respectively
"""

import os
import sys

print("Child process wil write text to a pipe and the parent will read the text that are written by child")

# os.pipe do not take any argument
# Method retuen a pair of file descriptor
r, w = os.pipe()

process_id = os.fork()

if process_id:
    #This is the parent process
    os.close(w)
    r = os.fdopen(r)
    print("Parent reading")
    string = r.read()
    print(string)
    sys.exit(0)

else:
    os.close(r)
    w = os.fdopen(w, "w")
    w.write("Text from child")
    w.close()

    sys.exit(0)

"""
os.fork() function inpython is sued to create a child process by duplicating the current process. This functrion is only available for unix-like os
"""