import json
from typing import Dict, List

class StoryManager:
    def __init__(self):
        self.story_episodes = []
        self.current_episode = 0
        self.story_metadata = {}
    
    def initialize_story(self, user_inputs: Dict):
        """Store initial user inputs and prepare for episode generation"""
        self.story_metadata = user_inputs
        self.current_episode = 0
        self.story_episodes = []
    
    def add_episode(self, episode_content: str):
        """Add a new episode to the story"""
        self.story_episodes.append(episode_content)
        self.current_episode += 1
    
    def get_previous_episode(self) -> str:
        """Get the most recent episode for context"""
        if self.story_episodes:
            return self.story_episodes[-1]
        return None
    
    def save_story(self, filename: str):
        """Save the complete story to a file"""
        story_data = {
            'metadata': self.story_metadata,
            'episodes': self.story_episodes
        }
        with open(filename, 'w') as f:
            json.dump(story_data, f)
    
    def load_story(self, filename: str):
        """Load a story from file"""
        with open(filename, 'r') as f:
            story_data = json.load(f)
        self.story_metadata = story_data['metadata']
        self.story_episodes = story_data['episodes']
        self.current_episode = len(self.story_episodes)