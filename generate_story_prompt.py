import writer_styles

def generate_story_prompt(
    AGE_GROUP, Gender, LANGUAGE, Heros_name,
    Race_species, Magic_or_weapon_preference, Role_in_the_current_world,
    previous_episode=None, current_episode=1
):
    # Get the appropriate writing style
    writing_style = writer_styles.get_writing_style(AGE_GROUP)
    
    base_prompt = f'''
    You are a professional fantasy writer creating a story for {AGE_GROUP} readers.
    Writing Style Guidelines:
    - Tone: {writing_style['tone']}
    - Sentence structure: {writing_style['sentence_length']} sentences
    - Vocabulary level: {writing_style['vocabulary']}
    - Key elements: {', '.join(writing_style['elements'])}
    - Model your prose after: {writing_style['style']}
    
    The hero is {Gender} named {Heros_name}, a {Race_species} who prefers {Magic_or_weapon_preference}.
    As a {Role_in_the_current_world}, their journey continues...
    '''

    if previous_episode:
        prompt = f'''
        {base_prompt}
        
        Previous episode summary:
        {previous_episode[-500:]}
        
        Continue the story while maintaining:
        - Consistent {writing_style['tone']} tone
        - {writing_style['style']} style
        - Logical progression from previous events
        - A new challenge that fits the {AGE_GROUP} level
        - A cliffhanger ending
        
        Write only the next episode content in {LANGUAGE}.
        '''
    else:
        prompt = f'''
        {base_prompt}
        
        Create an immersive first episode including:
        - Hero introduction with backstory
        - Initial challenge appropriate for {AGE_GROUP}
        - Introduction of key companions
        - World-building elements
        - A cliffhanger ending
        
        Write only the first episode content in {LANGUAGE}.
        '''
    
    return prompt