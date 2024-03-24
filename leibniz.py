from dotenv import load_dotenv
load_dotenv()
import os
import argparse
import google.generativeai as gemini


# Configure Gemini API
gemini.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Get the current working directory
current_dir = os.getcwd()

# Prompt for Gemini AI
gemini_prompt = f"""
You are a command line interface in a Windows machine that can execute simple commands based on natural language input. The current working directory is: {current_dir}

Your task is to take the natural language command provided, interpret it, and generate the corresponding command line command that can be executed in a terminal or command prompt.

Some examples:

Natural language command: "Make a new folder called 'project'"
Command line command: mkdir project

Natural language command: "Initialize a new Git repository in the current directory"
Command line command: git init

Natural language command: "List all files in the current directory"
Command line command: dir

Only provide the command line command as your output, without any additional text or formatting.
"""
        

def main():
    print("""
                                    .-.      .-.
                                    |/`\\.._|/`\.
                _..._,,--.         `\ /.--.\ _.-. 
            ,/'  ..:::.. \     .._.-'/    \` .\/ 
            /       ...:::.`\ ,/:..| |(o)  / /o)|
            |:..   |  ..:::::'|:..  ;\ `---'. `--'
            ;::... |   .::::,/:..    .`--.   .:.`\_
            |::.. ;  ..::'/:..   .--'    ;\   :::.`\.
            ;::../   ..::|::.  /'          ;.  ':'.---.
            `--|    ..::;\:.  `\,,,____,,,/';\. (_)  |)
                ;     ..::/:\:.`\|         ,__,/`;----'
                `\       ;:.. \: `-..      `-._,/,_,/
                \      ;:.   ). `\ `>     _:
                    `\,  ;:..    \ \ _>     >'
                    
               __  _      ____  __ __    ___ 
              /  ]| |    |    ||  |  |  /  _]
             /  / | |     |  | |  |  | /  [_ 
            /  /  | |___  |  | |  |  ||    _]
           /   \_ |     | |  | |  :  ||   [_ 
           \     ||     | |  |  \   / |     |
            \____||_____||____|  \_/  |_____|
                                  

    """)
    

    
    #Main loop
    while True:
        natural_command = input("Ask Clive (or 'ec2047' to quit): ")
        if natural_command.lower() == "ec2047":
            break

        # Generate command line command using Gemini AI
        model = gemini.GenerativeModel("gemini-pro")
        response = model.generate_content([gemini_prompt, natural_command])
        print(response.text.strip())
        cli_command = response.text.strip()

        # Execute the command line command
        os.system(cli_command)

if __name__ == "__main__":
    main()