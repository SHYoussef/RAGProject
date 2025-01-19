# RAGProject

the following repo is a RAG application.

Embedding model: sentence-transformers/all-MiniLM-L6-v2

Generation model: TinyLlama/TinyLlama-1.1B-Chat-v1.0

Feel free to test other models but simply changing the name of the hugging face repo on the code provided.

a requirements.txt file is also in the repo for the different librairies used and their versions.
Note: python 3.11.1 was used since the torch library is not yet supported in the latest python version (3.13) 

You can install the requirements using the following code 

pip install -r requirements.txt

Upon running the python file, several questions should appear on the terminal, asking for the device used ( -1 for cpu, 0 for the first gpu, 1 for the second gpu etc.), also
the models used run on cpus as well, though it might take longer than it would on gpu.

You will also be asked to provide a pdf name file, a taxes.pdf example is joined with the repo.

Lastly, you will be asked to provide a question, for example
