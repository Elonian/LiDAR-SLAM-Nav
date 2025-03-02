import os
import scipy.io as sio
import numpy as np
import open3d as o3d


def read_canonical_model(model_name):
  '''
  Read canonical model from .mat file
  model_name: str, 'drill' or 'liq_container'
  return: numpy array, (N, 3)
  '''
  model_fname = os.path.join('./code/icp_warm_up/data', model_name, 'model.mat')
  print(model_fname)
  model = sio.loadmat(model_fname)

  cano_pc = model['Mdata'].T / 1000.0 # convert to meter

  return cano_pc


def load_pc(model_name, id):
  '''
  Load point cloud from .npy file
  model_name: str, 'drill' or 'liq_container'
  id: int, point cloud id
  return: numpy array, (N, 3)
  '''
  pc_fname = os.path.join('./code/icp_warm_up/data', model_name, '%d.npy' % id)
  pc = np.load(pc_fname)

  return pc


def visualize_icp_result(source_pc, target_pc, pose):
  '''
  Visualize the result of ICP
  source_pc: numpy array, (N, 3)
  target_pc: numpy array, (N, 3)
  pose: SE(4) numpy array, (4, 4)
  '''
  source_pcd = o3d.geometry.PointCloud()
  source_pcd.points = o3d.utility.Vector3dVector(source_pc.reshape(-1, 3))
  source_pcd.paint_uniform_color([0, 0, 1])

  target_pcd = o3d.geometry.PointCloud()
  target_pcd.points = o3d.utility.Vector3dVector(target_pc.reshape(-1, 3))
  target_pcd.paint_uniform_color([1, 0, 0])

  source_pcd.transform(pose)

  o3d.visualization.draw_geometries([source_pcd, target_pcd])

def save_combined_icp_result(source_pc, target_pc, pose, output_filename="combined_icp_result.ply"):
  '''
  Save the combined source and target point clouds into a single .ply file.
  
  Parameters:
  - source_pc: numpy array, (N, 3) -> Source point cloud
  - target_pc: numpy array, (N, 3) -> Target point cloud
  - pose: SE(4) numpy array, (4, 4) -> Transformation matrix for source point cloud
  - output_filename: str, default "combined_icp_result.ply" -> Output .ply filename
  '''

  source_pcd = o3d.geometry.PointCloud()
  source_pcd.points = o3d.utility.Vector3dVector(source_pc.reshape(-1, 3))
  source_pcd.paint_uniform_color([0, 0, 1]) 

  target_pcd = o3d.geometry.PointCloud()
  target_pcd.points = o3d.utility.Vector3dVector(target_pc.reshape(-1, 3))
  target_pcd.paint_uniform_color([1, 0, 0]) 

  source_pcd.transform(pose)

  combined_points = np.concatenate([np.asarray(source_pcd.points), np.asarray(target_pcd.points)], axis=0)
  combined_colors = np.concatenate([np.asarray(source_pcd.colors), np.asarray(target_pcd.colors)], axis=0)
  combined_pcd = o3d.geometry.PointCloud()
  combined_pcd.points = o3d.utility.Vector3dVector(combined_points)
  combined_pcd.colors = o3d.utility.Vector3dVector(combined_colors)
  o3d.io.write_point_cloud(output_filename, combined_pcd)
  print(f"Combined ICP result saved as {output_filename}")


def visualise_combined_icp_result(file_path: str):
  pcd = o3d.io.read_point_cloud(file_path)

  # Visualize the point cloud
  o3d.visualization.draw_geometries_with_editing([pcd])