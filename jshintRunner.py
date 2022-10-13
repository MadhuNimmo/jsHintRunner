import os
import re
import sys
import subprocess

def runner(filepath,arr):
        if os.path.isdir(filepath):
                for root, subFolders, files in os.walk(filepath):
                        for file in files:
                                if(file.endswith(".js")):
                                        f = os.path.join(root, file)
                                        runjshint(f,arr)
        elif os.path.isfile(filepath):
                runjshint(filepath,arr)
        print(arr)
def runjshint(f,arr):
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
        return arr
if __name__ == "__main__":
            arr={};
            runner(sys.argv[1],arr)
