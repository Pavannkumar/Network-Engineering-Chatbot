import os
from groq import Groq
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Conversation history — stores all messages for multi-turn memory
conversation_history = []

# System prompt — defines the chatbot as a network engineering expert
SYSTEM_PROMPT = """You are an expert network engineer with 15+ years of experience in enterprise networking.
You have deep knowledge in:
- BGP routing, route flapping, hijacks, and path selection
- SD-WAN technologies including Palo Alto ION and Cloudgenix
- Cisco, HP, Aruba, Brocade, H3C routers and switches
- WAN/LAN troubleshooting, VLAN configurations, ACLs
- DNS, DHCP, NAT, VPN technologies
- Network security including TACACS, RADIUS, Cisco ISE
- SNMP monitoring and network automation
- Vulnerability patching and compliance remediation

Provide clear, practical, and professional answers.
When troubleshooting, give step-by-step guidance.
Use real-world examples where relevant.
Keep responses concise but comprehensive."""


def chat(user_message):
    """Send a message and get a response from Groq."""

    # Add user message to conversation history
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    # Send to Groq API with full conversation history
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + conversation_history,
        max_tokens=1024,
        temperature=0.7
    )

    # Extract response text
    assistant_message = response.choices[0].message.content

    # Add response to conversation history
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    return assistant_message


def main():
    """Main loop — runs the chatbot in the terminal."""

    print("=" * 60)
    print("   Network Engineering Assistant")
    print("   Powered by Groq AI")
    print("=" * 60)
    print("Ask any networking question. Type 'exit' to quit.")
    print("Type 'clear' to reset the conversation.")
    print("=" * 60)
    print()

    while True:
        # Get user input
        user_input = input("You: ").strip()

        # Skip empty input
        if not user_input:
            continue

        # Exit command
        if user_input.lower() == "exit":
            print("\nGoodbye!")
            break

        # Clear conversation
        if user_input.lower() == "clear":
            conversation_history.clear()
            print("\nConversation cleared. Starting fresh!\n")
            continue

        # Get response
        print("\nAssistant:", end=" ", flush=True)
        response = chat(user_input)
        print(response)
        print()


if __name__ == "__main__":
    main()