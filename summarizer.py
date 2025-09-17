import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load .env file
load_dotenv()

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",   # Fast & free
    api_key=os.getenv("GROQ_API_KEY")
)

# Step 1: Load transcript from file (from Day 2)
with open("transcript.txt", "r", encoding="utf-8") as f:
    transcript_text = f.read()

# Step 2: Summarize the transcript
prompt = f"Summarize the following YouTube transcript into 5 bullet points:\n\n{transcript_text}"

response = llm.invoke(prompt)

print("\n--- VIDEO SUMMARY ---")
print(response.content)



# After generating the summary
summary_file = "video_summary.txt"  # you can change the name or path
with open(summary_file, "w", encoding="utf-8") as f:
    f.write(response.content)  # write the text content

print(f"Summary saved to {summary_file}")
