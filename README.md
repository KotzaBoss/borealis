<img src="https://images.unsplash.com/photo-1517411032315-54ef2cb783bb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1402&q=80"  width="50%" height="50%" align="center">

---

[[_TOC_]]

# BOREALIS

Borealis is meant to be an interactive supplementary program to the incredible <u>[Aurora Builder](https://aurorabuilder.com)</u> which inspired it.
The primary idea is to give the user a handy "real-time" assistant when they play DnD. From creating, saving, loading characters on the fly,
leveling them up, engaging in combat and so on.  
While Aurora is the "sit-down-relax" companion, Borealis will be the "in-the-trenches" ally.

# TODO
+ [ ] Review code todos
+ [ ] Compile Feats and Features extract generics
+ [ ] Draft program loop
+ [ ] Save/Import interface
+ [ ] Implement history
+ [ ] Import Classes when typing.TYPE_CHECKING

# Program Flow

### Flowchart

 ```mermaid
graph LR;
	classDef UI color:aqua,stroke-width:8px
	classDef Overlord color:red
	classDef Overseer color:grey
	
	UI((UI)):::UI
	Azathoth{{Azathoth}}:::Overlord
	Ares{{Ares}}:::Overlord
	Mnemosyne{{Mnemosyne}}:::Overlord
	Hypnos{{Hypnos}}:::Overlord
	Fortuna{{Fortuna}}:::Overlord
	Amun{{Amun}}:::Overlord
	Cthulhu{{Cthulhu}}:::Overlord
	Daloth{{Daloth}}:::Overlord
	SpellOverlord{{SpellOverlord}}:::Overlord
	UI((UI)):::UI
	extCond{Hypnos?}
	EXIT>Exit]
	
	%% Chaos
	UI --> |User input| Azathoth
	Azathoth --> |Combat| Ares --> Daloth
	Azathoth --> |Load| Mnemosyne --> Daloth
	Azathoth --> |Exit| Hypnos --> Daloth
	Azathoth --> |Dice Rolls| Fortuna --> Daloth
	Azathoth --> |Character Creation| Amun --> Daloth
	Azathoth --> |Character Edits| Cthulhu --> Daloth
	Azathoth --> |Use spells| SpellOverlord -->Daloth
	Daloth --> extCond
	extCond -->|YES| EXIT
	extCond -->|NO - Return output| UI
 ```



```mermaid
graph LR;
	classDef UI color:aqua,stroke-width:10px
	classDef Overlord color:red
	classDef Overseer color:grey
	
	UI((UI)):::UI
	Azathoth{{Azathoth}}:::Overlord
	Cthulhu{{Cthulhu}}:::Overlord
	Daloth{{Daloth}}:::Overlord
	AbilityOverseer(AbilityOverseer):::Overseer
	Overseer2(Overseer2):::Overseer
	Char((Charsheet))
	
	UI --> |Edit requested| Azathoth
	Azathoth --> Cthulhu
	Cthulhu --- AbilityOverseer
	Cthulhu --- Overseer2
	AbilityOverseer -.- Char 
	Overseer2 -.- Char 
	Cthulhu --> |Return edited char sheet| Daloth
	Daloth --> UI
```
```mermaid
graph LR;
	%% Spells
	classDef UI color:aqua,stroke-width:8px
	classDef Overlord color:red
	classDef CharSheet stroke-width:8px
    UI((UI)):::UI
    Char((Character Sheet)):::Charsheet
    SpellOverlord{{SpellOverlord}}:::Overlord
    Daloth{{Daloth}}:::Overlord
    Azathoth{{Azathoth}}:::Overlord
    Spells[Spell Bank]
    
    UI ==> |Request use of spell X| Azathoth
    Azathoth --> SpellOverlord
    SpellOverlord --> |Check Spell System used| Char
    SpellOverlord --> |Grab spell| Spells 
    SpellOverlord --> |Use spell| Daloth
    Char --> Spells
    Daloth --> UI
```

