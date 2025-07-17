# Dictionary mapping age groups to writing styles
AGE_GROUP_STYLES = {
    "kids": {
        "style": "very most Simple and easy , magical language with short sentences. Like early Harry Potter books by J.K. Rowling.",
        "elements": ["whimsical", "hopeful", "clear moral lessons"],
        "tone": "cheerful and wondrous",
        "sentence_length": "short",
        "vocabulary": "basic"
    },
    "teens": {
        "style": "Fast-paced with emotional depth. Similar to Percy Jackson by Rick Riordan or Hunger Games by Suzanne Collins.",
        "elements": ["coming-of-age", "identity", "friendship"],
        "tone": "adventurous and emotional",
        "sentence_length": "medium",
        "vocabulary": "moderate"
    },
    "young adults": {
        "style": "Complex characters with romantic subplots. Like A Court of Thorns and Roses by Sarah J. Maas.",
        "elements": ["romance", "personal growth", "rebellion"],
        "tone": "dramatic and intense",
        "sentence_length": "varied",
        "vocabulary": "rich"
    },
    "adults": {
        "style": "Gritty realism with political intrigue. Similar to Game of Thrones by George R.R. Martin.",
        "elements": ["moral ambiguity", "complex plots", "world-building"],
        "tone": "dark and sophisticated",
        "sentence_length": "longer",
        "vocabulary": "advanced"
    },
    "seniors": {
        "style": "Classic epic fantasy style. Like Lord of the Rings by J.R.R. Tolkien.",
        "elements": ["wisdom", "tradition", "nostalgia"],
        "tone": "reflective and majestic",
        "sentence_length": "varied",
        "vocabulary": "literary"
    }
}

def get_writing_style(age_group):
    """Returns the appropriate writing style for the age group"""
    age_group = age_group.lower()
    return AGE_GROUP_STYLES.get(age_group, AGE_GROUP_STYLES["teens"])  # Default to teens style