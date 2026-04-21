import sys

class MedicalExpertSystem:
    def __init__(self):
        # KNOWLEDGE REPRESENTATION: SEMANTIC NETWORK & PRODUCTION RULES 
        self.rules = [
            {
                "disease": "Flu (Influenza)",
                "symptoms": ["fever", "body ache", "fatigue", "headache", "chills"],
                "explanation": "High-impact systemic symptoms suggest a viral influenza infection."
            },
            {
                "disease": "Common Cold",
                "symptoms": ["cough", "sore throat", "runny nose", "sneezing"],
                "explanation": "Localized upper respiratory symptoms without high fever characterize a rhinovirus."
            },
            {
                "disease": "Asthma",
                "symptoms": ["wheezing", "shortness of breath", "chest tightness", "persistent cough"],
                "explanation": "Respiratory distress and wheezing indicate bronchial airway inflammation."
            },
            {
                "disease": "Allergic Rhinitis",
                "symptoms": ["sneezing", "itchy eyes", "runny nose", "watery eyes"],
                "explanation": "Itchy, watery eyes and sneezing without fever suggest an allergic reaction."
            },
            {
                "disease": "Bronchitis",
                "symptoms": ["heavy cough", "mucus production", "chest discomfort", "slight fever"],
                "explanation": "Productive cough and chest discomfort point toward bronchial tube inflammation."
            },
            {
                "disease": "Gastroenteritis",
                "symptoms": ["nausea", "vomiting", "diarrhea", "stomach cramps"],
                "explanation": "Gastrointestinal distress suggests a viral or bacterial infection of the digestive tract."
            }
        ]

    def forward_chaining(self, user_symptoms):
        print("\n[LOG] Initializing Inference Engine...")
        print(f"[LOG] Facts gathered: {', '.join(user_symptoms)}")
        
        possible_diagnoses = []
        
        for rule in self.rules:
            # Logic: Count how many symptoms provided match the rule
            matched_symptoms = [s for s in rule["symptoms"] if s in user_symptoms]
            match_count = len(matched_symptoms)
            
            if match_count > 0:
                # Calculate confidence score based on match percentage 
                confidence = (match_count / len(rule["symptoms"])) * 100
                possible_diagnoses.append({
                    "disease": rule["disease"],
                    "confidence": confidence,
                    "explanation": rule["explanation"],
                    "matched": matched_symptoms
                })
        
        # Sort by confidence for the most accurate output
        return sorted(possible_diagnoses, key=lambda x: x['confidence'], reverse=True)

def run_expert_system():
    expert = MedicalExpertSystem()
    
    print("-"*50)
    print("   AI MEDICAL DIAGNOSIS EXPERT SYSTEM   ")
    print("-"*50)
    print("Instructions: Enter symptoms separated by commas.")
    print("Available symptoms include: fever, fatigue, cough, wheezing, ")
    print("nausea, itchy eyes, body ache, runny nose, etc.")
    print("." * 50)
    
    # ACCEPT USER INPUTS 
    user_input = input("\nEnter symptoms: ").lower()
    if not user_input.strip():
        print("Error: No symptoms provided.")
        return

    user_symptoms = [s.strip() for s in user_input.split(",")]
    
    # TRIGGER INFERENCE 
    results = expert.forward_chaining(user_symptoms)
    
    # GENERATE CONCLUSIONS WITH EXPLANATION 
    if results:
        print("\n--- INFERENCE RESULTS & LOGICAL REASONING ---")
        for res in results:
            print(f"\nDIAGNOSIS: {res['disease']}")
            print(f"CONFIDENCE: {res['confidence']:.1f}%")
            print(f"LOGIC: Matched {res['matched']} from Rule Base.")
            print(f"EXPLANATION: {res['explanation']}")
            print("." * 30)
    else:
        print("\nCONCLUSION: No specific diagnosis reached. Knowledge base insufficient.")

if __name__ == "__main__":
    run_expert_system()