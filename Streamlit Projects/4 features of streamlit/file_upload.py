# 8. **File Uploader and File Info**:
#    ```python
#    st.markdown("### Upload a File")
#    uploaded_file = st.file_uploader("Choose a file")
#    if uploaded_file is not None:
#        st.markdown(f"File `{uploaded_file.name}` uploaded successfully!")
#    ```



# import streamlit as st 

# st.markdown("### Upload a File")
# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#     name = 'IMG_20230924_092620.jpg'
#     st.markdown(f"File `{uploaded_file.name}` uploaded successfully!")





import streamlit as st
from PIL import Image
import io
import fitz  # PyMuPDF library for handling PDFs

# Display a markdown section with a heading
st.markdown("### Upload a File")

# Create a list to store the names of uploaded files
uploaded_files_list = st.session_state.get('uploaded_files', [])

# Create a file uploader
uploaded_file = st.file_uploader("Choose a file to upload", type=["txt", "jpg", "png", "pdf"])

# Check if a file is uploaded
if uploaded_file is not None:
    # Get the name of the uploaded file
    uploaded_file_name = uploaded_file.name
    
    # Display the name of the uploaded file
    st.write(f"Uploaded File: {uploaded_file_name}")

    # Add the name of the uploaded file to the list
    uploaded_files_list.append(uploaded_file_name)
    
    # Save the updated list in the session state
    st.session_state.uploaded_files = uploaded_files_list

# Create a selectbox with the names of uploaded files
selected_file_name = st.selectbox("Choose a file", uploaded_files_list, index=len(uploaded_files_list)-1 if uploaded_files_list else 0)

# Display the selected file name
st.write(f"Selected File: {selected_file_name}")

# Additional code for opening/displaying the selected file
if selected_file_name:
    # Display content for text files
    if selected_file_name.endswith(".txt"):
        file_content = uploaded_file.getvalue().decode('utf-8') if uploaded_file else ""
        st.text_area("File Content", file_content)
    
    # Display image for image files
    elif selected_file_name.lower().endswith((".jpg", ".jpeg", ".png")):
        img = Image.open(uploaded_file)
        st.image(img, caption=f"Uploaded Image: {selected_file_name}", use_column_width=True)

    # Display text for PDF files
    elif selected_file_name.lower().endswith(".pdf"):
        pdf_bytes = uploaded_file.read()
        
        # Use PyMuPDF to extract text from PDF
        pdf_document = fitz.open("pdf", pdf_bytes)
        pdf_text = ""
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            pdf_text += page.get_text("text")
        
        # Display extracted text
        st.text_area("PDF Content", pdf_text)
    
    # Add more conditions for other file types as needed
    else:
        st.warning("Unsupported file type. Cannot display content.")
