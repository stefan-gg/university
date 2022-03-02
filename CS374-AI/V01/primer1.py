import gym

env = gym.make('CartPole-v0')


def theta_policy(obs):
    angle = obs[2]
    return 0 if angle < 0 else 1


def omega_policy(obs):
    w = obs[3]
    return 1 if w > 0 else 0


def theta_omega_policy(obs):
    theta, w = obs[2:4]
    if abs(theta) < 0.03:
        return 0 if w < 0 else 1
    else:
        return 0 if theta < 0 else 1


for i_episode in range(1):
    observation = env.reset()
    for t in range(1000):
        env.render()
        # print(observation)
        action = env.action_space.sample()
        action2 = theta_policy(observation)
        observation, reward, done, info = env.step(action)

        if done:
            print("Episode finished after {} timesteps".format(t + 1))
            break

env.close()
