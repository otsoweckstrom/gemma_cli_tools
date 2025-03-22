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

<pre lang="markdown"> 
   bash git add . 
   gemma-commit-msg 
   
   Example Output: 
   📂 **Staged Files:** - main.py - utils/helper.py 
   💡 Suggested Commit Message: "Refactor helper logic" 
   Proceed with this commit? (y/n):  </pre>

Limitations:

Relies on Gemma 3:1B, which is small and sometimes imprecise

Commit message quality can vary


Potential Improvements:

Add multi-model support (e.g. Mixtral, LLaMA3)

Train the model with a large set of real commit messages

Allow message tweaking before commit

VS Code integration


## 🔧 Problem

Writing good commit messages is time-consuming and repetitive. Developers often default to vague messages like "update stuff" or skip writing them entirely. This tool uses a local LLM (Gemma 3:1B via Ollama) to generate concise, imperative commit messages based on the actual code changes — right from your terminal.

## 🎯 Target Users

- Developers who want fast, meaningful commits
- Git users working offline (Gemma runs locally!)
- Anyone too lazy to type "Fix stupid bug in helper again"

## 🧩 Bonus Tools Included

### 🔹 `clinky`: AI-Powered CLI Command Generator
A helper script that translates natural language into macOS/Linux terminal commands using Gemma 3:1B.

```bash
python clinky.py "delete a folder named test"
```

**Output:**
```bash
Suggested command: rm -r test
Proceed? (y/n):
```

- ✅ Designed for macOS/Linux, runs locally  
- ⚠️ Commands are executed only if confirmed by the user

---

### 🔹 `gemma-parse-html`: CSS Selector Extractor from HTML
Uses Gemma to guess the most relevant CSS selector from a given HTML file and target element description.

```bash
python gemma-parse-html.py path/to/page.html --target "product price"
```

**Output:**
```
Best CSS Selector: .product-price
```

  
- ⚠️ Accuracy depends on page structure and LLM reasoning

## Community feedback

u/rajdar
Train Gemma to write Conventional Commit messages https://www.deployhq.com/blog/conventional-commits-a-standardized-approach-to-commit-messages

u/schmurfy2
Why do we need to have AI everywhere ?
That's an interesting toy project but I would be really worried if this is really used...

u/alfrheim
AI is a tool, naming and messages are things most people struggle. Having a helping hand is useful.
