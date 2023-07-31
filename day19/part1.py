      
#INPUT = "input.txt"
INPUT = "input_example.txt"

MINUTES = 24

solution=0
    
ORE = 1
CLAY = 2
OBSIDIAN = 3
GEODE = 4

    
class Blueprint:
    def __init__(self, OreOreRobot=0, OreClayRobot=0,OreObsidianRobot=0,ClayObisidianrobot=0,OreGeodeRobot=0,ObisidanGeodeRobot=0):
        self.ore_ore_robot = OreOreRobot
        self.ore_clay_robot = OreClayRobot
        self.ore_obsidian_robot = OreObsidianRobot
        self.clay_obsidian_robot = ClayObisidianrobot
        self.ore_geode_robot = OreGeodeRobot
        self.obsidian_geode_robot = ObisidanGeodeRobot
    
class State:
    def __init__(self):
        self.ore=0
        self.obsidian=0
        self.clay=0
        self.geode=0
        self.robots=[ORE]
    
    def copy(self):
        s=State()
        s.ore = self.ore
        s.obsidian = self.obsidian
        s.clay = self.clay
        s.robots = self.robots.copy()
        return s
        
with open(INPUT) as f:
    lines = [f.strip().replace("\n","") for f in f.readlines()]

blueprints = []

def getWordAsInt(str,index):
    return int(str.strip().split(" ")[index])

def performMove(remainingMinutes,blueprint:Blueprint, state:State):
    
    if(remainingMinutes==0):
        return state.geode
        
    state = state.copy()
    possibleMoves = []
    
    for robot in state.robots:
        if robot==ORE:
            state.ore = state.ore+1
        elif robot==CLAY:
            state.clay = state.clay+1
        elif robot==OBSIDIAN:
            state.obsidian = state.obsidian+1
        else:
            state.geode = state.geode+1
    
    if(state.ore >= blueprint.ore_ore_robot):
        new_state = state.copy()
        new_state.ore = new_state.ore-blueprint.ore_ore_robot
        new_state.robots.append(ORE)
        possibleMoves.append(performMove(remainingMinutes-1,blueprint,new_state))
    
    if(state.ore >= blueprint.ore_clay_robot):
        new_state = state.copy()
        new_state.ore = new_state.ore-blueprint.ore_clay_robot
        new_state.robots.append(CLAY)
        possibleMoves.append(performMove(remainingMinutes-1,blueprint,new_state))
        
    if(state.ore >= blueprint.ore_obsidian_robot and state.clay >= blueprint.clay_obsidian_robot):
        new_state = state.copy()
        new_state.ore = new_state.ore-blueprint.ore_obsidian_robot
        new_state.clay = new_state.ore-blueprint.clay_obsidian_robot
        new_state.robots.append(OBSIDIAN)
        possibleMoves.append(performMove(remainingMinutes-1,blueprint,new_state))
        
    if(state.ore >= blueprint.ore_geode_robot and state.obsidian >= blueprint.obsidian_geode_robot):
        new_state = state.copy()
        new_state.ore = new_state.ore-blueprint.ore_geode_robot
        new_state.clay = new_state.ore-blueprint.obsidian_geode_robot
        new_state.robots.append(GEODE)
        possibleMoves.append(performMove(remainingMinutes-1,blueprint,new_state))
    
    #Do nothing
    possibleMoves.append(performMove(remainingMinutes-1,blueprint,state))
    
    return max(possibleMoves)
    

for line in lines:  
    blueprint = Blueprint()
    s = line.split(":")
    
    id = getWordAsInt(s[0],1)
    s = s[1].split(".")
    
    blueprint.ore_ore_robot = getWordAsInt(s[0],4)
    blueprint.ore_clay_robot = getWordAsInt(s[1],4)
    blueprint.ore_obsidian_robot = getWordAsInt(s[2],4)
    blueprint.clay_obsidian_robot = getWordAsInt(s[2],7)
    blueprint.ore_geode_robot=getWordAsInt(s[3],4)
    blueprint.obsidian_geode_robot=getWordAsInt(s[3],7)
    
    initialState = State()
    
    solution = solution + performMove(MINUTES, blueprint, initialState)


print("Solution: " + str(solution))
    