from dotenv import load_dotenv
load_dotenv()
import os
import argparse
import voice 
import google.generativeai as gemini

# Get the current working directory
current_dir = os.getcwd()

# Function to handle API key retrieval and storage
def get_api_key():
    """Retrieves the API key from the environment or prompts the user for it.
    Stores the key in a .env file if it's not present."""

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("API key not found. Please enter your Gemini API key:")
        api_key = input()
        with open(".env", "w") as f:
            f.write(f"GEMINI_API_KEY='{api_key}'")
    return api_key

# Configure Gemini API using the retrieved key
def configure_gemini():
    """Configures the Gemini API with the API key."""

    try:
        api_key = get_api_key()
        gemini.configure(api_key=api_key)
    except Exception as e:  # Catch any exceptions during configuration
        print(f"Error configuring Gemini API: {e}")

def main():
    
    clive_text = "\033[96m" + """
                                    .-.      .-.
                                    |/`\\.._|/`\\.
                _..._,,--.         `\\ /.--.\\ _.-. 
            ,/'  ..:::.. \\     .._.-'/    \\\\` .\\ 
            /       ...:::.`\\ ,/:..| |(o)  / /o)| /
            |:..   |  ..:::::'|:..  ;\\ `---'. `--'
            ;::... |   .::::,/:..    .`--.   .:.`\\_
            |::.. ;  ..::'/:..   .--'    ;\\   :::.`\\.
            ;::../   ..::|::.  /'          ;.  ':'.---.
            `--|    ..::;\\:.  `\\,,,____,,,/';;\\. (_)  |)
                ;     ..::/:\\:.`\\|         ,__,/`;----'
                `\\       ;:.. \\: `-..      `-._,/,_,/
                \\      ;:.   ). `\\ _>     _:
                    `\\,  ;:..    \\ \\ _>     >'""" + "\033[0m"

    squirrel_text = "\033[38;2;0;128;0m" + """
               __  _      ____  __ __    ___ 
              /  ]| |    |    ||  |  |  /  _]
             /  / | |     |  | |  |  | /  [_ 
            /  /  | |___  |  | |  |  ||    _]
           /   \_ |     | |  | |  :  ||   [_ 
           \     ||     | |  |  \   / |     |
            \____||_____||____|  \_/  |_____| / BETA /
                                  
        
          ** Tip: For best results run Clive in the directory you intend to work in.**  
          ** Tip: Say 'let me talk' to switch to speech input mode. Start typing to go back to text input.**""" + "\033[0m"

    print(clive_text)
    print(squirrel_text)

    # wd_bool = input("\n\nDo you want to set a working directory?(y/n): ")
    # if wd_bool == 'y' or wd_bool == 'Y' or wd_bool == 'yes' or wd_bool == 'Yes':
    #     current_dir = input("Enter proper path: ")

    # Prompt for Gemini AI
    gemini_prompt = f"""
    You are a virtual assistant for the Windows command line, that can execute simple commands based on natural language input. The current working directory is: {current_dir} and always work within this directory unless told explicitly to change the directory.

    Your task is to take the natural language command provided, interpret it, and generate the corresponding command line command that can be executed in a terminal or command prompt.

    Some examples:

    Natural language command: "Make a new folder called 'project'"
    Command line command: cd {current_dir} && mkdir Documents mkdir project

    Natural language command: "Make a new folder called 'project' at 'P:\Desktop\Folder'"
    Command line command: cd P:\Desktop\Folder && mkdir Documents mkdir project

    Natural language command: "Initialize a new Git repository in the current directory"
    Command line command: cd {current_dir} && git init

    Natural language command: "Initialize a new Git repository at 'P:\Desktop\Folder'"
    Command line command: cd P:\Desktop\Folder && git init

    Natural language command: "List all files in the current directory"
    Command line command: dir

    Natural language command: "Copy 'report.txt' to the Desktop"
    Command line command: copy report.txt "%userprofile%\Desktop" 
    (This includes handling path expansion for the user's Desktop)

    Natural language command: "Delete 'temp.txt'" -> 
    Command line command: del temp.txt
    
    Natural language command: "Tell me about my computer's resources" ->
    Command line command: systeminfo 
    (This example demonstrates providing more complex commands)

    basically current directory means: {current_dir}

    And always remember that you are working in a windows machine. Take your time to think and provide the most accurated solution for the stated problem
    Only provide the command line command as your output, without any additional text or formatting.
    """

    speech_mode = False
    while True:
        if not speech_mode:
            user_choice = input("Ask Clive: ")
        else:
            user_choice = voice.recognize_speech(timeout=1.5)  
            if user_choice is None:
                # Check for timeout or recognition error
                print("No speech detected. Press Enter to continue listening or type to exit speech mode.")
                user_choice = input()
                if not user_choice:
                    continue  
                else:
                    speech_mode = False  

        if user_choice.lower() == "let me talk":
            speech_mode = True
            print("Speech input mode activated. Say anything or start typing to exit.")
        elif user_choice.lower() == "ec2047":
            break
        else:
            speech_mode = False  

        if not speech_mode:
            # Text input mode
            natural_command = user_choice
        else:
            # Speech input mode
            continue  

        # Generate command line command using Gemini AI
        model = gemini.GenerativeModel("gemini-pro")
        response = model.generate_content([gemini_prompt, natural_command])
        print(response.text.strip())
        cli_command = response.text.strip()

        # Execute the command line command
        os.system(cli_command)

if __name__ == "__main__":
    configure_gemini()
    main()