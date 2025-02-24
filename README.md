
# Document Converter and Chat Interface

This project provides a web-based interface for converting documents to Markdown format using various OCR engines. It uses Gradio for the interface and can integrate with OpenAI’s API for advanced document processing capabilities.

## Features

- **Document Upload & Conversion**  
  - Upload documents for conversion.
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
  - Interact with the converted document in a conversational manner.

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
markdown==3.7
```

Install them via:

```bash
pip install -r requirement.txt
```

### System-Level OCR Engine

For OCR features, you must have the system-level Tesseract engine installed.

- **Windows**:  
  - [Download the official installer](https://github.com/UB-Mannheim/tesseract/wiki) or use Chocolatey:  
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

After installation, verify by running:
```bash
tesseract --version
```
You should see a version like `tesseract 5.3.0 ...`.

---

## Environment Variables

OpenAI integration is optional but recommended for advanced document parsing. To enable it, create a `.env` file in the project root with your API key:

<details>
<summary><b>Example <code>.env</code> file</b></summary>

```ini
OPENAI_API_KEY=your_openai_api_key_here
```
</details>

> **Note**: Do not commit your real `.env` file to version control! Provide a `.env.example` instead.

---

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/ansemin/Doc2Md.git
cd Doc2Md
```

*(If your repo name is different, adjust accordingly.)*

### 2. Install Dependencies

Activate your virtual environment (if you use one):

```bash
pip install -r requirements.txt
```

This installs all Python packages specified in `requirements.txt`.

### 3. Run the Application

Depending on your file structure, if `main.py` is in `src/` or the project root, use one of the following commands:

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

After the server starts, open your browser and go to:
```
http://localhost:7860
```
You will see the Gradio interface. From there, you can:

1. Upload a PDF file.
2. Select a conversion method (e.g., “PyPdfium with OCR”).
3. Convert to view or download your chosen format.
4. Use the chat interface to interact with the document’s content.

---

## Example Walkthrough

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

Once the Gradio UI loads, you can:

1. Upload a PDF.
2. Select the desired conversion method.
3. Click the "Convert" button.
4. Download or copy your converted Markdown, JSON, Text, or Document Tags.
5. If OpenAI is configured, chat with the processed text.

---

## Docling Tesseract OCR Setup

To use Docling Tesseract OCR, you need to install `tesserocr`. Follow the steps below.

### Installing `tesserocr` Using a Wheel File

#### Step 1: Download the Correct Wheel File
1. Visit the releases page:  
   [SimonFlueckiger/tesserocr-windows_build](https://github.com/simonflueckiger/tesserocr-windows_build/releases)
2. Download the `.whl` file that matches:
   - Your Python version (for example, `cp312` for Python 3.12 or `cp311` for Python 3.11)
   - Your system architecture (for instance, `win_amd64` for 64-bit Windows)

   For example, for Python 3.12 (64-bit), you might download:
   ```
   tesserocr-2.7.1-cp312-cp312-win_amd64.whl
   ```

#### Step 2: Move the Wheel File to Your Virtual Environment
1. Open your file explorer and locate the downloaded `.whl` file.
2. Move the file into your virtual environment folder (for example, `.venv`):
   ```
   D:\Projects\.venv\
   ```

#### Step 3: Activate the Virtual Environment
1. Open Command Prompt.
2. Change to your project directory:
   ```sh
   cd D:\Projects
   ```
3. Activate the virtual environment:
   ```sh
   .venv\Scripts\activate
   ```
   The prompt will indicate that the environment is active.

#### Step 4: Install the Wheel File
Inside the virtual environment, run:
```sh
pip install .venv\tesserocr-2.7.1-cp312-cp312-win_amd64.whl
```
Replace the filename with your downloaded file if it differs.

#### Step 5: Verify Installation
Open a Python shell and run:
```python
import tesserocr
print(tesserocr.tesseract_version())
```
If a Tesseract version is printed, the installation succeeded.

---

## Manual Tesseract Installation and PATH Setup

If `tesserocr` cannot locate Tesseract, follow these steps:

### Step 1: Verify Tesseract Installation
Run the following command:
```sh
tesseract --version
```
If Tesseract is installed correctly, this command will display its version.

### Step 2: Find the Tesseract Installation Path
Run:
```sh
where tesseract
```
A typical output might be:
```
C:\Program Files\Tesseract-OCR\tesseract.exe
```
If no path is returned, Tesseract may not be installed or is not included in the system PATH.

### Step 3: Add Tesseract to the System PATH (Windows)
1. Open Environment Variables settings:
   - Press `Win + R`, type `sysdm.cpl`, and press Enter.
   - In the Advanced tab, click on Environment Variables.
2. Under System Variables, locate the variable named `Path` and select Edit.
3. Click New and add:
   ```
   C:\Program Files\Tesseract-OCR
   ```
4. Save the changes and close the settings.
5. Restart Command Prompt and run:
   ```sh
   tesseract --version
   ```
   The command should now display the Tesseract version.

### Step 4: Set the TESSDATA_PREFIX Environment Variable (if needed)
If `tesserocr` still cannot find Tesseract, set the `TESSDATA_PREFIX` variable by running:
```sh
setx TESSDATA_PREFIX "C:\Program Files\Tesseract-OCR\tessdata"
```
Restart Command Prompt and verify the variable with:
```sh
echo %TESSDATA_PREFIX%
```

---

## Contributing

1. Fork the repository and create a new branch for your changes.
2. Submit a Pull Request describing your modifications.

Bug reports, improvements, and feature requests are welcome.

### Additional Resources

- [Tesseract OCR Documentation](https://tesseract-ocr.github.io/)
- [OpenAI API Documentation](https://platform.openai.com/docs/introduction)
- [Gradio Documentation](https://gradio.app/docs/)

---

Enjoy converting and chatting with your documents! If you have any issues or questions, please open an Issue or Pull Request.
