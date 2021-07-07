#!/usr/bin/env python
# coding: utf-8

from os import walk
import pymeshlab
import re

def pre_process_mesh_using_meshlab(path, file):
    ms = pymeshlab.MeshSet()
    mesh_file = path + "/" + file
    ms.load_new_mesh(mesh_file)
    ms.simplification_quadric_edge_collapse_decimation(targetfacenum=19200,
                                                        preserveboundary=True,
                                                        preservenormal=True,
                                                        preservetopology=True)
    ms.repair_non_manifold_edges_by_removing_faces()
    ms.remove_zero_area_faces()
    ms.remove_unreferenced_vertices()
    ms.remove_isolated_pieces_wrt_face_num(mincomponentsize = 25)
    print(file)
    new_file_name = re.sub("\.obj", "", file)
    new_file_name += "_proc.obj"
    new_file_path = path + "/final_set/proc/" + new_file_name
    ms.save_current_mesh(new_file_path)
    print("Saving file:", new_file_path)

# path = "E:/Uni_Projects/3DMeshes/2020_ProjectMeshPreparation/mesh_cutting/input"
path = r"E:\Uni_Projects\3DMeshes\2020_ProjectMeshPreparation"
_, _, filenames = next(walk(path))

print(filenames)

final_set = [
'64126155.obj',
'Hannover_ZL_initialSegmentation.obj',
'15912596.obj',
'Hannover_SE_Segm1_initial.obj',
'Hannover_DK_initialSegmentation.obj',
'Hannover_GDPT_right_3.obj',
'Hannover_GDPT_right_initial_2.obj',
'Hannover_NRLP_initial_cut.obj',
'Kiel_BB_Pat8_initial_cut.obj',
'Hannover_PP_left_initial.obj',
'Hannover_PP_left_initialb.obj',
'SN_20180830_2_initial_cut.obj',
'Hannover_MRPS_neu_2.obj',
'Hannover_MRPS_neu_1.obj',
'SN_20180830_left_cut1.obj',
'Hannover_AM_left_initial.obj',
'Kiel_BB_Pat_10_initial_cut2.obj',
'Kiel_BB_Pat_10_initial_cut.obj',
'Hannover_AB_right_initial.obj',
'Hannover_AB_right_initialb.obj'
]

for file in filenames:
   if "obj" in file and file in final_set:
       pre_process_mesh_using_meshlab(path, file)
