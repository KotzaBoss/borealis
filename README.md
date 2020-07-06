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

Choose type of diagram for prototyping

### Mermaid Flowchart

 ```mermaid
graph LR;
	classDef UI color:white,stroke-width:10px
	classDef Overlord color:red
	classDef Overseer color:grey
	
	UI((UI)):::UI
	Azathoth{Azathoth}:::Overlord
	Ares{{Ares}}:::Overlord
	Mnemosyne{{Mnemosyne}}:::Overlord
	Hypnos{{Hypnos}}:::Overlord
	Fortuna{{Fortuna}}:::Overlord
	Amun{{Amun}}:::Overlord
	Cthulhu{{Cthulhu}}:::Overlord
	Daloth{{Daloth}}:::Overlord
	UI((UI)):::UI
	EXIT>Exit]
	
	%% Chaos
	UI --> |User input| Azathoth
	Azathoth --> |Combat| Ares --> Daloth
	Azathoth --> |Load| Mnemosyne --> Daloth
	Azathoth --> |Exit| Hypnos --> Daloth
	Azathoth --> |Dice Rolls| Fortuna --> Daloth
	Azathoth --> |Character Creation| Amun --> Daloth
	Azathoth --> |Character Edits| Cthulhu --> Daloth
	Daloth --> ext{Hypnos?}
	ext -->|YES| EXIT
	ext -->|NO| UI
 ```

```mermaid
graph TD;
	classDef UI color:white,stroke-width:10px
	classDef Overlord color:red
	classDef Overseer color:grey
Cthulhu{{Cthulhu}}:::Overlord
AbilityOverseer(AbilityOverseer):::Overseer
Overseer2(Overseer2):::Overseer
Overseer3(Overseer3):::Overseer
%% How is Cthulhu properly graphed?
%% He is constanlty passing the character sheet around?
%% Or should the overseers communicate?
%% SOLID would suggest segregation of work but that makes an ugly diagram
Cthulhu --> AbilityOverseer -.-> Cthulhu
Cthulhu --> Overseer2 -.-> Cthulhu
Cthulhu --> Overseer3 -.-> Cthulhu
```

### Mermaid State Diagram

```mermaid
stateDiagram	
UI
note left of UI
	User CAN ONLY interface with UI
end note
Azathot: Input Controller
Daloth: Output Controller
Amun: Create
Hypnos: Exit
Cthul: Edit
state Cthulhu_Overseers {
	[*] --> AbilityOverseer
	AbilityOverseer --> Overseer2
	Overseer2 --> Overseer3
	Overseer3 --> [*]
}
Mnemosyne: Import
Fortuna: Roll Dice
Ares: Combat

[*] --> UI
UI --> Azathot
Azathot --> Amun
Azathot --> Cthul
Azathot --> Hypnos
Azathot --> Mnemosyne
Azathot --> Fortuna
Azathot --> Ares

Cthul --> Cthulhu_Overseers
Cthulhu_Overseers --> Daloth
Amun --> Daloth
Fortuna --> Daloth
Ares --> Daloth
Mnemosyne --> Daloth
Hypnos --> Daloth

Daloth --> [*]: Hypnos Awakened
Daloth --> UI
```



