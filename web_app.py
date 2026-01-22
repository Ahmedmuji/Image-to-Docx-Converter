import streamlit as st

# Must be the first Streamlit command
st.set_page_config(page_title="Image to Docx converter", layout="centered")

import os
import tempfile
from docx import Document
from smart_converter import process_single_image_to_doc
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO)

st.title("Smart GenAI OCR Converter")
st.write("Upload an image of your notes. The AI will transcribe text and **re-generate diagrams** as digital plots!")

uploaded_file = st.file_uploader("Choose an image (JPG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the image
    st.image(uploaded_file, caption='Uploaded Image', width="stretch")
    
    if st.button("Convert to Word"):
        with st.spinner("Processing... This may take a minute (Gemini API + Code Generation)..."):
            try:
                # Save uploaded file to temp
                suffix = os.path.splitext(uploaded_file.name)[1]
                if not suffix: suffix = ".jpg"
                
                with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_path = tmp_file.name
                
                # Process
                doc = Document()
                # Create a title in doc
                doc.add_heading(f"Source: {uploaded_file.name}", level=0)
                
                success = process_single_image_to_doc(tmp_path, doc)
                
                # Cleanup temp input
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)
                
                if success:
                    # Save doc to a temp file for download
                    out_tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
                    out_path = out_tmp.name
                    out_tmp.close() # Close so docx can write to it
                    
                    doc.save(out_path)
                    
                    st.success("Conversion Complete!")
                    
                    # Read back for download button
                    with open(out_path, "rb") as f:
                        docx_data = f.read()
                        
                    st.download_button(
                        label="Download Word Document",
                        data=docx_data,
                        file_name=f"Converted_{os.path.splitext(uploaded_file.name)[0]}.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
                    
                    # Cleanup output temp (optional, OS cleans up eventually for tempfile but named ones persist)
                    # We leave it for now or delete after a delay? Streamlit re-runs scripts so immediate delete breaks download?
                    # Streamlit download button handles data in memory so file on disk is not strictly needed after reading.
                    os.remove(out_path)
                    
                else:
                    st.error(" Conversion Failed. Check backend logs.")
            
            except Exception as e:
                st.error(f"An error occurred: {e}")
                logging.error(e, exc_info=True)
