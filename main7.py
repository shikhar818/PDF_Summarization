import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from PyPDF2 import PdfReader as Pdf

# Load tokenizer and model
quantization_config = BitsAndBytesConfig(llm_int8_has_fp16_weight = True)

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b-it")
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b-it", device_map = "cuda",quantization_config=quantization_config, low_cpu_mem_usage=True)

def summarize_text(text):
    context = text
    response = ""
    prompt = f"\nContext:\n{context}\n\nResponse:\n{response}"
    input_ids = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(**input_ids, max_length=2000)
    summary = tokenizer.decode(outputs[0], skip_special_tokens= True)
    return summary

def convert_pdf_to_text(file):
    pdf = Pdf(file)
    page = pdf.pages[input_page]
    text = page.extract_text()
    return text

def split_extract_text(text):
    split_length = 900
    part1 = text[:split_length]
    part2 = text[split_length:split_length * 2]
    return part1, part2
    

st.title("PDF Summarization App")

input_page = st.number_input("Enter page number:", format = "%d",step=1)
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    text = convert_pdf_to_text(uploaded_file)
    st.write("Original Text:")
    st.text_area("", text, height=300)

if st.button("Summarize"):
    part1, part2 = split_extract_text(text)
    summary_part1 = summarize_text(part1)
    summary_part2 = summarize_text(part2)
    st.write("Summary Part 1:")
    st.text_area("", summary_part1, height=150)
    st.write("Summary Part 2:")
    st.text_area("", summary_part2, height=150)