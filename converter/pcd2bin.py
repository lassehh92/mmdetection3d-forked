import numpy as np
import os
from pypcd import pypcd

input_directory = '/Volumes/LHH-WD-1TB/data/Novafos-3D/Muffe3D/Area_1/pcd_files_binary/'
output_directory = '/Volumes/LHH-WD-1TB/data/Novafos-3D/Muffe3D/Area_1/bin_files'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# list ply files in input the input directory
pc_files = [f for f in os.listdir(input_directory) if f.endswith('.pcd')and not f.startswith('.')]

# List all .pcd files in the input directory
for filename in pc_files:
    print("{} is processing ...".format(filename))
    if filename.endswith('.pcd'):
        input_filepath = os.path.join(input_directory, filename)
        output_filepath = os.path.join(output_directory, filename.replace('.pcd', '.bin'))

        pcd_data = pypcd.PointCloud.from_path(input_filepath)
        points = np.zeros([pcd_data.width, 6], dtype=np.float32) 
        points[:, 0] = pcd_data.pc_data['x'].copy()
        points[:, 1] = pcd_data.pc_data['y'].copy()
        points[:, 2] = pcd_data.pc_data['z'].copy()
        points[:, 3] = pcd_data.pc_data['red'].copy().astype(np.float32)
        points[:, 4] = pcd_data.pc_data['green'].copy().astype(np.float32)
        points[:, 5] = pcd_data.pc_data['blue'].copy().astype(np.float32)

        with open(output_filepath, 'wb') as f:
            f.write(points.tobytes())


# https://github.com/open-mmlab/mmdetection3d/blob/dev-1.x/docs/en/advanced_guides/customize_dataset.md

# ONLY works with python 2!! 
# conda activate pcd
