# simulator.py
simulator.py is a simple tool to have experiments easily running in parallel.

It execute a given list of commands by keeping a number of process in parallel. For example, the following code will execute 30 different commands by executing at the most 20 in parallel: 
```python
execfile("simulator.py")
commands = ["ping -c 10 %s > /dev/null" % h for h in ["www.google.com", "www.twitter.com", "www.github.com"]] * 10
Simulator.execute(commands, number_of_processes=20, delay_between=1)
```
This tool checks periodically whether a process has finished or not, when a process finishes, another command runs. The parameter `delay_between` is the time in seconds which the main process sleeps until this check is performed again. The value of this parameter depends on the expected time that the commands will take to finish. The longer they take, the higher `delay_between` should be.  