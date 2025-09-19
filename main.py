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

def summarize_text(text, style="bullet"):
    """Summarizes transcript in bullet or paragraph form"""
    if style == "bullet":
        prompt = f"Summarize the following transcript into 5 bullet points:\n\n{text}"
    else:
        prompt = f"Summarize the following transcript into 2 detailed paragraphs:\n\n{text}"
    
    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    # Step 1: Load transcript from file
    transcript_file = "transcript.txt"  # make sure this file exists
    with open(transcript_file, "r", encoding="utf-8") as f:
        transcript_text = f.read()

    # Step 2: Choose summary style
    style = input("Choose summary style (bullet/paragraph): ").strip().lower()

    # Step 3: Generate summary
    summary = summarize_text(transcript_text, style)

    # Step 4: Save summary
    summary_file = "video_summary.txt"
    with open(summary_file, "w", encoding="utf-8") as f:
        f.write(summary)

    # Step 5: Print summary
    print("\n--- VIDEO SUMMARY ---")
    print(summary)
    print(f"\n✅ Summary saved to {summary_file}")
