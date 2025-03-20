import ollama
import subprocess

def get_staged_diff():
    """Gets the Git diff of staged changes."""
    try:
        result = subprocess.run(["git", "diff", "--staged"], capture_output=True, text=True)
        git_diff = result.stdout.strip()
        return git_diff if git_diff else None
    except Exception as e:
        return f"Error getting diff: {str(e)}"

def generate_commit_message(diff):
    """Uses Gemma to generate a commit message from Git changes."""
    prompt = f"""
    You are an AI that generates Git commit messages.
    
    **Task:**  
    Write a **short, imperative commit message** based on the code changes.

    **Git Diff:**
    {diff}

    **Rules:**
    - Keep it under **40 characters**.
    - Use an **imperative tone** (e.g., "Fix bug", "Refactor login system").
    - **Only return the commit message** with no extra words.

    **Example Output:**  
      Fix checkout page validation  
      Update API response handling  
      Optimize query performance  

    **Only return the commit message, nothing else.**
    """

    try:
        response = ollama.chat(model='gemma3:1b', messages=[{"role": "user", "content": prompt}])
        commit_message = response['message']['content'].strip()

        # Ensure the response isn't empty or malformed
        if not commit_message :
            return "Auto-generated commit"

        return commit_message

    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """CLI tool to generate Git commit messages from staged changes."""
    git_diff = get_staged_diff()

    if not git_diff:
        print("No staged changes found. Please stage changes using `git add .`")
        return

    print("\n🔍 **Git Diff (Staged Changes):**\n")
    print(git_diff)  # Display the raw Git diff

    commit_message = generate_commit_message(git_diff)

    print(f"\n💡 **Suggested Commit Message:** \"{commit_message}\"")

    confirm = input("\nProceed with this commit? (y/n): ").strip().lower()
    
    if confirm == "y":
        subprocess.run(["git", "commit", "-m", commit_message])
        print("✅ Commit created!")
    else:
        print("❌ Commit canceled.")

if __name__ == "__main__":
    main()
