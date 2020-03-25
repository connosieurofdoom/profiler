# profiler
## Repository with code for profiling other functions.

#### Installation command:
pip install -i https://test.pypi.org/simple/ profiler-connosieurofdoom 


Prints the CPU and memory usage.
Logs the output to a log and a csv file too.

~~~python
#Code Sample for python
from bsort import bsort
from profiler import profile

t = [0,10,3,41,2]
profile(bsort,t)


~~~
Sample output:

DateTime:2020-03-25 11:08:50.311120 \
Function Name:bsort \
Input:[0, 2, 3, 10, 41] \
Output:[0, 2, 3, 10, 41] \
create_time:2020-03-25 11:08:49 \
Execution Time:2.3699999999959864e-05 \
Number of active threads:5 \
Machine:AMD64 \
Platform Version:10.0.18362 \
System:Windows \
Processor:Intel64 Family 6 Model 158 Stepping 9, GenuineIntel \
RAM:8 GB \
Process Priority:32 \
Memory Usage:0.031497955322265625 \
Cores:4 \
Cpu Usage:100.0 \
Virtual Memory:svmem(total=8459030528, available=3618177024, percent=57.2, used=4840853504, free=3618177024) \
memory_usage:0 \
read_bytes:4313098 \
write_bytes:2874 \
no. of threads:9 \
username:LEGION\Shreyas \
LOG path: e:\Git\CodeLibrary\Shreyas\Python\log\ \
CSV path: e:\Git\CodeLibrary\Shreyas\Python\csv\ 