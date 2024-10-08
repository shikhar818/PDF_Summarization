<h1>📄 PDF Summarization Project</h1>

<h2>📝 Project Overview</h2>
<p>
  This project is designed to <strong>summarize the content of any PDF document</strong>, automatically extracting meaningful summaries using advanced language models and PDF processing libraries. It simplifies document comprehension by providing concise overviews of each page.
</p>

<h2>🛠️ Libraries Used</h2>
<ul>
  <li><strong>Py2PDF</strong></a>: Extracts and preprocesses content from the PDF.</li>
  <li><strong>Gemma</strong></a>: A Language Learning Model (LLM) that summarizes the extracted text efficiently.</li>
  <li><strong>Streamlit</strong></a>: Used for deploying the application, providing a user-friendly interface.</li>
</ul>

<hr>

<h2>🔄 Workflow</h2>

<h3>1. PDF Upload</h3>
<p>Users can upload <strong>any PDF file</strong> through the <strong>Streamlit</strong> interface.</p>

<h3>2. Text Extraction</h3>
<p><strong>Py2PDF</strong> extracts the text, parsing through sections, headings, and paragraphs, and prepares the content for summarization.</p>

<h3>3. Summarization</h3>
<p><strong>Gemma</strong> processes the extracted content, identifying key sections and important details, and generates <strong>summaries</strong> for each part or the entire document.</p>

<h3>4. Results Display</h3>
<p>The summarized content is presented in a clean, <strong>easy-to-read format</strong> on the <strong>Streamlit app</strong>, allowing users to quickly grasp the document's essence.</p>
<p>Note: It requires a high computational resource (GPU) in order to get it running smoothly on your local machine ! </p>


<h2>🎯 Features</h2>
<ul>
  <li><strong>Automated Summarization</strong>: Quickly generates summaries from any PDF file.</li>
  <li><strong>Interactive Interface</strong>: Simple PDF upload and display using Streamlit.</li>
  <li><strong>Accurate Summaries</strong>: Powered by the <strong>Gemma</strong> LLM to extract key information.</li>
</ul>

<h2>Screenshots</h2>

![Screenshot 2024-09-06 205354](https://github.com/user-attachments/assets/d508c5bb-a998-433a-a632-a5a5d1041609)

![3](https://github.com/user-attachments/assets/f7038029-4615-4152-85e7-7eb686fa9619)


![4](https://github.com/user-attachments/assets/0acf311d-113d-446c-9187-8c25af38ddb3)



<h4>Input:</h4>

![image](https://github.com/user-attachments/assets/9374ec0d-d79b-456b-bb1d-627a296e422c)

<h4>Output:</h4>

![image](https://github.com/user-attachments/assets/dc046346-c15c-4b35-a2ee-58f9fc6320bd)
