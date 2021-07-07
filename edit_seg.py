import re
import sys
from os import walk

path = "E:/Uni_Projects/3DMeshes/MeshCNN-master/MeshCNN-master/datasets/final_set/seg"
_, _, filenames = next(walk(path))
print(filenames)

for name in filenames:
    if "eseg" not in name:
        continue
        
    name = path + "/" + name

    file = open(name, "r")
    lines = file.readlines()
    # print(lines[:10])

    file_rem = open(name, "w")
    for line in lines:
        if re.match('\[\]', line):  # matches []
            file_rem.write("%d"%0 + "\n")
        elif re.match('\[\'0\'\]', line):  # matches ['0']
            file_rem.write("%d"%0 + "\n")
        elif re.match('\[\'1\'\]', line):  # matches ['1']
            file_rem.write("%d"%1 + "\n")
        elif re.match('\[\'0\'\,', line):  # matches ['0',
            file_rem.write("%d"%0 + "\n")
        elif re.match('\[\'1\'\,', line):  # matches ['1',
            file_rem.write("%d"%1 + "\n")
    file_rem.close()
    print("Saving file:", name)