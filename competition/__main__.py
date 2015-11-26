# IMPORTS:

from prisoner.__main__ import main
from prisoner.bots import cooperate_bot, defect_bot, tit_for_tat_bot, mirror_bot

# SETUP:

all_bots = {
    "cooperate": cooperate_bot,
    "defect": defect_bot,
    "tit_for_tat": tit_for_tat_bot,
    "mirror": mirror_bot
}

# COMPETITION BOTS:

# MAIN:

if __name__ == "__main__":
    main(all_bots)
