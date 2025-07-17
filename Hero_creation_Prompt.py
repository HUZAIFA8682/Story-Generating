def Hero_creation_prompt(Hero_name,Hero_specie,Hero_Gender,Dress_color,Hero_Class,Hero_Nature,Hero_age,Hero_Skill,Hero_weapon):

    prompt = f'''
    Create a detailed Hero character map for a fantasy story inspired by Dungeons and Dragons. Use the following user inputs:
    - Hero' Name : {Hero_name}
    - Hero's Species:{Hero_specie}
    - Hero's Gender: {Hero_Gender}
    - Dress Color: {Dress_color}
    - Hero Class: {Hero_Class}    E.g., Fighter, Wizard, Rogue, Cleric, Ranger, Bard, etc.
    - Hero Alignment: {Hero_Nature} E.g., Lawful Good, Chaotic Neutral, Neutral Evil, etc.
    - Hero Age Group: {Hero_age}
    - Hero Key Skills : {Hero_Skill} E.g., Bow & arrows, fire magic, stealth, healing
    - Hero Weapon : {Hero_weapon} E.g it would be the Gun , Sword , Pistol , Sniper or any other thing

    Provide the character map in a structured format.

    '''
    return prompt