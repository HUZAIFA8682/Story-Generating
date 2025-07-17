import requests
import config
import Hero_creation_Prompt as hcp
import clearLLMresponce as cLLMr
import json


if config.LLM_responce == "Gemini":
    # Replace with your actual Gemini API key
    API_KEY = 'AIzaSyARS3X7-s-tZ6EbKuTt3H4TBRylDAmXh_4'
    API_URL = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent'
    
    def responce_from_Gemini_of_Hero(
        Hero_name,Hero_specie,Hero_Gender,Dress_color,Hero_Class,Hero_Nature,Hero_age,Hero_Skill,Hero_weapon
    ):
        hero_prompt = hcp.Hero_creation_prompt(
            Hero_name=Hero_name,Hero_specie=Hero_specie,Hero_Gender=Hero_Gender,Dress_color=Dress_color,Hero_Class=Hero_Class,Hero_Nature=Hero_Nature,Hero_age=Hero_age,Hero_Skill=Hero_Skill,Hero_weapon=Hero_weapon
        )
        
        headers = {
            'Content-Type': 'application/json',
            'X-goog-api-key': API_KEY
        }

        data = {
            "contents": [
                {
                    "parts": [
                        {"text": hero_prompt}
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
