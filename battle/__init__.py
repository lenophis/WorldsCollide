import battle.formation_flags
from battle.multipliers import Multipliers
import battle.load_enemy_level
import battle.no_exp_party_divide
import battle.suplex_train_check
import battle.auto_status
import battle.end_checks

__all__ = ["Battle"]
class Battle:
    def __init__(self):
        self.multipliers = Multipliers()
