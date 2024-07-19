import pyautogui
import pyperclip
import time
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY"),
)
# Function to perform the required actions
def automate_text_selection_and_copy():
    # Move to the icon position and click
    pyautogui.moveTo(1318, 1043, duration=0.5)
    pyautogui.click()

    # Allow some time for any response after the click
    time.sleep(1)

    # Move to the start position, click and hold
    pyautogui.moveTo(587, 128, duration=0.5)
    pyautogui.mouseDown()

    # Drag to the end position and release
    pyautogui.moveTo(1830, 909, duration=0.5)
    pyautogui.mouseUp()

    # Copy the selected text to the clipboard (Ctrl+C)
    pyautogui.hotkey('ctrl', 'c')

    # Allow some time for the copy action to complete
    time.sleep(0.5)

    # Retrieve the copied text from the clipboard
    copied_text = pyperclip.paste()
    pyautogui.click(1118,1005)
    return copied_text

# Run the function and store the result in a variable
chatHistory = automate_text_selection_and_copy()

# Print the copied text
print("Copied text:", chatHistory)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named giriraj, who's a student at IIIT sonepat and a coder, he speaks in hindi and english. analyse the chat history and respond like giriraj "},
    {"role": "user", "content": chatHistory}
  ]
)

response = completion.choices[0].message.content
pyperclip.copy(response)
# Move to the new position to click and paste the copied text
pyautogui.moveTo(895, 974, duration=0.5)
pyautogui.click()

# Allow some time for the application to respond
time.sleep(0.5)

# Paste the copied text (Ctrl+V)
pyautogui.hotkey('ctrl', 'v')

# Allow some time for the paste action to complete
time.sleep(0.5)

# Press Enter
pyautogui.press('enter')

print("Text pasted and Enter key pressed.")
