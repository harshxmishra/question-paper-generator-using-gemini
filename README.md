# Question Paper Generator Using Gemini

Welcome to the **Question Paper Generator Using Gemini**! This project uses cutting-edge AI technology to create question papers based on user-defined parameters such as difficulty level, topic categories, and more. It's designed to assist educators in streamlining the process of preparing question papers tailored to specific requirements.

---

## Features

- **Upload PDF Content**: Extract text from uploaded PDF documents.
- **Smart Text Chunking**: Split large chunks of text into manageable sections using advanced text splitting techniques.
- **Customizable Parameters**: Define difficulty levels, topic categories, important topics, and maximum marks.
- **AI-Powered Generation**: Utilize Google's Gemini and FAISS for embedding and conversational AI to generate question papers.
- **Interactive UI**: A user-friendly Streamlit interface for seamless interaction.

---

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **AI Models**: Google Gemini (Generative AI) and GoogleGenerativeAIEmbeddings
- **Vector Database**: FAISS (Facebook AI Similarity Search)
- **Other Tools**: PyPDF2, LangChain, dotenv

---

## Installation

Follow these steps to set up the project locally:

### Prerequisites

- Python 3.8+
- Google API Key for Generative AI access

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/question-paper-generator-using-gemini.git
   cd question-paper-generator-using-gemini

    Set Up Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies:

pip install -r requirements.txt

Configure Environment Variables: Create a .env file in the project root with your Google API Key:

GOOGLE_API_KEY=your_google_api_key

Run the Application:

    streamlit run app.py

    Access the App: Open your browser and navigate to http://localhost:8501.

How to Use

    Upload PDF Documents:
        Use the sidebar to upload PDF files containing relevant content for generating the question paper.
        Click "Submit & Process" to extract and preprocess the content.

    Input Parameters:
        Provide the context or specific instructions for the question paper.
        Select difficulty level, enter topic categories, maximum marks, and important topics.

    Generate Question Paper:
        Click the "Generate Question Paper" button.
        View the AI-generated question paper directly in the app.

Example Use Case

    Upload PDFs: Upload documents containing course material or notes.
    Set Parameters: Choose "Medium" difficulty, topics like "Algebra, Calculus," maximum marks as 50, and important topics such as "Integration, Derivatives."
    Generate Output: Receive a customized, structured question paper covering all specified requirements.

Contributing

We welcome contributions! Follow these steps to contribute:

    Fork the repository.
    Create a new branch for your feature or bug fix:

git checkout -b feature-name

Commit your changes and push:

    git commit -m "Add your message here"
    git push origin feature-name

    Create a Pull Request.

License

This project is licensed under the MIT License.
Acknowledgments

    Google Generative AI for their powerful Gemini model.
    LangChain for simplifying AI chain creation.
    The open-source community for invaluable libraries and tools.

