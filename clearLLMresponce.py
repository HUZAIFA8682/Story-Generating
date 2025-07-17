import json

def cleanResponse(llm_response):
    '''
        Purpose: Cleans the json response returned from LLM to preserve the JSON data only
        Input: String returned from LLM
        Output: JSON data retrieved from LLM response
    '''

    print("Raw LLM Response:", llm_response)  # Debugging Output

    # Directly return JSON if no brackets are found
    if '[' not in llm_response or ']' not in llm_response:
        try:
            return json.loads(llm_response)
        except json.JSONDecodeError as e:
            print("Error: Response is not valid JSON:", e)
            return None  # or handle it as needed

    try:
        # Extract JSON substring between the first '[' and the last ']'
        json_start = llm_response.find('[')
        json_end = llm_response.rfind(']') + 1  # Ensure the closing bracket is included

        if json_start == -1 or json_end == -1:
            raise ValueError("Error: Could not locate JSON brackets in the response")

        json_data = llm_response[json_start:json_end]
        print("Extracted JSON String:", json_data)  # Debugging Output

        # Attempt to parse extracted JSON
        return json.loads(json_data)

    except (json.JSONDecodeError, ValueError) as e:
        print("Error: Failed to parse JSON -", e)
        return None  # Handle error gracefully