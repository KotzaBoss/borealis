# Effects

All possible different feature effects are close to one thousand so I will try to find the commonalities.
## General
### Ability Score Increase
Ability Score Increase give characters an increase to an ability score. This increase cannot exceed 20 unless stated.
> [Ability, Amount]

### Ability Score Max Increase
Ability Score Increase give characters an increase to the maximum of the ability score.
> [Ability, Amount]

### Speed set
Set the speed of the character to the number
> Amount 

### Increase Speed
Add to the current speed.
> Amount

### Decrease Speed
Subtract from the current speed.
> Amount

### Initiative Bonus
Add to initiative
> Bonus Amount

### Darkvision
There are two types of Darkvision, Normal and Superior. Normal is at 60 feet and Superior at 120.
This is not implementable in our current build.

### Advantage on
Effect that gives flat advantage on some things. (Roll 2d20 and take the maximum)
> [Ability, Skills, saving throws, weapon attacks, tools, vehicles, conditions, magic, initiative, other]

### Disadvantage on
Effect that gives flat disadvantage on some things. (Roll 2d20 and take the minimum)
> [Ability, Skill, saving throw, weapons, armor, shields, tools, vehicle, conditions, magic, initiative, other] 

# Conditional Immunity
Immunity on conditions for example
> Condition that you are immune to.

### Proficiency on
Gives proficiency on rolls on the specific thing.
> [Ability, Skill, saving throw, weapons, armor, shields, tools, vehicle, conditions, magic, initiative, other]

### Double Proficiency on
Gives two times the proficiency bonus to rolls
> [Ability, Skill, saving throw, tools, vehicle, conditions, magic, initiative, other]

### Language
Learned Language. This is not implementable in our current build.

### Toughness
Increase hit point maximum by x each level.
> Number, Specific class levels, Specific level and above.

### Cantrip as Feature
Some features give you cantrips to use.
> Cantrip, Spellcasting Modifier(Wisdom, Intelligence, Charisma).

### Spell as Feature
Some features give you spells to use. You cannot upcast this.
> Spell,  Spellcasting Modifier(Wisdom, Intelligence, Charisma).

### Resistance
Is being dealt half times the damage from the specific damage type.
>Damage type [slashing, piercing, bludgeoning, cold, poison, acid, psychic, fire, necrotic, radiant, force, thunder, lightning]
### Immunity
Is being dealt no damage from the specific damage type.
>Damage type [slashing, piercing, bludgeoning, cold, poison, acid, psychic, fire, necrotic, radiant, force, thunder, lightning]
### Vulnerability
Is being dealt two times the damage from the specific damage type.
>Damage type [slashing, piercing, bludgeoning, cold, poison, acid, psychic, fire, necrotic, radiant, force, thunder, lightning]

### Add Spell To Spell List
Add a spell to your specific class spell list
> Class, spell

### Halfing Luck
Reroll aces once only on d20s.

### Attack:
General effect that makes a specific attack
>Shape(Not Usable), Range(Not Usable), Radius(Not Usable), Attack Type(Not Usable) (Ranged, melee)(Not usable), Modifier Bonus, Proficiency, Damage(Dices and pluses), Damage Type, Amount of targets.

### Relentless Endurance:
X times per (short) long rest when dead don't die
> Times

### Savage attack:
On critical with specific weapon type roll extra X weapon damage dice
> Weapon, X number

### Bonus Damage
This can be a dice bonus or a flat bonus.
> Number-D-Dices, Flat Number
## Barbarian

### Unarmored Defense:
This has several different editions from having a flat ac to having 10 + 2 modifiers to having 16 + proficiency(warforged).
> Flat AC(Number), modifiers(list of abilities), proficiency (True, False) 

### Extra Attack:
Not usable probably.

### Extra Attack On Bonus Action:
X amount of attacks with Y Weapon on Bonus action.
> 

### Rage:
>Activatable Some times, Rage can be made using Advantage(Strength), Bonus Damage(depending on level), Resistance(Bludgeoning), Resistance(Piercing), Resistance(Slashing)

### Reckless Attack
> Activatable, Can be made with advantage (Meelee attack rolls with). !! Problem we cannot determine between attacking with dex and attacking with strength

### Danger Sense
> Advantage (Dex saving throw)

### Ability Score Improvement
>Ability Score Increase

### Extra Attack
> Extra Attack

### Feral Instict
> Advantage(initiative) !!The rest of this ability is impossible to implement

### Brutal Critical
> Savage Attack (amount of dice vary)

### Relentless Rage
> This is a cluster#$%@ of an ability.

### Persistence Rage
> Upgrade to Rage to have infinity duration.

### Indomitable Might
> Use Strength score for Strength Check.

###Primal Champion
> Ability Score Max Increase(Strength, Consitution), Ability Score Increase(Strength, Consitution, +4 on both)

## Berserker Barbarian
>Extra Attack on Bonus Action