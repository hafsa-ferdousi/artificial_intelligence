
import heapq
import math
from queue import Queue

def manhattan(x1,y1,x2,y2):
    return abs(x1 - x2) + abs(y1 - y2)

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
class GridWorldEnv:
    def __init__(self, size, goal, agent_pos):
        self.size = size
        self.goal = goal
        self.agent_pos = agent_pos
        self.visited = []

    def get_state(self):
        return self.agent_pos

    def is_goal_reached(self):
        return self.agent_pos == self.goal

    def updateAgentPos(self, agentPos):
        self.agent_pos = agentPos

class Agent:
    def __init__(self,env):
        self.env=env

    def perceive(self,current_state,qu):
        x=current_state[0]
        y=current_state[1]
        data=[]
        if(y-1>=0 and [x,y-1] not in self.env.visited and  [x,y-1] not in [item[1] for item in pq]):
            data.append([x,y-1])
        if (y + 1 < self.env.size and [x, y + 1] not in self.env.visited and [x,y+1] not in [item[1] for item in pq]):
            data.append([x, y + 1])
        if (x + 1 < self.env.size and [x+1, y ] not in self.env.visited and [x+1,y] not in [item[1] for item in pq]):
            data.append([x+1, y ])
        if (x - 1 >= 0 and [x-1, y ] not in self.env.visited and [x-1,y] not in [item[1] for item in pq]):
            data.append([x-1, y ])
        return data



    def act(self, state):
        self.env.updateAgentPos(state)

env=GridWorldEnv(4,[0,3],[3,0])
agent=Agent(env)
pq = []
g=manhattan(3,0,agent.env.agent_pos[0], agent.env.agent_pos[1])
h=euclidean_distance(agent.env.agent_pos[0], agent.env.agent_pos[1], agent.env.goal[0], agent.env.goal[1])
heapq.heappush(pq, (h+g, agent.env.get_state()))


while pq:
    priority, node = heapq.heappop(pq)
    print(node, "With Priority", priority)
    agent.env.updateAgentPos(node)

    agent.env.visited.append(node)

    if(agent.env.is_goal_reached()):
        print('Goal')
        break

    percept = agent.perceive(node, pq)

    for p in percept:
        g=manhattan(3,0,p[0],p[1])
        h=euclidean_distance(p[0], p[1], agent.env.goal[0], agent.env.goal[1])
        print(h+g)
        heapq.heappush(pq, (h + g, p))


