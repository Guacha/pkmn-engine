import math

def exp_for_lvl(growth_rate, lvl):
    if growth_rate == 'erratic':
        if lvl == 1: return 0
        elif 1 < lvl < 50:
            return math.floor(lvl**3 * (100-lvl)/50)
        elif 50 <= lvl < 68:
            return math.floor(lvl**3 * (100-lvl)/100)
        elif 68 <= lvl < 98:
            return math.floor(lvl**3 * (1911-10*lvl)//3)//500
        else:
            return math.floor(lvl**3 * (160-lvl)/100)
        
    elif growth_rate == 'fast':
        return math.floor(4*lvl**3/5)
    
    elif growth_rate == 'medium':
        if lvl == 1: return 0
        return lvl**3
    
    elif growth_rate == 'medium-slow':
        if lvl == 1: return 0
        return math.floor(6/5 * lvl**3 - 15*lvl**2 + 100*lvl - 140)
    
    elif growth_rate == 'slow':
        if lvl == 1: return 0
        return 5*lvl**3 // 4
    
    elif growth_rate == 'fluctuating':
        if lvl < 15:
            return lvl**3 * ((lvl+1)//3 + 24)//50
        
        elif 15 <= lvl < 36:
            return lvl**3 * (lvl+14)//50
        
        else:
            return lvl**3 * ((lvl//2) + 32)//50