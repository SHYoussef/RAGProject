# RAGProject

This repository contains a Retrieval-Augmented Generation (RAG) application.

### Models Used:
- **Embedding model**: `sentence-transformers/all-MiniLM-L6-v2`
- **Generation model**: `TinyLlama/TinyLlama-1.1B-Chat-v1.0`

Feel free to experiment with other models by simply changing the Hugging Face model repository name in the code.

### Installation:
A `requirements.txt` file is included in the repository, listing all necessary libraries and their respective versions.  
Note: Python 3.11.1 is recommended, as the latest version (3.13) is not fully supported by the `torch` library.

To install the dependencies, run:

`pip install -r requirements.txt`

### Usage:
Once the application is running, you will be prompted to:
1. Select the device (e.g., `-1` for CPU, `0` for the first GPU, `1` for the second GPU, etc.).
   - The models can run on CPUs, though processing may take longer compared to using a GPU.
   
2. Provide the name of a PDF file. An example file, `taxes.pdf`, is included in the repository.

3. Input a question. For example, if you ask:

`who pays taxes?`

The model will generate a response similar to:

`People who are self-employed, such as entrepreneurs or ride-share drivers, also have to pay income taxes, but those taxes aren't withheld from their earnings. Self-employed people have to pay those taxes on their own. If you are self-employed, make sure that you pay estimated taxes four times throughout the year to avoid a large, tax bill at the end of the year.`

### Additional Notes:
- This RAG application processes the provided PDF and retrieves relevant information to generate meaningful answers based on the document.
- Make sure to adjust the model names or configurations if testing with other models.
- You can build a docker image using the command: `docker build -t ragimage .`. Make sure the dockerfile is in the working directory.
