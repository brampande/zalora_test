## Prerequisite:
- Docker already Installed
- make command already installed

## Note:
 - Run: make run to execute the program
 - You can see the output after a container execute the program. You can check using command make checklog
  
## Architecture:

This task actually does not have a lot of processing, but it is very memory consuming because the data processed is quite large and the transformation is quite complex. Here I use docker as a medium to manage the amount of memory and perform processing in the container. The reasons are that:
1. Easier to use and support on all OS and we can configure the memory we use.
2. I use pandas for data processing, because I personally think pandas has enough functions that can provide data transformation