import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

# Initialize LLM
@st.cache_resource
def load_llm():
    model_name = "meta-llama/Llama-3.2-1B"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return pipeline("text-generation", model=model, tokenizer=tokenizer)

llm_pipeline = load_llm()

# Streamlit UI
st.title("Vacation Planning Assistant 🌍")
st.sidebar.header("User Preferences")

# Collect user inputs
vacation_type = st.sidebar.selectbox("Type of Vacation", ["Beaches", "Mountains", "Cultural", "Adventure", "City", "Wildlife"])
budget = st.sidebar.selectbox("Budget", ["Low", "Medium", "High"])
days = st.sidebar.slider("Number of Days", 1, 30, 7)
travel_preference = st.sidebar.radio("Travel Preference", ["Relaxation", "Adventure", "Family-friendly", "Romantic", "Solo"])
user_notes = st.sidebar.text_area("Any Additional Preferences?", "")

if st.sidebar.button("Get Recommendations"):
    # Construct the prompt for the LLM
    prompt = (
        f"Provide personalized vacation recommendations based on the following preferences:\n\n"
        f"- Type of Vacation: {vacation_type}\n"
        f"- Budget: {budget}\n"
        f"- Duration: {days} days\n"
        f"- Travel Preference: {travel_preference}\n"
    )
    if user_notes:
        prompt += f"- Additional Preferences: {user_notes}\n"
    prompt += (
        "Include details such as the best destinations, estimated costs, popular activities, and ideal travel times. "
        "Structure the output as a list of recommendations."
    )

    # Generate response from LLM
    with st.spinner("Generating vacation recommendations..."):
        llm_response = llm_pipeline(prompt, max_length=2000, num_return_sequences=1)[0]["generated_text"]

    # Display recommendations
    st.subheader("Recommended Destinations and Tips")
    st.write(llm_response)
