import gym
import numpy as np
import cv2
from new_env.sawyer_hammer import SawyerHammerEnv
# from metaworld.benchmarks import ML1

# env = gym.make("Hopper-v3")
env = SawyerHammerEnv()
observation = env.reset()

# print(observation)
actions = np.array([[0,0,-0.2,0],[0,0,-0.2,0.2], [0,0,0.2,0.2],[0.2,0,0.2,0.2]])
print(env.get_endeff_pos())

print(env.get_site_pos('rightEndEffector'))
print(env.get_site_pos('leftEndEffector'))
print(env.init_fingerCOM)
print(env.sim.data.ctrl)

for i in range(200):
  # env.render()
  image = env.render()
  if(i < 10):
      img_idx = "00"+str(i)
  if(i>100):
      img_idx = str(i)
  else:
      img_idx = '0'+str(i)

  image_name = img_idx+'.png'
  cv2.imwrite(image_name, image[:,:,::-1])
  # action = env.action_space.sample()

  action = actions[i // 50]

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