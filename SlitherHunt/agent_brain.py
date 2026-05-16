from a_star_Pathfinding import astar
from settings import GRID_HEIGHT, GRID_WIDTH


class AgentBrain:
    def __init__(self):
        #stores current computed path from enemy to target
        self.path = []
        #track last positions to avoid recalculations
        self.last_target_pos = None
        self.last_enemy_pos = None 



    def get_action(self, enemy_pos, target_pos, obstacles):
        #convert positions to tuples
        enemy_t = tuple(enemy_pos)
        target_t = tuple(target_pos)

#recompute path if
#-no existing path
#-enemy position changed
#-target position changed
        if (
            not self.path or
            self.last_enemy_pos != enemy_t or
            self.last_target_pos != target_t):
            
            self.path = astar (
                start=enemy_pos,
                goal=target_pos,
                obstacles= obstacles,
                grid_height=GRID_HEIGHT,
                grid_width= GRID_WIDTH
            )
            self.last_enemy_pos = enemy_t
            self.last_target_pos = target_t#####################
        
        if not self.path:
            return None
        
        next_pos = self.path[0]

        if list (next_pos) in obstacles:
            self.path = []
            return None
        
        next_pos = self.path.pop(0)##############

        nx, ny = next_pos
        ex, ey = enemy_pos

#convert next grid position into movement direction
        if nx > ex:
            return "RIGHT"
        
        if nx < ex:
            return "LEFT"
        
        if ny > ey:
            return "DOWN"
        
        if ny < ey:
            return "UP"
        
        #no movement needed
        return None
