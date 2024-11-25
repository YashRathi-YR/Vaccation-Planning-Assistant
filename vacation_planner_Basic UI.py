import streamlit as st

# Function to create the UI for input
def create_vacation_planning_ui():
    st.title("Vacation Planning Assistant")

    st.header("Tell us about your vacation preferences")

    # 1. Preferred Destinations or Types of Vacation
    vacation_type = st.selectbox(
        "What type of vacation are you interested in?",
        ["Beaches", "Mountains", "Cultural", "Adventure", "Relaxation", "Family-friendly"]
    )

    # 2. Budget Constraints
    budget = st.slider(
        "Select your budget (in USD)",
        min_value=500,
        max_value=10000,
        step=100,
        value=2000
    )

    # 3. Number of Days Available
    days_available = st.number_input(
        "How many days are you planning to spend on vacation?",
        min_value=1,
        max_value=30,
        step=1,
        value=7
    )

    # 4. Travel Preferences
    travel_pref = st.radio(
        "What kind of experience are you looking for?",
        ["Adventure", "Relaxation", "Cultural Immersion", "Family-friendly"]
    )

    # Button to Generate Recommendations
    if st.button("Get Vacation Recommendations"):
        # Displaying user inputs after clicking the button
        st.write("### Your Input:")
        st.write(f"Vacation Type: {vacation_type}")
        st.write(f"Budget: ${budget}")
        st.write(f"Number of Days: {days_available}")
        st.write(f"Travel Preference: {travel_pref}")

        # Placeholder for actual functionality
        st.write("### Generating vacation recommendations...")

        # Example of what we could display once the functionality is implemented
        st.write("Recommended Destination: Bali (example)")
        st.write("Estimated cost: $3000")
        st.write("Activities: Beach activities, cultural tours, relaxation spots")
        st.write("Best Travel Time: March to October")

# Call the function to display the UI
create_vacation_planning_ui()
