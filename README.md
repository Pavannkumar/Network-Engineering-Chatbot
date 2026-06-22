# Network Engineering Assistant Chatbot

An AI-powered terminal chatbot for network engineers, built with Python and Groq AI.
Ask any networking question and get expert, practical answers with real CLI examples.

## What It Does

- Answers questions on BGP, SD-WAN, Cisco, Palo Alto, VLANs, DNS, TACACS and more
- Provides step-by-step troubleshooting guidance with real CLI commands
- Maintains conversation context across multiple questions
- Runs entirely in the terminal

## Tech Stack

- Python 3.x
- Groq AI API (llama-3.3-70b-versatile)
- python-dotenv

## Setup

1. Clone the repository: git clone https://github.com/Pavannkumar/Network-Engineering-Chatbot.git
2. Install dependencies: pip install groq python-dotenv
3. Create a .env file: GROQ_API_KEY=your_groq_api_key_here
4. Run: python chatbot.py

## Get a Free Groq API Key

Sign up at https://console.groq.com - completely free, no credit card required.

## Example Questions

- What causes BGP route flapping and how do I fix it on a Cisco router?
- How do I configure TACACS on a Cisco device?
- What is the difference between iBGP and eBGP?
- How do I troubleshoot a Palo Alto SD-WAN link failure?

## Commands

- Type your question and press Enter
- Type clear to reset the conversation
- Type exit to quit