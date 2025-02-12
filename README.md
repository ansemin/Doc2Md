# Document Converter and Chat Interface

This project provides a **web-based interface** for converting documents to Markdown format using various OCR engines. It utilizes **Gradio** for the user interface and can integrate with **OpenAI’s API** for enhanced document processing capabilities.

## Features

- **PDF Upload & Conversion**  
  - Upload PDF documents for conversion.
  - Choose between multiple conversion methods:
    - **PyPdfium** (with or without OCR)  
    - **Docling** (with various OCR options)  
    - **Marker** (with or without OCR)  

- **Multiple Export Formats**  
  - Markdown  
  - JSON  
  - Text  
  - Document Tags  

- **Chat Interface**  
  - Interact with the **converted** document in a conversational manner.

---

## Requirements

### Python Dependencies

To run this project, install the following Python packages (as listed in `requirements.txt`):

```text
docling==2.18.0
gradio==5.14.0
grpcio-status==1.70.0
marker-pdf==1.3.5
multiprocess==0.70.17
openai==1.61.1
pipdeptree==2.25.0
pytesseract==0.3.13
semchunk==2.2.2
tesseract==0.1.3
```

Install them via:

```bash
pip install -r requirements.txt
```

### System-Level OCR Engine

For OCR features, you must **also** have the system-level **Tesseract** engine installed.  

- **Windows**:  
  - [Download the official installer](https://github.com/UB-Mannheim/tesseract/wiki) **or** use Chocolatey:  
    ```powershell
    choco install tesseract
    ```
- **macOS**:  
  ```bash
  brew install tesseract
  ```
- **Linux (Debian/Ubuntu)**:  
  ```bash
  sudo apt-get update
  sudo apt-get install tesseract-ocr
  ```

Once installed, verify via:
```bash
tesseract --version
```
You should see a version like `tesseract 5.3.0 ...`.

---

## Environment Variables

In this project, **OpenAI** integration is optional but recommended for advanced document parsing. To enable it, create a `.env` file in the **root directory** of the project with your API key:

<details>
<summary><b>Example <code>.env</code> file</b></summary>

```ini
OPENAI_API_KEY=your_openai_api_key_here
```
</details>

> **Note**: Do **not** commit your real `.env` file to version control! Provide a `.env.example` instead.

---

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/ansemin/Doc2Md.git
cd Doc2Md
```

*(If your repo name is different, adjust accordingly.)*

### 2. Install Dependencies

Make sure you’re in your virtual environment (if you’re using one):

```bash
pip install -r requirements.txt
```

This installs all Python packages specified in `requirements.txt`.

### 3. Run the Application

Depending on your file structure, if `main.py` is in `src/` or the project root, do one of the following:

```bash
# If main.py is at the project root:
python main.py
```
**or**
```bash
# If main.py is inside a 'src' folder:
python src/main.py
```

### 4. Access the Web UI

Once the server starts, open your browser and go to:
```
http://localhost:7860
```
You should see the Gradio interface. From there, you can:

1. **Upload** a PDF file.  
2. **Select** a conversion method (e.g., “PyPdfium with OCR”).  
3. **Convert** to view or download your chosen format.  
4. **Use the chat interface** to interact with the document’s content.

---

## Example Walkthrough

Below is a quick demonstration of the typical workflow:

```bash
# Step 1: Clone the repo (example path)
git clone https://github.com/ansemin/Doc2Md.git
cd Doc2Md

# Step 2: (Optional) Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or:
.\.venv\Scripts\activate  # Windows

# Step 3: Install Python packages
pip install -r requirements.txt

# Step 4: (Optional) Set up your .env for OpenAI:
cp .env.example .env
# Then edit .env to add your API key

# Step 5: Run the app
python main.py  # or python src/main.py, depending on your structure

# Open http://localhost:7860 in your browser
```

You will be greeted by the Gradio UI. From there:

1. **Upload a PDF**.  
2. **Select** your desired conversion method.  
3. **Click** the “Convert” button.  
4. **Download** or copy your converted Markdown, JSON, Text, or Document Tags.  
5. If you have OpenAI configured, you can **chat** with the processed text.

---

## Contributing

1. **Fork** the repository and create a new branch for your features or bug fixes.  
2. Submit a **Pull Request** explaining your changes.  

We welcome improvements, bug reports, and feature requests!


### Additional Resources

- [Tesseract OCR Documentation](https://tesseract-ocr.github.io/)  
- [OpenAI API Documentation](https://platform.openai.com/docs/introduction)  
- [Gradio Documentation](https://gradio.app/docs/)  

---

**Enjoy converting and chatting with your documents!** If you have any issues or questions, please open an Issue or Pull Request.
