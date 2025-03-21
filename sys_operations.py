import os
import sys
import platform
import socket

# Lab 9 - Question 3.a.a, 3.a.b
#Machine type and processor type
print(platform.machine())
print(platform.architecture())

# Lab 9 - Question 3.a.c, 3.a.d
# Set and Get socket timeout
print(socket.getdefaulttimeout())
socket.setdefaulttimeout(50)
print(socket.getdefaulttimeout())

# Lab 9 - Question 3.a.e
# OS name
print(os.name)
print(platform.system())

# Lab 9 - Question 3.a.f
# Process ID
print(os.getpid())

# Lab 9 Question 3.b.a
# File descriptors
# Open (or create) a file called fdpractice
f_name = "fdpractice.txt"
#with open("fdpractice.txt", "a+") as f:
#    f.read()
#    f.write("hello, world")

#f1 = open(f_name, "r")
#print(f1)
#f1.close()

f = (os.open(f_name, os.O_RDWR | os.O_CREAT))
print(type(f))

f_obj = os.fdopen(f, "a+")
print(f_obj)
f_obj.close()

print()

# Lab 9 - Question 3.b.e.
# Forking
print("Before fork: ", os.getpid())
p = os.fork()
print("After fork: ", os.getpid())


if p == 0:
    print("Child process")
    print("Parent Process PID: ", os.getppid())
else:
    print("Parent process")
    os.wait()
    print("Child process PID: ", p)

print("Last line")