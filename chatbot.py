import random

# --- 1. KNOWLEDGE BASE (Rules and Responses) ---
# Dictionary where keys are required keywords and values are responses.
RULES = {
    "hello": "Hello! I am a simple health assistant. How can I help you today?",
    "appointment": "To schedule, please call 555-HEALTH. I cannot book appointments.",
    "symptoms": "If your symptoms are severe, contact a doctor immediately. I can only offer general information.",
    "fever": "A fever usually means rest, fluids, and non-prescription pain relief. Seek medical advice if it persists. ensure that you are hydrated.",
    "timings": "Our standard clinic hours are 9 AM to 5 PM, Monday to Friday.",
    "chest pain":"call the emergency services immediately.",
    "bye": "Goodbye! Take care and have a healthy day.",
    
     } 

# --- 2. INPUT PROCESSING FUNCTION ---
def get_bot_response(user_input):
    user_input = user_input.lower().strip() 

    if "bye" in user_input or "exit" in user_input:
        return RULES["bye"], True  # Return response and exit flag
    
    
    for keyword, response in RULES.items():
        if keyword in user_input:
            # If a keyword is found, return the predefined response
            return response, False
    
    # Default Fallback Response (if no match is found)
    default_response = "I did not understand that. You can ask about 'fever', 'appointment', or 'timings'."
    return default_response, False

# --- 3. MAIN CHAT LOOP ---
def run_chat_bot():
    print("🤖 Health Bot: Hello! Type 'bye' to exit.")
    
    is_exiting = False
    
    while not is_exiting:
        user_input = input("You: ")
        
        
        response, should_exit = get_bot_response(user_input)
        
        print(f"🤖 Health Bot: {response}")
        
        if should_exit:
            is_exiting = True

# Execute the chat bot
if __name__ == "__main__":
    run_chat_bot()