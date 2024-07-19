# Automated Text Selection and Chat Response

This project uses Python to automate the selection and copying of text from a specified area on the screen, sending it to OpenAI's GPT-3.5-turbo model for analysis, and pasting the response back to the screen.

## Features

- Automates text selection and copying using `pyautogui`
- Sends copied text to OpenAI's GPT-4 model for analysis
- Pasts the response back to a specified location on the screen

## Requirements

- Python 3.x
- An OpenAI API key
- The following Python packages:
  - `pyautogui`
  - `pyperclip`
  - `openai`

## Setup

1. Clone the repository:
    ```bash
   https://github.com/GIRIRAJSHANKAR27/AutoMated_Chat_Response.git
    cd AutoMated_Chat_Response
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    source .venv/bin/activate    # On Windows: .venv\Scripts\activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory of the project and add your OpenAI API key:
    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. Run the script:
    ```bash
    python main.py
    python program.py
    ```

2. The script will:
    - Move the mouse to the specified coordinates and click to open the chat
    - Select and copy the text from the chat area
    - Send the copied text to the OpenAI model
    - Paste the response back to the chat input area and press Enter
