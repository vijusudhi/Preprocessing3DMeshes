import re
import os

top = r'E:\Uni_Projects\3DMeshes\MeshCNN-master\MeshCNN-master\datasets\final_set_50meshes\train'
for _, _, f in os.walk(top):
    filenames = f
    break
# print(filenames)

meshes = [m.strip() for m in filenames]
meshes = [re.sub('_proc', '', m) for m in meshes]
# meshes = [re.sub('vertices', 'obj', m) for m in meshes]
# print(meshes)


file = open('meshes_ref.txt', 'r')
meshes_ref = file.readlines()
file.close()

# meshes_ref = [m.strip() for m in meshes_ref]
# print(meshes_ref)

meshes_ref = '''
64126155.obj
Hannover_ZL_initialSegmentation.obj
15912596.obj
Hannover_SE_Segm1_initial.obj
Hannover_DK_initialSegmentation.obj
Hannover_GDPT_right_3.obj
Hannover_GDPT_right_initial_2.obj
Hannover_NRLP_initial_cut.obj
Kiel_BB_Pat8_initial_cut.obj
Hannover_PP_left_initial.obj
Hannover_PP_left_initialb.obj
Kiel_BB_Pat2_initial.cut.obj
Hannover_MRPS_neu_2.obj
Hannover_MRPS_neu_1.obj
SN_20180830_left_cut1.obj
Hannover_AM_left_initial.obj
Kiel_BB_Pat_10_initial_cut2.obj
Kiel_BB_Pat_10_initial_cut.obj
Hannover_AB_right_initial.obj
Hannover_AB_right_initialb.obj
Hannover_LR_right2b.obj
Hannover_WK_rightFromBoth_initial_onlyRight.obj
Hannover_WK_rightFromBoth_initial_onlyRightb.obj
Hannover_LR_leftb.obj
Hannover_LR_left_initial.obj
HRA_20180325_2_initial.obj
Kiel_BB_Pat13_initial.obj
Hannover_LR_right_initial.obj
Hannover_WLAD_initial.obj
Hannover_UD_left_initial.obj
Hannover_PP_post_initialb.obj
Hannover_PP_post_initial.obj
Hannover_ATTE_initial_2.obj
Hannover_ATTE_initial.obj
Hannover_AZ_initial.obj
Hannover_WK_left_initialb.obj
Hannover_WK_left_initial.obj
Kiel_BB_Pat20_seg.obj
Hannover_PP_right_initial_smooth.obj
Hannover_PP_right_initial.obj
Hannover_GDPT_left_initial_2.obj
Kiel_BB_Pat24_initial.obj
Hannover_UD_rechts_initial_smooth.obj
Hannover_UD_rechts_initial.obj
Hannover_NRLP_initial_better.obj
Hannover_LR_right.2obj.obj
Hannover_MJ_links_initial.obj
Hannover_MJ_right_initial.obj
Hannover_AB_post_initial.obj
Hannover_AB_post_initialb.obj
'''

meshes_ref = meshes_ref.split('\n')
meshes_ref.remove('')
meshes_ref.remove('')
# print(meshes_ref)


print('--- NOT FOUND IN THE TRAIN FODLER ---')
for mesh in meshes_ref:
    if mesh not in meshes:
        print(mesh)
        
print('')
print('--- NOT FOUND IN THE FINAL LIST ---')
for mesh in meshes:
    if mesh not in meshes_ref:
        print(mesh)        