from os import walk
import re
import os
import shutil
import math

edges_path = "E:/Uni_Projects/3DMeshes/2020_ProjectMeshPreparation/small_meshes/proc"
_, _, filenames = next(walk(edges_path))

for name in filenames:
    if not '.edges' in name:
        continue
    
    wo_ext = re.sub("\.edges", "", name)
    print(wo_ext)
    
    file = open(name, 'r')
    lines = file.readlines()
    print(len(lines))
    file.close()
    
    eseg_file = wo_ext + ".eseg"
    print(eseg_file)
    
    mid = math.floor(len(lines)/2)
    
    new_file = open(eseg_file, 'w+')
    for i in range(0, mid, 1):
        new_file.write("0\n")
    for i in range(mid, len(lines), 1):
        new_file.write("1\n")
    new_file.close()
