import os
import multiprocessing
import platform

#To Access Environment Variables
print(os.environ)
print(os.environ['HOME'])
print(os.environ["PATH"])

#To find Numbers of CPU
print(multiprocessing.cpu_count())

#FInd OS Platform and Release Info
print(os.name)
print(platform.system())
print(platform.release())