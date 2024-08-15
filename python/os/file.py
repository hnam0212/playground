import os

fd = os.open("test.txt", os.O_RDWR|os.O_CREAT)

print(fd)

fd2= os.open("test2.txt", os.O_RDWR|os.O_CREAT)

print(fd2)

print(type(fd))

print(fd)

fo = os.fdopen(fd, "w+")
print(type(fo))
fo.write(f"First line {os.linesep}")

fo.close()


fd = os.open("test.txt", os.O_RDWR|os.O_CREAT)

fo = os.fdopen(fd, "a")

fo.write("Second line")

fo.close()

"""
Summary:
- fdopen accespts a file descriptor as parameter value and returns a file object
- file object include method like read, write, readline, seek ,...
- File descriptor is an integer value that identifies the open files from a chunk of open files kept by kernel of the process
- OS will use fd to manage open files and other I/O resource

- 0: stdin
- 1: stdout
- 2 stder
- and so on, 3, 4 , 5 for each file opened in your program

"""