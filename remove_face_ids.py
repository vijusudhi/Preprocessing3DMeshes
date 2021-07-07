import re

file = open("E:/Uni_Projects/3DMeshes/MeshCNN-master/MeshCNN-master/datasets/human_seg/train/BM_20170828_seg.obj", "r")
lines = file.readlines()
print(lines[:10])

file_rem = open("E:/Uni_Projects/3DMeshes/MeshCNN-master/MeshCNN-master/datasets/human_seg/train/BM_20170828_seg_rem.obj", "w")
for line in lines:
    if re.match('^f', line):
        line_rem = line.split(" ")[:4]
        line_rem = " ".join(line_rem)
        file_rem.write(line_rem + "\n")
    else: 
        file_rem.write(line)
        
file_rem.close()