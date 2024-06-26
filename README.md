# TubeGenie - YouTube Video Interaction

## Project Overview
TubeGenie is a Streamlit application that allows users to interact with YouTube videos using OpenAI's powerful language models. By leveraging advanced AI capabilities, the app can provide insightful answers to user queries based on the content of the specified YouTube video.

## Project Description

### Objectives
- To enable users to chat with YouTube videos by asking questions and receiving intelligent responses.
- To seamlessly integrate YouTube video content analysis with natural language processing.

### Features
1. **Video Content Analysis:** Extracts key information from YouTube videos to provide accurate responses.
2. **Interactive Q&A:** Users can ask questions about the video content and receive detailed answers.
3. **Easy Cleanup:** Simple interface to manage and release resources used by the application.

## Data Sources
- **YouTube Video Data:** Extracted using the YouTube video URL provided by the user.
- **OpenAI API:** Utilizes OpenAI's GPT-4-turbo model to process and generate responses.

## Methodology

1. **Data Collection:**
   - Users input the YouTube video URL.
   - The application extracts the video ID and fetches the video content.

2. **Data Preparation:**
   - The video content is processed and stored in a temporary database for quick access.
   - Ensures that the content is ready for querying by the language model.

3. **Query Processing:**
   - Users ask questions related to the video content.
   - The application uses OpenAI's language model to generate responses based on the video content.

## Technologies Used

### Embedchain
- **Description:** Embedchain is a framework that allows seamless integration of data sources with AI models. It handles data ingestion, embedding, and querying, making it easier to build applications that require natural language understanding.
- **Usage in TubeGenie:** Embedchain is used to process and manage the video content data. It helps in embedding the video content into a format that can be efficiently queried by the OpenAI language model.

### ChromaDB
- **Description:** ChromaDB is a highly efficient, disk-backed, and memory-mapped database designed for handling large-scale data storage and retrieval.
- **Usage in TubeGenie:** ChromaDB is used as the underlying storage mechanism for the embedded video content. It ensures fast and reliable access to the data during query processing.

### VectorDB
- **Description:** VectorDB is a specialized database designed for storing and querying vector representations of data. It is optimized for handling operations like nearest neighbor search, which are common in machine learning applications.
- **Usage in TubeGenie:** VectorDB is used to store the vector embeddings of the video content. This enables efficient similarity search and retrieval, which is essential for generating accurate responses to user queries.

## Results
- **Accurate Responses:** Provides detailed and contextually accurate answers to user queries.
- **Efficient Resource Management:** The app ensures resources are managed and released effectively after use.
![alt text](<Images/Image1.jpg>)
![alt text](<Images/Image2.jpg>)

## Tools and Technologies
- **Programming Languages:** Python
- **Libraries:** Streamlit, embedchain, re, tempfile, shutil
- **APIs:** OpenAI API for language processing

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/tubegenie.git
   cd tubegenie
   ```

2. **Install required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up OpenAI API:**
   - Sign up on [OpenAI](https://www.openai.com/) to get your API key.
   - Replace the placeholder in the code with your actual API key.

## Running the Project

1. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **Interact with the App:**
   - Enter your OpenAI API key.
   - Provide the YouTube video URL.
   - Ask questions about the video and get responses.
   - Use the "Clean Up Resources" button to release resources when done.

## Future Work
- Integrate support for multiple video platforms.
- Enhance the accuracy and contextual understanding of the AI model.
- Add real-time processing capabilities for live videos.

## References
- [OpenAI API](https://www.openai.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [ChromaDB Documentation](https://chroma.readthedocs.io/)
- [Embedchain Documentation](https://embedchain.readthedocs.io/)
- [VectorDB Documentation](https://vectordb.readthedocs.io/)

## Contributors
- Siddharth Singh
- sms10221@nyu.edu
