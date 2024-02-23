import subprocess
from difflib import SequenceMatcher

similarity_flag = 0
# Set similarity_flag to flag value
# either by directly changing code, or by calling variable in other files

def comp(mode, in1, in2):
    # Comparing two URLs
    if(mode == 1): 
        a = SequenceMatcher(None, in1, in2).ratio()
        if(a >= similarity_flag): return a

    # Comparing two websites
    elif(mode == 2):
        subprocess.run(["wget -O file1.html", in1])
        subprocess.run(["wget -O file2.html", in2])
        file1 = open("file1.html").read()
        file2 = open("file2.html").read()
        a = SequenceMatcher(None, file1, file2).ratio()
        if(a >= similarity_flag): return a

