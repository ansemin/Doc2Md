import gradio as gr
from converter import convert_file
from docling_chat import chat_with_document

def main():
    with gr.Blocks() as demo:
        gr.Markdown("Converter (Docling & Marker) with optional full OCR")

        with gr.Tab("Upload and Convert"):
            file_input = gr.File(label="Upload PDF", type="filepath")

            pipeline_choice = gr.Dropdown(
                label="Conversion Method",
                choices=[
                    "PyPdfium no OCR",
                    "PyPdfium EasyOCR",
                    "Docling parse no OCR",
                    "Docling parse EasyOCR",
                    "Docling parse EasyOCR (CPU only)",
                    "Docling parse Tesseract",
                    "Docling parse Tesseract CLI",
                    "Docling parse ocrmac",
                    "Docling parse full force OCR",
                    "Marker parse no OCR",
                    "Marker parse Force OCR"
                ],
                value="PyPdfium no OCR"
            )

            output_format = gr.Radio(
                label="Output Format",
                choices=["Markdown", "JSON", "Text", "Document Tags"],
                value="Markdown"
            )

            file_display = gr.Markdown(label="Converted Markdown")
            file_download = gr.File(label="Download File")

            convert_button = gr.Button("Convert")

            convert_button.click(
                fn=convert_file,
                inputs=[file_input, pipeline_choice, output_format],
                outputs=[file_display, file_download]
            )

        with gr.Tab("Chat with Document"):
            document_text_state = gr.State("")
            chatbot = gr.Chatbot(label="Chat", type="messages")
            text_input = gr.Textbox(placeholder="Type here...")
            clear_btn = gr.Button("Clear")

            file_display.change(lambda text: text, inputs=file_display, outputs=document_text_state)

            text_input.submit(
                fn=chat_with_document,
                inputs=[text_input, chatbot, document_text_state],
                outputs=[chatbot, chatbot]
            )
            clear_btn.click(lambda: ([], []), None, [chatbot, chatbot])

    demo.launch(server_name="localhost", server_port=7860, share=True)

if __name__ == "__main__":
    main()
