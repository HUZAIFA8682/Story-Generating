import requests
import json
import generate_story_prompt as gsp
import clearLLMresponce as cLLMr
import config 

if config.LLM_responce == "Gemini":
    # Replace with your actual Gemini API key
    API_KEY = 'AIzaSyARS3X7-s-tZ6EbKuTt3H4TBRylDAmXh_4'
    API_URL = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent'
    
    def responce_from_Gemini(
        AGE_GROUP, Gender, LANGUAGE, Heros_name,
        Race_species, Magic_or_weapon_preference, Role_in_the_current_world,
        previous_episode=None, current_episode=1  # Added new parameters here
    ):
        story_prompt = gsp.generate_story_prompt(
        
            AGE_GROUP=AGE_GROUP,
            Gender=Gender,
            LANGUAGE=LANGUAGE,
            Heros_name=Heros_name,
            Race_species=Race_species,
            Magic_or_weapon_preference=Magic_or_weapon_preference,
            Role_in_the_current_world=Role_in_the_current_world,
            previous_episode=previous_episode,  # Passing new parameters
            current_episode=current_episode
        )
        
        headers = {
            'Content-Type': 'application/json',
            'X-goog-api-key': API_KEY
        }

        data = {
            "contents": [
                {
                    "parts": [
                        {"text": story_prompt}
                    ]
                }
            ]
        }

        response = requests.post(API_URL, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            result = response.json()
            response_text = result['candidates'][0]['content']['parts'][0]['text']
        else:
            raise Exception(f"Error from Gemini API: {response.status_code} - {response.text}")
        
        cleaned_response = cLLMr.cleanResponse(response_text)
        return cleaned_response

if config.LLM_responce == "Groq":
    def responce_from_Groq(
        AGE_GROUP, Gender, Number, LANGUAGE, Heros_name,
        Race_species, Magic_or_weapon_preference, Role_in_the_current_world,
        previous_episode=None, current_episode=1  # Added new parameters here
    ):
        story_prompt = gsp.generate_story_prompt(
            AGE_GROUP=AGE_GROUP,
            Gender=Gender,
            Number=Number,
            LANGUAGE=LANGUAGE,
            Heros_name=Heros_name,
            Race_species=Race_species,
            Magic_or_weapon_preference=Magic_or_weapon_preference,
            Role_in_the_current_world=Role_in_the_current_world,
            previous_episode=previous_episode,  # Passing new parameters
            current_episode=current_episode
        )
        
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer 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"
        }
        data = {
            "model": "meta-llama/llama-4-scout-17b-16e-instruct",
            "messages": [
                {
                    "role": "user",
                    "content": story_prompt
                }
            ]
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            # Updated to match Groq's actual response structure
            response_text = result['choices'][0]['message']['content']
        else:
            raise Exception(f"Error from Groq API: {response.status_code} - {response.text}")
        
        cleaned_response = cLLMr.cleanResponse(response_text)
        return cleaned_response