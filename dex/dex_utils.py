import math

def exp_for_lvl(growth_rate, lvl):
    if growth_rate.name == 'erratic':
        if lvl < 50:
            return lvl**3 * (100-lvl)/50
        elif 50 <= lvl < 68:
            return lvl**3 * (100-lvl)/100
        elif 68 <= lvl < 98:
            return lvl**3 * (1911-10*lvl)//3
        else:
            return lvl**3 * (160-lvl)/100
        
    elif growth_rate.name == 'fast':
        return 4*lvl**3/5
    
    elif growth_rate.name == 'medium-fast':
        return lvl**3
    
    elif growth_rate.name == 'medium-slow':
        return 6/5 * lvl**3 - 15*lvl**2 + 100*lvl - 140
    
    elif growth_rate.name == 'slow':
        return 5*lvl**3 / 4
    
    elif growth_rate.name == 'fluctuating':
        if lvl < 15:
            return lvl**3 * ((lvl+1)//3 + 24)/50
        
        elif 15 <= lvl < 36:
            return lvl**3 * (lvl+14)/50
        
        else:
            return lvl**3 * ((lvl//2) + 32)/50