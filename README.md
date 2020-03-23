# profiler
## Repository with code for profiling other functions.

pip install -i https://test.pypi.org/simple/ profiler-connosieurofdoom
Prints the CPU and memory usage.

~~~python
#Code Sample for python
from bsort import bsort
from profiler import profiler

t = [0,10,3,41,2]
profiler.profile(bsort,t)

~~~