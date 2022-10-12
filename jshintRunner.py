import os
import re
import sys
import subprocess

arr={};

def runner(filedir):
        for filename in os.listdir(filedir):
                f = os.path.join(filedir, filename)
                if os.path.isfile(f):
                        bashCommand = "jshint "+f
                        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
                        output, error = process.communicate()
                        outarr = output.decode("utf-8").split('\n')
                        for item in outarr:
                                if "ES6" in item:
                                        keyname = item.split(", ")[-1]
                                        if keyname in arr.keys():
                                                arr[keyname]+=1
                                        else:
                                                arr[keyname]=1
        print(arr)

if __name__ == "__main__":
            runner(sys.argv[1])
# python3 jshintRunner.py <<directory name>>
