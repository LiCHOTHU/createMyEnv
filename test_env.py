import gym
import numpy as np
import cv2
from new_env.sawyer_hammer import SawyerHammerEnv
# from metaworld.benchmarks import ML1
from mujoco_py import load_model_from_path, MjSim
from mujoco_py import GlfwContext
GlfwContext(offscreen=True)


env = SawyerHammerEnv()
# observation = env.reset()

'''
pose_fn = "./new_env/util/assets/sample_hammer/L/0/L_21838163_hammer.xml"
img_fn = "./sample.png"
model = load_model_from_path(pose_fn)
sim = MjSim(model)


image, depth = sim.render(420, 380, camera_name="dataset", depth=True)
image_flip = cv2.flip(image, 0)
cv2.imwrite(img_fn, image_flip)
'''
for i in range(3000):
  env.render()
  action = env.action_space.sample()

  # action = actions[i // 50]

  print("------this step {0}------".format(i))
  # print("observation info")
  # print(observation)

  print("action info")
  print(action)
  print("right end effector")
  print(env.get_site_pos('rightEndEffector'))
  print("left end effector")
  print(env.get_site_pos('leftEndEffector'))

  observation, reward, done, info = env.step(action)


  if done:
    observation = env.reset()
env.close()