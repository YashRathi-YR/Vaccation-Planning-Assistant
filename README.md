# **Vacation Planning Assistant** 🌍

### A Personalized Vacation Recommendation Tool Powered by LLaMA and Streamlit

---

## **Overview**
The Vacation Planning Assistant is an interactive web application designed to provide personalized vacation recommendations. Built with **Streamlit** and powered by **Meta’s LLaMA** model via Hugging Face's Transformers, the application generates tailored suggestions based on user inputs like vacation type, budget, duration, and travel preferences.

---

## **Features**
- **Customizable Inputs**: Choose from vacation types, budgets, durations, and travel preferences.
- **AI-Powered Recommendations**: Get detailed suggestions for destinations, activities, and travel tips.
- **Real-Time Interaction**: Adjust preferences and instantly receive recommendations.

---

## **Requirements**
### **Python Version**
- Python 3.8 or later

### **Libraries**
The following Python packages are required:
- `streamlit`
- `transformers`
- `torch`

To install the dependencies, use the following command:
```bash
pip install -r requirements.txt
```

### **System Requirements**
- A machine with sufficient memory (minimum 8GB RAM recommended).
- GPU acceleration is optional but recommended for faster model inference.

---

## **Installation Instructions**
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/vacation-planning-assistant.git
   cd vacation-planning-assistant
   ```

2. **Install Dependencies**
   Ensure you have Python and `pip` installed. Run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download Pre-trained LLaMA Model**
   The application uses the `meta-llama/Llama-3.2-1B` model. Download it via Hugging Face:
   ```python
   from transformers import AutoTokenizer, AutoModelForCausalLM
   tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B")
   model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-1B")
   ```

---

## **Running the Application**
1. **Start the Streamlit App**
   From the project directory, run:
   ```bash
   streamlit run app.py
   ```

2. **Open in Browser**
   Streamlit will display a URL (e.g., `http://localhost:8501/`). Open it in your browser to access the application.

---

## **How to Use**
1. Open the application in your browser.
2. Adjust the preferences in the **sidebar**:
   - **Type of Vacation**: Select from options like Beaches, Mountains, etc.
   - **Budget**: Low, Medium, or High.
   - **Duration**: Set the number of days using the slider.
   - **Travel Preferences**: Relaxation, Adventure, Family-friendly, etc.
   - **Additional Notes**: Add any specific requirements.
3. Click the **"Get Recommendations"** button.
4. View the AI-generated vacation suggestions on the main screen.

---

## **Project Structure**
```
vacation-planning-assistant/
│
├── app.py                # Main application file
├── requirements.txt      # Python dependencies
├── README.md             # Documentation
└── assets/               # (Optional) Folder for storing images or assets
```

---

## **Customization**
To modify the application:
1. **Change the Model**: Update the `model_name` in the `load_llm` function to use a different pre-trained model.
2. **Enhance Prompts**: Edit the prompt structure in the `prompt` variable for different outputs.
3. **Extend Features**: Add new input widgets or API integrations in `app.py`.

---

## **Future Plans**
- Add live destination data using APIs.
- Improve performance with quantized LLaMA models.
- Integrate visual recommendations like maps and itineraries.

---

## **Contributing**
Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Commit your changes: `git commit -m "Add a feature"`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

---

Happy traveling! ✈️
