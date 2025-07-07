history = []

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    history.append({"user": user_input})
    response = "This is a simulated Gemini response."
    history.append({"gemini": response})
    print("Gemini:", response)
