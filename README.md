# profiler
## Repository with code for profiling other functions.

#### Installation command:
pip install -i https://test.pypi.org/simple/ profiler-connosieurofdoom 


Prints the CPU and memory usage.

~~~python
#Code Sample for python
from bsort import bsort
from profiler import profile

t = [0,10,3,41,2]
profile(bsort,t)


~~~
Sample output:

DateTime:2020-03-24 11:51:56.184423
Function Name:selSort
Input:[1, 2, 10, 30]
Output:[1, 2, 10, 30]
Execution Time:1.6200000000021753e-05
Number of active threads:5
Machine:AMD64
Platform Version:10.0.18362
System:Windows
Processor:Intel64 Family 6 Model 158 Stepping 9, GenuineIntel
RAM:8 GB
Memory Usage:0.031524658203125
Cpu Usage:50.0
Virtual Memory:svmem(total=8459030528, available=3324809216, percent=60.7, used=5134221312, free=3324809216)
LOG path: e:\Git\CodeLibrary\Shreyas\Python\log\
CSV path: e:\Git\CodeLibrary\Shreyas\Python\csv\