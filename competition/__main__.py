# IMPORTS:

from prisoner.dilemma import *
from prisoner.bots import *
from prisoner.__main__ import main

# SETUP:

all_bots = {}

# DEFAULT BOTS:

@pd_bot
def cooperate_bot(self_hist, opp_hist, opp_bot):
    return True
all_bots["cooperate_bot"] = cooperate_bot

@pd_bot
def defect_bot(self_hist, opp_hist, opp_bot):
    return False
all_bots["defect_bot"] = defect_bot

@pd_bot
def coin_flip_bot(self_hist, opp_hist, opp_bot):
    return random.getrandbits(1)
all_bots["coin_flip_bot"] = coin_flip_bot

@pd_bot
def tit_for_tat_bot(self_hist, opp_hist, opp_bot):
    if opp_hist:
        return opp_hist[-1]
    else:
        return True
all_bots["tit_for_tat_bot"] = tit_for_tat_bot

@pd_bot
def mirror_bot(self_hist, opp_hist, opp_bot):
    return opp_bot(opp_hist, self_hist, mirror_bot)
mirror_bot += cooperate_bot
all_bots["mirror_bot"] = mirror_bot

# COMPETITION BOTS:

# MAIN:

if __name__ == "__main__":
    main(all_bots)
