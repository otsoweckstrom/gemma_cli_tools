#!/usr/bin/env python3

import ollama
import argparse
import subprocess

def clean_command(command):
    """Removes any markdown-style code blocks from the response."""
    return command.replace("```", "").replace("powershell", "").replace("bash", "").strip()
def get_command(user_input):
    """Generates a macOS/Linux-friendly CLI command using Gemma."""
    prompt = f"""
    You are a macOS terminal assistant. Convert the following request into an accurate macOS Bash command.
    
    **Rules:**
    - ONLY return valid macOS Bash commands.
    - DO NOT include explanations or extra text, ONLY the command.
    - NEVER return markdown formatting like triple backticks (```) or "bash".
    - If unsure, return: "Sorry, I couldn't generate a command for that request."

    **Special macOS Rules:**
    - Use 'rm -r <directory>' instead of 'rm <directory>' to delete directories.
    - Use 'ls -G' instead of 'ls --color=auto'.
    - Use 'networksetup -getinfo Wi-Fi' instead of 'ip a'.
    - Use 'open .' instead of 'xdg-open .'.
    - Use 'brew install <package>' instead of 'apt-get install <package>'.

    **Correct Examples:**
    - "list files in the current directory" → ls -lah
    - "find my IP address" → networksetup -getinfo Wi-Fi
    - "copy file.txt to backup.txt" → cp file.txt backup.txt
    - "create a new folder named test" → mkdir test
    - "find running processes" → ps aux
    - "kill process with ID 1234" → kill -9 1234
    - "check network status" → ifconfig -a
    - "delete file test.txt" → rm test.txt
    - "delete directory test" → rm -r test
    - "restart the computer" → sudo shutdown -r now

    Request: {user_input}
    """

    try:
        response = ollama.chat(model='gemma3:1b', messages=[{"role": "user", "content": prompt}])
        raw_command = response['message']['content'].strip()
        return clean_command(raw_command) if raw_command else "Sorry, I couldn't generate a command for that request."
    except Exception as e:
        return f"Error: {str(e)}"
def execute_command(command):
    """Executes the command properly in a macOS shell."""
    subprocess.run(command, shell=True, executable="/bin/bash")

def main():
    parser = argparse.ArgumentParser(description="Clinky: AI-powered macOS CLI Helper")
    parser.add_argument("query", type=str, help="Describe the command you need")
    args = parser.parse_args()

    command = get_command(args.query)

    if command:
        print(f"\nSuggested command: {command}")
        confirm = input("Proceed? (y/n): ").strip().lower()
        if confirm == "y":
            execute_command(command)
        else:
            print("Command execution canceled.")

if __name__ == "__main__":
    main()
