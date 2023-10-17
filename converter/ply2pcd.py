import os
import pdal 
import json

input_path="/Volumes/LHH-WD-1TB/data/Novafos-3D/Muffe3D/Area_1/pointclouds/"
output_path="/Volumes/LHH-WD-1TB/data/Novafos-3D/Muffe3D/Area_1/pcd_files_binary/"

# make sure output directory exists
if not os.path.exists(output_path):
    os.makedirs(output_path)

# list ply files in input the input directory
pc_files = [f for f in os.listdir(input_path) if f.endswith('.ply')and not f.startswith('.')] # added startswith condition to aviod inclussion of ._files


### PDAL Pipelines ###

# "filename":os.path.join(output_path,filename.replace('ply','las')) 
def pdal_pipeline_ply2pcd(filename):
    pipeline_dict = [
        {
            "type":"readers.ply",
            "filename":input_path+filename,
        },
        {
            "type":"writers.pcd",
            "compression":"binary",
            "filename":os.path.join(output_path,filename.replace('ply','pcd'))
        }
    ]
    return pipeline_dict


### Loop PLY files and execute PDAL Pipeline ###

for pc_file in pc_files:
    print(f"{pc_file} is processing ...")
    pipeline_json = json.dumps(pdal_pipeline_ply2pcd(pc_file))
    pipeline = pdal.Pipeline(pipeline_json)
    count = pipeline.execute()
    arrays = pipeline.arrays
    metadata = pipeline.metadata
    log = pipeline.log



