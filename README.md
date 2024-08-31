# ParseTopOutput

A python script to parse the Linux top output and create some useful outputs like CSVs, graphs etc.

## Description

Its written in python and currently it supports the following
* Takes the Linux top output capture in a text file as an input.
* Generates a CSV file contain the following files as an output.
  * Timestamp
  * PID
  * %CPU
  * %MEM
  * COMMAND

## Getting Started
* Tested so far only with top output which is of the following format
```
top - 23:21:50 up 3 days,  3:43,  0 users,  load average: 0.52, 0.58, 0.59
Tasks:  15 total,   1 running,  14 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.4 us,  1.1 sy,  0.0 ni, 98.6 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :  32424.4 total,  10581.1 free,  21619.3 used,    224.0 buff/cache
MiB Swap:  98304.0 total,  97248.8 free,   1055.2 used.  10674.5 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
    1 root      20   0   10532    716    652 S   0.0   0.0   0:00.38 init(Ubuntu-22.
    5 root      20   0   11456   1272    620 S   0.0   0.0   0:56.29 init
  389 root      20   0   10560    360    304 S   0.0   0.0   0:00.00 SessionLeader
```

### Dependencies

* Python3

### Installing

Clone the following repository and then you are good to go.
* https://github.com/NagarjunaPitchela/ParseTopOutput

### Executing program

```
python3 ParseTopOutput.py SampleTopOutput.txt
```

## Help

No error handling as of now. 
```
TBD
```

## Authors

* Nagarjuna Reddy Pitchela  
https://github.com/NagarjunaPitchela  
Email: nagarjunareddyp@gmail.com

## Version History

* 0.0
    * Not released yet, but still can be used :-)

## License

WTFPL

## Acknowledgments

I am not a Python programmer, so most of the code is written with the help of internet based tools like
* stackoverflow
* ChatGPT
* Google
* GeeksForGeeks 
* etc
