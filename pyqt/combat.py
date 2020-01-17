from .utils import dice_roller


class CombatOutput(object):
    """ Object contaning calculations for damage dealing
        TODO:
            Check for better solution?
    """

    def __init__(self):
        self.char = None
        self._weapon = None
        self._stat = None
        self.att_roll = None
        self.att_const = None
        self.damage = None
        #
        # self.__dict__ = {'weapon': self.weapon,
        #                  'stat': self.stat,
        #                  'attack': self.att_roll,
        #                  'const': self.att_const,
        #                  'dmg': self.damage
        #                  }

    def attack_roll(self):
        """ Check 1d20 roll and set attack constant as follows:

               d20 -> nat 20 -> att_const = 2
               d20 -> nat 1 -> att_const = 0
               d20 -> (1, 20) -> att_const = 1
               attack roll = d20 + stat['mod'] + prof
            ``
        """

        d20 = dice_roller('1d20', mem_out=False)[0]
        self.att_roll = d20
        if d20 == '1':
            mem_output(f"Critical failure...")
            return None
            # self.att_const = 0
        elif d20 == '20':
            mem_output(f"Critical hit!")
            self.att_const = 2
        else:
            self.att_roll = d20 + self.char.stats[self.stat]['mod'] + self.char.prof['score']
            mem_output(f"Attack = {self.att_roll}")
            self.att_const = 1

    def damage_roll(self):
        """ calculate damage roll
            take att_const from previous calculation.

            damage = (sum(weapon_damage_rolls) + stat_mod)) * att_const
        """
        tmprolls = dice_roller(self.char.weapons[self.weapon]['dmg'], mem_out=False)
        mem_output(f"{tmprolls} + {self.char.stats[self.stat]['mod']} * {self.att_const}")
        self.damage = (sum(tmprolls) + self.char.stats[self.stat]['mod']) * self.att_const
        mem_output(f"{self.damage}")

    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, choice):

        if choice:
            if choice not in self.char.weapons:
                raise KeyError('Unavailable _weapon')
            self._weapon = choice

    @property
    def stat(self):
        return self._stat

    @stat.setter
    def stat(self, choice):
        if choice:
            if choice not in ('str', 'dex'):
                raise KeyError('Only str or dex')
            self._stat = choice
