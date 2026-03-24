import streamlit as st
import os
from dotenv import load_dotenv
from supadata import Supadata, SupadataError
from google import genai

# Load environment variables
load_dotenv()

# Initialize clients
supadata = Supadata(api_key=os.getenv("SUPADATA_API_KEY"))
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Page config
st.set_page_config(
    page_title="YouTube Transcript Summarizer",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for black and white minimalist aesthetic - COMPACT VERSION
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Poppins:wght@300;400;600;700&family=Inter:wght@300;400;500&display=swap');
    
    /* Global Background - Pure Black */
    .stApp {
        background: #000000;
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    
    /* Subtle grid pattern overlay */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
        background-size: 50px 50px;
        pointer-events: none;
        z-index: 0;
    }
    
    /* Main Title with Minimalist Style - SMALLER */
    h1 {
        font-family: 'Orbitron', sans-serif !important;
        font-size: 2.5rem !important;
        font-weight: 900 !important;
        text-align: center;
        color: #ffffff !important;
        position: relative;
        padding-bottom: 12px;
        margin-bottom: 15px;
        margin-top: 10px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    
    h1::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 150px;
        height: 2px;
        background: linear-gradient(90deg, transparent, #ffffff, transparent);
        animation: line-pulse 2s ease-in-out infinite;
    }
    
    @keyframes line-pulse {
        0%, 100% { 
            opacity: 0.5;
            width: 150px;
        }
        50% { 
            opacity: 1;
            width: 250px;
        }
    }
    
    /* Subheader - SMALLER */
    .stApp > header + div h3 {
        font-family: 'Poppins', sans-serif !important;
        font-size: 0.95rem !important;
        text-align: center;
        color: #999999;
        font-weight: 300;
        margin-bottom: 25px;
        margin-top: -10px;
        letter-spacing: 0.5px;
    }
    
    /* Input Fields - Clean White Border - SMALLER PADDING */
    .stTextInput > div > div > input {
        background: #000000 !important;
        border: 2px solid #ffffff !important;
        border-radius: 0px !important;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.9rem !important;
        padding: 10px 15px !important;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #ffffff !important;
        box-shadow: inset 0 0 0 1px #ffffff !important;
        outline: none !important;
        background: #111111 !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #555555 !important;
    }
    
    /* Dropdown/Select - Minimalist Style - SMALLER */
    .stSelectbox > div > div {
        background: #000000 !important;
        border: 2px solid #ffffff !important;
        border-radius: 0px !important;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:hover {
        background: #111111 !important;
        box-shadow: inset 0 0 0 1px #ffffff;
    }
    
    .stSelectbox label {
        color: #ffffff !important;
        font-family: 'Poppins', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.8rem !important;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    
    /* Primary Button - Inverted Colors - SMALLER */
    .stButton > button {
        background: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #ffffff !important;
        border-radius: 0px !important;
        padding: 10px 30px !important;
        font-family: 'Poppins', sans-serif !important;
        font-size: 0.95rem !important;
        font-weight: 700 !important;
        transition: all 0.3s ease;
        cursor: pointer;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Force button text to be black */
    .stButton > button p,
    .stButton > button span,
    .stButton > button div {
        color: #000000 !important;
    }
    
    .stButton > button:hover {
        background: #000000 !important;
        color: #ffffff !important;
        box-shadow: inset 0 0 0 2px #ffffff;
        transform: translateY(-2px);
    }
    
    /* Force hover text to be white */
    .stButton > button:hover p,
    .stButton > button:hover span,
    .stButton > button:hover div {
        color: #ffffff !important;
    }
    
    /* Download Button - SMALLER */
    .stDownloadButton > button {
        background: #000000 !important;
        color: #ffffff !important;
        border: 2px solid #ffffff !important;
        border-radius: 0px !important;
        padding: 8px 25px !important;
        font-family: 'Poppins', sans-serif !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stDownloadButton > button:hover {
        background: #ffffff !important;
        color: #000000 !important;
        transform: translateY(-2px);
    }
    
    /* Video Thumbnail Card - SMALLER BORDER */
    .stImage {
        border: 2px solid #ffffff;
        box-shadow: 0 5px 20px rgba(255, 255, 255, 0.08);
        overflow: hidden;
        transition: all 0.3s ease;
        background: #000000;
    }
    
    .stImage:hover {
        box-shadow: 0 10px 35px rgba(255, 255, 255, 0.15);
        transform: translateY(-3px);
    }
    
    /* Summary Display Area - Clean Container - SMALLER */
    div[data-testid="stMarkdownContainer"] {
        background: #000000;
        border: 2px solid #ffffff;
        border-radius: 0px;
        padding: 18px;
        margin: 12px 0;
        max-height: 500px;
        overflow-y: auto;
        font-size: 0.9rem;
    }
    
    /* Custom Scrollbar - White Theme */
    div[data-testid="stMarkdownContainer"]::-webkit-scrollbar {
        width: 6px;
    }
    
    div[data-testid="stMarkdownContainer"]::-webkit-scrollbar-track {
        background: #000000;
        border-left: 1px solid #333333;
    }
    
    div[data-testid="stMarkdownContainer"]::-webkit-scrollbar-thumb {
        background: #ffffff;
        border-radius: 0px;
    }
    
    div[data-testid="stMarkdownContainer"]::-webkit-scrollbar-thumb:hover {
        background: #cccccc;
    }
    
    /* Info/Warning/Error Messages - SMALLER */
    .stAlert {
        background: #000000 !important;
        border: 2px solid #ffffff !important;
        border-radius: 0px !important;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
        padding: 12px 15px !important;
        font-size: 0.9rem !important;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-color: #ffffff transparent #ffffff transparent !important;
    }
    
    /* Footer with Clean Divider - SMALLER */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, #ffffff, transparent);
        margin: 25px 0 15px 0;
    }
    
    /* Footer Text - SMALLER */
    .stMarkdown h3 {
        font-family: 'Poppins', sans-serif !important;
        color: #ffffff !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px;
        margin-bottom: 10px;
        margin-top: 5px;
    }
    
    .stMarkdown ul, .stMarkdown ol {
        font-family: 'Inter', sans-serif !important;
        font-size: 0.85rem !important;
        color: #cccccc !important;
        line-height: 1.6 !important;
    }
    
    .stMarkdown strong {
        color: #ffffff !important;
        font-weight: 700 !important;
    }
    
    .stMarkdown p {
        color: #dddddd !important;
        line-height: 1.6 !important;
        margin: 5px 0 !important;
    }
    
    /* Labels - SMALLER */
    label {
        font-family: 'Poppins', sans-serif !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 0.8rem !important;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    
    /* Fade-in Animation */
    .element-container {
        animation: fadeIn 0.8s ease-in;
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Column containers - REDUCE PADDING */
    .stColumn {
        padding: 5px;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Success/Info boxes - SMALLER */
    .stSuccess {
        background: #000000 !important;
        border: 2px solid #ffffff !important;
        color: #ffffff !important;
        padding: 10px 12px !important;
        font-size: 0.9rem !important;
    }
    
    .stWarning {
        background: #000000 !important;
        border: 2px solid #ffffff !important;
        color: #ffffff !important;
        padding: 10px 12px !important;
        font-size: 0.9rem !important;
    }
    
    .stError {
        background: #000000 !important;
        border: 2px solid #ffffff !important;
        color: #ffffff !important;
        padding: 10px 12px !important;
        font-size: 0.9rem !important;
    }
    
    /* Markdown content styling - SMALLER */
    .stMarkdown h2 {
        font-family: 'Poppins', sans-serif !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px;
        margin-top: 15px;
        margin-bottom: 8px;
        padding-bottom: 8px;
        border-bottom: 1px solid #333333;
        font-size: 1.2rem !important;
    }
    
    /* Make select dropdown text white */
    .stSelectbox div[data-baseweb="select"] > div {
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# Extract video ID from YouTube URL
def extract_video_id(youtube_url):
    if "v=" in youtube_url:
        return youtube_url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in youtube_url:
        return youtube_url.split("youtu.be/")[1].split("?")[0]
    return None

# Get transcript using Supadata SDK
def get_transcript(video_id):
    try:
        transcript_result = supadata.youtube.transcript(
            video_id=video_id,
            text=True
        )
        
        if transcript_result and transcript_result.content:
            return transcript_result.content, None
        else:
            return None, "No transcript content found"
            
    except SupadataError as e:
        error_msg = str(e.message) if hasattr(e, 'message') else str(e)
        return None, f"Supadata Error: {error_msg}"
    except Exception as e:
        return None, f"Error: {str(e)}"

# Generate summary with user-selected language
# New (Gemini)
def generate_summary(transcript, language):
    # Combine system and user content into a single prompt for simpler use
    system_prompt = f"You are a YouTube video summarizer. You MUST respond ONLY in {language}. Create detailed notes with key points, main topics, and important takeaways in a well-structured format with clear sections."
    user_prompt = f"Please summarize this YouTube video transcript in {language} language:\n\n{transcript}"
    
    full_prompt = f"{system_prompt}\n\n{user_prompt}"
    
    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=full_prompt,
            config={
                "temperature": 0.5,
                "max_output_tokens": 2048
            }
        )
        
        return response.text
    except Exception as e:
        return f"Error generating summary with Gemini: {str(e)}"

# Streamlit UI # Main UI
st.markdown("<h1>📝 YouTube Transcript Summarizer</h1>", unsafe_allow_html=True)
st.markdown("<h3>Generate detailed notes from any YouTube video with AI-powered insights</h3>", unsafe_allow_html=True)


# Two columns for better layout
col1, col2 = st.columns([3, 1])

with col1:
    youtube_url = st.text_input(
        "🔗 Enter YouTube Video URL:",
        placeholder="https://www.youtube.com/watch?v=...",
        label_visibility="visible"
    )
with col2:
    # Language selection dropdown
    language = st.selectbox(
        "Summary Language:",
        [
            "English",
            "Malayalam",
            "Hindi",
            "Arabic",
            "Spanish",
            "French",
            "German",
            "Chinese",
            "Japanese",
            "Portuguese",
            "Russian",
            "Italian",
            "Korean"
        ]
    )

# Generate button
if st.button("🎬 Generate Summary", type="primary"):
    if youtube_url:
        with st.spinner(f"Processing video and generating {language} summary..."):
            video_id = extract_video_id(youtube_url)
            
            if video_id:
                # Display video thumbnail
                st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", 
                        use_container_width=True)
                
                # Get transcript
                transcript, error = get_transcript(video_id)
                
                if transcript:
                    # Show transcript length
                    st.info(f"📄 Transcript length: {len(transcript)} characters")
                    
                    # Generate summary in selected language
                    summary = generate_summary(transcript, language)
                    
                    # Display summary
                    st.markdown(f"## 📋 Summary ({language})")
                    st.write(summary)
                    
                    # Download button for summary
                    st.download_button(
                        label="⬇️ Download Summary",
                        data=summary,
                        file_name=f"youtube_summary_{video_id}.txt",
                        mime="text/plain"
                    )
                else:
                    st.error(error or "Could not retrieve transcript.")
            else:
                st.error("❌ Invalid YouTube URL. Please check and try again.")
    else:
        st.warning("⚠️ Please enter a YouTube URL")

# Add footer with instructions
st.markdown("---")
st.markdown("""
### 💡 How to use:
1. Copy a YouTube video URL
2. Select your preferred summary language
3. Click 'Generate Summary' button
4. Download your summary (optional)

**Tip:** Works best with videos that have captions/transcripts available!
""")
