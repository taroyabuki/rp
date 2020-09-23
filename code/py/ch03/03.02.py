%pwd
# あるいは
import os
os.getcwd()
#> '/home/jovyan/work'

%cd fromzero
# あるいは
os.chdir('fromzero')

os.getcwd()
#> '/home/jovyan/work/fromzero'

