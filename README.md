# profiler
## Repository with code for profiling other functions.

#### Installation command:
pip install -i https://test.pypi.org/simple/ profiler-connosieurofdoom 


Prints the CPU and memory usage.

~~~python
#Code Sample for python
from bsort import bsort
from profiler import profiler

t = [0,10,3,41,2]
profiler.profile(bsort,t)

~~~
Sample output:

Input: [0, 10, 3, 41, 2] \
Output: [0, 2, 3, 10, 41] \
Execution Time: 0.000921100000000008 \
MemoryUsage: 0.0318603515625 \
cpuUsage: 50.0 \
VirtualMemory: svmem(total=8459030528, available=1430855680, percent=83.1, used=7028174848, free=1430855680) \