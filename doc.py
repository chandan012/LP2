print("Welcome to the Expert Doctor System!")

# Gathering symptoms from the user
print("Please answer the following questions about your symptoms:")
fever = input("Do you have a fever? (yes/no): ").lower()
cough = input("Do you have a cough? (yes/no): ").lower()
headache = input("Do you have a headache? (yes/no): ").lower()
sore_throat = input("Do you have a sore throat? (yes/no): ").lower()
fatigue = input("Do you experience fatigue? (yes/no): ").lower()

# Diagnosing potential health issues based on symptoms
if fever == "yes" and cough == "yes" and headache == "yes" and sore_throat == "yes" and fatigue == "yes":
    print("Based on your symptoms, you may have the flu.")
    print("Recommended medicine: Over-the-counter pain relievers (e.g., acetaminophen) for fever and body aches.")
    print("Care to be taken: Rest, drink plenty of fluids, and avoid contact with others to prevent spreading the flu.")
elif fever == "yes" and cough == "yes" and sore_throat == "yes":
    print("Based on your symptoms, you may have a strep throat.")
    print("Recommended medicine: Antibiotics prescribed by a doctor to treat the bacterial infection.")
    print("Care to be taken: Rest, drink warm fluids, gargle with saltwater, and avoid irritants like smoking.")
elif fever == "yes" and cough == "yes":
    print("Based on your symptoms, you may have a common cold.")
    print("Recommended medicine: Over-the-counter cough syrups or lozenges for cough relief, and fever reducers if needed.")
    print("Care to be taken: Get plenty of rest, drink fluids, and use saline nasal drops for nasal congestion.")
elif fever == "yes":
    print("Based on your symptoms, you may have a fever.")
    print("Recommended medicine: Over-the-counter fever reducers like acetaminophen or ibuprofen.")
    print("Care to be taken: Rest, drink fluids, and use a cool compress to reduce discomfort.")
elif cough == "yes":
    print("Based on your symptoms, you may have a cough.")
    print("Recommended medicine: Over-the-counter cough syrups or lozenges to relieve coughing.")
    print("Care to be taken: Stay hydrated, avoid irritants like smoke, and use a humidifier to moisten the air.")
elif headache == "yes":
    print("Based on your symptoms, you may have a headache.")
    print("Recommended medicine: Over-the-counter pain relievers like acetaminophen or ibuprofen.")
    print("Care to be taken: Rest in a quiet, dark room, apply a cold or warm compress to the forehead.")
elif sore_throat == "yes":
    print("Based on your symptoms, you may have a sore throat.")
    print("Recommended medicine: Over-the-counter pain relievers like acetaminophen or throat lozenges.")
    print("Care to be taken: Drink warm liquids, gargle with saltwater, and avoid irritants like smoking.")
elif fatigue == "yes":
    print("Based on your symptoms, you may be experiencing fatigue.")
    print("Recommended medicine: There is no specific medication for fatigue. Focus on improving sleep and managing stress.")
    print("Care to be taken: Get enough rest, maintain a balanced diet, exercise regularly, and manage stress levels.")
else:
    print("Based on your symptoms, it is difficult to determine the health issue. Please consult a doctor.")

print("Thank you for using the Expert Doctor System. Take care of your health!")
