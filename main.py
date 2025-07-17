import gettextfromGemini as gtfg
from story_manager import StoryManager
import json
import HeroCreation as hc

def main():
    # Initialize story manager
    story_manager = StoryManager()
    
    # Get initial user inputs
    print("Welcome to the Story Generator!")
    print("Enter your Information...")
    
    user_inputs = {
        'AGE_GROUP': input("Enter age group: "),
        'Gender': input("Enter gender: "),
        'LANGUAGE': input("Enter preferred language: "),
        'Heros_name': input("Enter hero's name: "),
        'Race_species': input("Enter race/secies: "),
        'Magic_or_weapon_preference': input("Enter Magic or weapon preference: "),
        'Role_in_the_current_world': input("Enter Hero's Role in the world: "),
        
    }
    
    print("Please Enter the Deatail Information About your Fantasy Hero")
    hero_name = input("Enter Heros Name for Conformation : ")
    hero_specie = input("Enter the Specie of the Hero: ")
    hero_gender = input("Enter Hero's Gender fdr Confirmation: ")
    dress_color = input("Enter Hero's Dress Color: ")
    hero_class = input("Enter Hero Class (e.g., Fighter, Wizard, Rogue, etc.): ")
    hero_alignment = input("Enter Hero Alignment (e.g., Lawful Good, Chaotic Neutral): ")
    hero_age = input("Enter Hero Age Group (e.g., Young, Adult, Elder): ")
    hero_skills = input("Enter Hero Key Skills (e.g., Bow & Arrows, Fire Magic, Stealth): ")
    hero_weapon = input("Enter Heros Weapon : ")

    hc.responce_from_Gemini_of_Hero(
    hero_name,
    hero_specie,
    hero_gender,
    dress_color,
    hero_class,
    hero_alignment,
    hero_age,
    hero_skills,
    hero_weapon
    )
    # Initialize story with user inputs
    story_manager.initialize_story(user_inputs)
    
    # Generate first episode
    print("\nGenerating your first episode...")
    first_episode = gtfg.responce_from_Gemini(**user_inputs)
    story_manager.add_episode(first_episode)
    print("\n=== Episode 1 ===\n")
    print(first_episode)
    
    # Main interaction loop
    while story_manager.current_episode < 24:
        command = input("\nType 'next' to continue the story or 'quit' to exit: ").lower()
        
        if command == 'quit':
            save = input("Would you like to save your story? (y/n): ").lower()
            if save == 'y':
                filename = input("Enter filename to save: ")
                story_manager.save_story(filename)
            break
            
        elif command == 'next':
            print(f"\nGenerating episode {story_manager.current_episode + 1}...")
            next_episode = gtfg.responce_from_Gemini(
                **user_inputs,
                previous_episode=story_manager.get_previous_episode(),
                current_episode=story_manager.current_episode + 1
            )
            story_manager.add_episode(next_episode)
            print(f"\n=== Episode {story_manager.current_episode} ===\n")
            print(next_episode)
            
            if story_manager.current_episode == 24:
                print("\nCongratulations! You've completed the full 24-episode story!")
                save = input("Would you like to save your story? (y/n): ").lower()
                if save == 'y':
                    filename = input("Enter filename to save: ")
                    story_manager.save_story(filename)
                break

if __name__ == "__main__":
    main()