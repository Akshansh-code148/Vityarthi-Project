AI Content Detector

Project Overview
The AI Content Detector is a Python-based console application that attempts to determine whether a given text appears AI-generated or human-written.
It uses simple heuristic techniques such as:

.AI-style phrase detection

.Sentence-length variance

.Repetitive structure checks

.Based on these patterns, it generates an AI score (0–100) and outputs a verdict.

Features
AI Phrase Detection
Scans for common AI-styled phrases such as “in conclusion”, “moreover”, “furthermore”, etc.

Sentence Length Variance
Analyzes consistency in sentence lengths—very low variance often indicates automated writing.

Score Normalization
Produces a final AI score from 0 to 100.

Clear Verdict
Outputs:
Likely AI-generated
Possibly AI-generated
Likely human-written

Users can paste text repeatedly and type "quit" to exit.

Technologies/tools used
Python 3.x
Only standard python libraries
CLI(Command Line Interface)

Steps to Install and Run the Project
Install Python
Check if Python is installed:
python
Save the Code
Paste the code into it.
Run the python program

Instructions for Testing
1.	Provide AI-sounding text
Example:
In conclusion, it is important to note that this system provides a robust and efficient solution.
Expected: Higher AI score.
2. Test with casual human text
Example:
I woke up late today, made some tea, and then walked my dog. Nothing special.
Expected: Likely Human written


Screenshot

<img width="1480" height="528" alt="image" src="https://github.com/user-attachments/assets/c088ce5a-d1fb-43e9-a180-f26a124e38da" />
