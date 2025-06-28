# Irish Ads

A Streamlit application that generates Irish-style advertisements using OpenAI's language models through LangChain. The app takes product information as input and generates targeted advertising content along with an Ideal Customer Profile (ICP).

## Features

- Generate Irish-style advertisement content from product information
- Create Ideal Customer Profiles (ICP) for targeted marketing
- Simple and intuitive Streamlit interface
- Powered by OpenAI's GPT models via LangChain

## Prerequisites

- Python 3.10 or higher
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd matteo_irish
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```

## Usage

1. Run the Streamlit application:
```bash
streamlit run main.py
```

2. Open your browser and navigate to the URL shown in the terminal (typically `http://localhost:8501`)

3. In the application:
   - Paste your product information in the text area
   - Click "Submit"
   - The app will generate:
     - Irish-style advertisement content based on your product
     - An Ideal Customer Profile (ICP) in JSON format

## Project Structure

```
matteo_irish/
├── main.py              # Main Streamlit application
├── helpers/
│   ├── constants.py     # Configuration constants (API keys, etc.)
│   └── utils.py         # Utility functions for response generation
├── prompt.txt           # Prompt templates
├── format.json          # Format specifications
├── venv/                # Virtual environment (not tracked in git)
└── README.md            # This file
```

## Key Components

- **main.py**: The main application file that sets up the Streamlit interface and handles user interactions
- **helpers/constants.py**: Stores configuration constants including the OpenAI API key
- **helpers/utils.py**: Contains utility functions for generating responses and retrieving prompts
- **prompt.txt**: Contains the prompt templates used for generating ICP responses

## Dependencies

The main dependencies include:
- `streamlit`: For the web interface
- `langchain-openai`: For integrating with OpenAI's language models
- `python-dotenv`: For environment variable management

## Configuration

The application uses the following configuration:
- Temperature: 0.7 (for creative but coherent responses)
- Model: OpenAI's chat model via LangChain

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements.