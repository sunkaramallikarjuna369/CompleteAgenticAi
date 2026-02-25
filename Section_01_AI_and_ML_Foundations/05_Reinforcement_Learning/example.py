"""
Reinforcement Learning
======================
Section 01

Demonstrates RL: Q-Learning grid world
and Multi-Armed Bandit.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random

print("=" * 60)
print("1. Q-LEARNING GRID WORLD")
print("=" * 60)

class GridWorld:
    def __init__(self, size=4):
        self.size = size
        self.goal = (size-1, size-1)
    def step(self, state, action):
        moves = {0: (-1,0), 1: (1,0), 2: (0,-1), 3: (0,1)}
        dx, dy = moves[action]
        nx = max(0, min(self.size-1, state[0]+dx))
        ny = max(0, min(self.size-1, state[1]+dy))
        new_state = (nx, ny)
        reward = 10 if new_state == self.goal else -0.1
        done = new_state == self.goal
        return new_state, reward, done

random.seed(42)
env = GridWorld(4)
Q = {}
alpha, gamma, epsilon = 0.1, 0.9, 0.2

for ep in range(500):
    state = (0, 0)
    for _ in range(50):
        if random.random() < epsilon:
            action = random.randint(0, 3)
        else:
            q_vals = [Q.get((state, a), 0) for a in range(4)]
            action = q_vals.index(max(q_vals))
        ns, r, done = env.step(state, action)
        old_q = Q.get((state, action), 0)
        next_max = max(Q.get((ns, a), 0) for a in range(4))
        Q[(state, action)] = old_q + alpha * (r + gamma * next_max - old_q)
        state = ns
        if done:
            break

# Show learned policy
actions = ["U", "D", "L", "R"]
print("  Learned Policy:")
for r in range(4):
    row = ""
    for c in range(4):
        if (r,c) == env.goal:
            row += " G "
        else:
            q_vals = [Q.get(((r,c), a), 0) for a in range(4)]
            row += f" {actions[q_vals.index(max(q_vals))]} "
    print(f"    {row}")

print("\n" + "=" * 60)
print("2. MULTI-ARMED BANDIT")
print("=" * 60)

class Bandit:
    def __init__(self, n_arms=4):
        self.probs = [random.random() for _ in range(n_arms)]
        self.counts = [0] * n_arms
        self.values = [0.0] * n_arms

    def pull(self, arm):
        reward = 1.0 if random.random() < self.probs[arm] else 0.0
        self.counts[arm] += 1
        self.values[arm] += (reward - self.values[arm]) / self.counts[arm]
        return reward

bandit = Bandit(4)
total_reward = 0
for _ in range(1000):
    if random.random() < 0.1:
        arm = random.randint(0, 3)
    else:
        arm = bandit.values.index(max(bandit.values))
    total_reward += bandit.pull(arm)

print(f"  True probs:     {[f'{p:.2f}' for p in bandit.probs]}")
print(f"  Learned values: {[f'{v:.2f}' for v in bandit.values]}")
print(f"  Total reward:   {total_reward:.0f}/1000")

print("\nDone!")
