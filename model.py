"""
Market-Making & Betting-Game Simulator

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - expected_value
def expected_value(values, probabilities):
    # TODO: return the expected value of the discrete distribution (values, probabilities).
    return np.sum(np.array(values)*np.array(probabilities))

# Step 2 - one_reroll_die_value
def one_reroll_die_value(sides):
    # TODO: return {'value': expected winnings under optimal reroll policy, 'reroll_faces': sorted faces to reroll}
    mean = expected_value(range(1,sides+1),1/sides)
    values=[max(faces,mean) for faces in range(1,sides+1)]
    value=expected_value(values,1/sides)

    return {'value': float(value), 'reroll_faces': [k for k in range(1,sides+1) if k<mean]}

# Step 3 - pay_per_reroll_die_game
def pay_per_reroll_die_game(sides, reroll_cost):
    # TODO: return {'threshold': t, 'value': V} for the pay-per-reroll die game under the optimal threshold policy.
    

    def value(N,t):
        if t>=N+1:
            return float('-inf')
        return ((N+t)/2) -reroll_cost*(t-1)/(N-t+1)

    t= max(0,min(int(sides+1-(2*reroll_cost*sides)**0.5),sides))

    val1=value(sides,t)
    val2=value(sides,t+1)

    if val1>=val2:
        return {'threshold': t, 'value': val1}
    else:
        return {'threshold': t+1, 'value': val2}

    pass

# Step 4 - red_black_card_game_value
import numpy as np

def red_black_card_game_value(num_red, num_black):
    # TODO: return {'value': expected payout under optimal stopping, 'stop_now': whether to stop immediately}.
    r,b= num_red,num_black

    V=np.zeros((r+1,b+1))
    for k in range(1,r+1):
        V[k][0]=k

    for i in range(1,r+1):
        for j in range(1,b+1):
            t=i+j
            V[i][j]=max(i*(1+V[i-1][j])/t + j*(-1+V[i][j-1])/t,0)

    return {'value': V[r][b], 'stop_now': max(V[r][b],0)==0}

# Step 5 - make_quotes
def make_quotes(fair_value, spread_width):
    # TODO: return a dict with 'bid' and 'ask' symmetric around fair_value with total width spread_width
    return {'bid': fair_value-spread_width/2, 'ask':fair_value+spread_width/2}

# Step 6 - execute_trade (not yet solved)
# TODO: implement

# Step 7 - mark_to_market_pnl (not yet solved)
# TODO: implement

# Step 8 - adverse_selection_loss (not yet solved)
# TODO: implement

# Step 9 - uncertainty_spread (not yet solved)
# TODO: implement

# Step 10 - inventory_skewed_quotes (not yet solved)
# TODO: implement

# Step 11 - update_fair_value_from_trade (not yet solved)
# TODO: implement

# Step 12 - update_remaining_card_value (not yet solved)
# TODO: implement

# Step 13 - run_market_making_episode (not yet solved)
# TODO: implement

# Step 14 - summarize_episode_pnls (not yet solved)
# TODO: implement

