from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import AutoTokenizer
from langchain_chroma import Chroma
from langchain.schema import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFacePipeline
import PyPDF2
import re


device = int(input("choose device for the generation model, -1 for cpu, 0 for first gpu ... : "))
pdf_name = input("enter file name, format expected filename.pdf : ")

#Load tokenizer

tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2", trust_remote_code = True)

#function to count number of tokens, used below for chunking

def tiktoken_len(text):
    tokens = tokenizer.encode(text)
    return len(tokens)



def load_pdf_as_string(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
    return text

#Load the pdf as a string

data = load_pdf_as_string(pdf_name)


#Define a splitter for chunking

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20,
    length_function=tiktoken_len,
    separators=["\n\n", "\n", " ", ""]
)

#chunking of the document

documents = text_splitter.split_text(data)

#Load embedding model, for other models check hugging face website

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# convert each chunk to a document, since chroma expect such type

documents = [Document(page_content=chunk, metadata={}) for chunk in documents]

# Load documents in chromadb
db = Chroma.from_documents(documents, embedding_model)


# Instantiate the local model

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
    ),
    device = device

)

chat_model = ChatHuggingFace(llm=llm)



# Create the RetrievalQA chain (using your vector_store as before)
qa_chain = RetrievalQA.from_chain_type(
    llm=chat_model,
    chain_type="stuff",
    retriever=db.as_retriever(),
)

# Ask questions to the chain


while True:
    question = input("Question: ")
    response = qa_chain.invoke(question)
    match = re.search(r"<\|assistant\|>(.*)", response["result"], re.DOTALL)



    if match:
        result = match.group(1).strip()
        print("Answer:", result)
    else:
        print(response["result"])
    