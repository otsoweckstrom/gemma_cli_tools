# 💬 gemma-commit

Generate clear, short Git commit messages using a local LLM (Gemma 3:1B via Ollama).

## What It Does

Analyzes your staged Git changes and suggests a short, imperative commit message — all offline using open-source LLMs.

## Why?

Writing good commit messages sucks. Let the AI do it. It's fast, local, and doesn’t send your code to the cloud.

## 📦 Installation

1. Install [Ollama](https://ollama.com/)
2. Pull the model:
   bash ollama pull gemma3:1b
   
Clone this repo & move the tool to a global path:
chmod +x gemma-commit
sudo mv gemma-commit /usr/local/bin/

Usage:

<pre lang="markdown"> ```bash git add . 
   gemma-commit-msg 
   Example Output: 📂 **Staged Files:** - main.py - utils/helper.py 
   💡 Suggested Commit Message: "Refactor helper logic" 
   Proceed with this commit? (y/n): ``` </pre>

Limitations:
Relies on Gemma 3:1B, which is small and sometimes imprecise
Commit message quality can vary

Potential Improvements:
Add multi-model support (e.g. Mixtral, LLaMA3)
Allow message tweaking before commit
VS Code integration


## 🔧 Problem

Writing good commit messages is time-consuming and repetitive. Developers often default to vague messages like "update stuff" or skip writing them entirely. This tool uses a local LLM (Gemma 3:1B via Ollama) to generate concise, imperative commit messages based on the actual code changes — right from your terminal.

## 🎯 Target Users

- Developers who want fast, meaningful commits
- Git users working offline (Gemma runs locally!)
- Anyone too lazy to type "Fix stupid bug in helper again"
