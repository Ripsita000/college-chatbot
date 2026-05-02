import tkinter as tk
import re
import random

# Responses
responses = {
    "greeting": ["Hello! How can I help you?", "Hi there!", "Hey!"],
    "timing": ["College timing is 9 AM to 5 PM."],
    "library": ["Library is on the 2nd floor. Timing: 9 AM - 6 PM."],
    "contact": ["You can contact admin at admin@college.com"],
    "courses": ["We offer B.Tech, BCA, MBA and more."],

    "admission": ["You can contact the college administration to apply."],
    "eligibility": ["You must pass higher secondary."],
    "btech_eligibility": ["For B.Tech, science stream is required."],
    "last_date": ["Last date for admission is 10 April 2026."],

    "fee": ["B.Tech: 5,00,000 | BCA/BBA: 4,60,000 | MBA: 4,00,000"],
    "scholarship": ["SVMCM scholarship is available."],
    "concession": ["Fee concession depends on academic performance."],

    "hostel": ["Hostel available with WiFi and mess."],
    "facilities": ["Facilities include WiFi, labs, canteen, sports."],

    "exam": ["Exams are conducted semester-wise."],
    "result": ["Results are available on the website."],

    "campus": ["Campus has labs, library, playground."],
    "faculty": ["Faculty members are highly qualified."],

    "holiday": ["Closed on Sundays and public holidays."],
    "working": ["College runs Monday to Saturday."]
}

# NLP processing
def get_response(user_input):
    user_input = user_input.lower()
    user_input = re.sub(r'[^\w\s]', '', user_input)

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return random.choice(responses["greeting"])

    elif "time" in user_input or "timing" in user_input:
        return random.choice(responses["timing"])

    elif any(word in user_input for word in ["library", "lab"]):
        return random.choice(responses["library"])

    elif any(word in user_input for word in ["contact", "email"]):
        return random.choice(responses["contact"])

    elif "course" in user_input:
        return random.choice(responses["courses"])

    elif "admission" in user_input or "apply" in user_input:
        return random.choice(responses["admission"])

    elif "eligibility" in user_input:
        return random.choice(responses["eligibility"])

    elif "btech" in user_input and ("eligibility" in user_input or "qualification" in user_input):
        return random.choice(responses["btech_eligibility"])

    elif "last date" in user_input or "deadline" in user_input:
        return random.choice(responses["last_date"])

    elif any(word in user_input for word in ["fee", "fees", "cost"]):
        return random.choice(responses["fee"])

    elif "scholarship" in user_input:
        return random.choice(responses["scholarship"])

    elif "concession" in user_input:
        return random.choice(responses["concession"])

    elif any(word in user_input for word in ["hostel", "wifi"]):
        return random.choice(responses["hostel"])

    elif any(word in user_input for word in ["facility", "canteen"]):
        return random.choice(responses["facilities"])

    elif any(word in user_input for word in ["exam", "schedule"]):
        return random.choice(responses["exam"])

    elif "result" in user_input:
        return random.choice(responses["result"])

    elif any(word in user_input for word in ["campus", "location"]):
        return random.choice(responses["campus"])

    elif any(word in user_input for word in ["faculty", "teacher"]):
        return random.choice(responses["faculty"])

    elif "holiday" in user_input:
        return random.choice(responses["holiday"])

    elif "working" in user_input or "days" in user_input:
        return random.choice(responses["working"])

    else:
        return "Sorry, I didn't understand. Ask about admission, fees, courses, etc."

# GUI function
def send_message():
    user_input = entry.get()

    chat_log.insert(tk.END, "You: " + user_input + "\n")

    response = get_response(user_input)
    chat_log.insert(tk.END, "Bot: " + response + "\n\n")
    
    chat_log.see(tk.END)

    entry.delete(0, tk.END)

# Window
root = tk.Tk()
root.title("College Chatbot")
root.geometry("500x500")
root.configure(bg="#1e1e1e")

root.bind('<Return>', lambda event: send_message())

# Chat area
chat_log = tk.Text(root, width=60, height=20,font=("Arial", 12), bg="#1e1e1e" , fg="white",  insertbackground="white")
chat_log.pack(pady=10)

# Entry box
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

# Button
send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack()

clear_btn = tk.Button(root, text="Clear Chat",command=lambda: chat_log.delete(1.0, tk.END))

root.mainloop()