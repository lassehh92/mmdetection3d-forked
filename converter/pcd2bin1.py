import numpy as np
from pypcd import pypcd

#pcd_data = pypcd.PointCloud.from_path('/Volumes/LHH-WD-1TB/data/Novafos-3D/Muffe3D/Area_1/pcd_files_test/Area_1_Site_1.pcd')
pcd_data = pypcd.PointCloud.from_path('/Volumes/LHH-WD-1TB/data/Novafos-3D/Muffe3D/Area_1_Site_1.pcd')
#pcd_data = pypcd.PointCloud.from_path('/Users/lhh/github-projects/mmdetection3d-forked/converter/data.pcd')

points = np.zeros([pcd_data.width, 3], dtype=np.float32)
points[:, 0] = pcd_data.pc_data['x'].copy()
points[:, 1] = pcd_data.pc_data['y'].copy()
points[:, 2] = pcd_data.pc_data['z'].copy()
with open('/Volumes/LHH-WD-1TB/data/Novafos-3D/Muffe3D/Area_1/bin_files/Area_1_Site_1.bin', 'wb') as f:
    f.write(points.tobytes())