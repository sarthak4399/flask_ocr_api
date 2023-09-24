# from flask import Flask, request, jsonify
# from PIL import Image
# import pytesseract
# from flask import render_template
# import fitz  # PyMuPDF

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('upload.html')


# @app.route('/extract_text', methods=['POST'])
# def extract_text():
#     try:
#         if 'file' not in request.files:
#             return jsonify({'error': 'No file part'})

#         file = request.files['file']

#         if file.filename == '':
#             return jsonify({'error': 'No selected file'})

#         allowed_extensions = {'jpg', 'jpeg', 'png', 'pdf'}
#         if '.' not in file.filename or file.filename.split('.')[-1].lower() not in allowed_extensions:
#             return jsonify({'error': 'Invalid file extension'})

#         if file.filename.lower().endswith('.pdf'):
#             pdf_document = fitz.open(stream=file.read(), filetype='pdf')
#             text = ""

#             for page_number in range(len(pdf_document)):
#                 page = pdf_document[page_number]
#                 pix = page.get_pixmap()
#                 img = Image.frombytes(
#                     "RGB", [pix.width, pix.height], pix.samples)
#                 page_text = pytesseract.image_to_string(img, lang='hin')
#                 text += page_text

#         else:
#             image = Image.open(file)
#             text = pytesseract.image_to_string(image)

#         text_utf8 = text.encode('utf-8').decode('utf-8')

#         return jsonify({'message': 'Text extraction successful', 'text': text_utf8})

#     except Exception as e:
#         return jsonify({'error': str(e)})


# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, request, jsonify
# import fitz
# import requests
# import io

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return jsonify({'message': 'Welcome to the Text Extraction API'})


# @app.route('/extract_text', methods=['POST'])
# def extract_text():
#     try:
#         # Get the Google Drive file ID from the request
#         file_id = request.form.get('file_id')

#         if not file_id:

#             return jsonify({'error': 'File ID not provided'})

#         # Construct the Google Drive file URL
#         file_url = f'https://drive.google.com/uc?id={file_id}'

#         # Send a GET request to the URL to fetch the PDF file
#         response = requests.get(file_url)

#         # Check if the request was successful (status code 200)
#         if response.status_code != 200:
#             return jsonify({'error': 'Failed to fetch PDF file from URL'})

#         # Read the PDF content as bytes
#         pdf_bytes = response.content

#         # Initialize PyMuPDF (fitz) to work with PDF
#         pdf_document = fitz.open(stream=pdf_bytes, filetype='pdf')
#         text = " "

#         for page_number in range(len(pdf_document)):
#             page = pdf_document[page_number]
#             text += page.get_text()

#         text_utf8 = text.encode('utf-8').decode('utf-8')

#         return jsonify({'message': 'Text extraction successful', 'text': text_utf8, 'language': 'hi'})

#     except Exception as e:
#         return jsonify({'error': str(e)})


# if __name__ == '__main__':
#     app.run(debug=True)
#     extract_text()
# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, request, jsonify
# import fitz
# import requests
# import io

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return jsonify({'message': 'Welcome to the Text Extraction API'})


# @app.route('/extract_text', methods=['POST'])
# def extract_text():
#     try:
#         # Get the Google Drive file ID from the request
#         file_id = request.form.get('file_id')

#         if not file_id:

#             return jsonify({'error': 'File ID not provided'})

#         # Construct the Google Drive file URL
#         file_url = f'https://drive.google.com/uc?id={file_id}'

#         # Send a GET request to the URL to fetch the PDF file
#         response = requests.get(file_url)

#         # Check if the request was successful (status code 200)
#         if response.status_code != 200:
#             return jsonify({'error': 'Failed to fetch PDF file from URL'})

#         # Read the PDF content as bytes
#         pdf_bytes = response.content

#         # Initialize PyMuPDF (fitz) to work with PDF
#         pdf_document = fitz.open(stream=pdf_bytes, filetype='pdf')
#         text = " "

#         for page_number in range(len(pdf_document)):
#             page = pdf_document[page_number]
#             text += page.get_text()

#         text_utf8 = text.encode('utf-8').decode('utf-8')

#         return jsonify({'message': 'Text extraction successful', 'text': text_utf8, 'language': 'hi'})

#     except Exception as e:
#         return jsonify({'error': str(e)})


# if __name__ == '__main__':
#     app.run(debug=True)
#     extract_text()
# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, request, jsonify
# import fitz
# import requests
# import io

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return jsonify({'message': 'Welcome to the Text Extraction API'})


# @app.route('/extract_text', methods=['POST'])
# def extract_text():
#     try:
#         # Get the Google Drive file ID from the request
#         file_id = request.form.get('file_id')

#         if not file_id:

#             return jsonify({'error': 'File ID not provided'})

#         # Construct the Google Drive file URL
#         file_url = f'https://drive.google.com/uc?id={file_id}'

#         # Send a GET request to the URL to fetch the PDF file
#         response = requests.get(file_url)

#         # Check if the request was successful (status code 200)
#         if response.status_code != 200:
#             return jsonify({'error': 'Failed to fetch PDF file from URL'})

#         # Read the PDF content as bytes
#         pdf_bytes = response.content

#         # Initialize PyMuPDF (fitz) to work with PDF
#         pdf_document = fitz.open(stream=pdf_bytes, filetype='pdf')
#         text = " "

#         for page_number in range(len(pdf_document)):
#             page = pdf_document[page_number]
#             text += page.get_text()

#         text_utf8 = text.encode('utf-8').decode('utf-8')

#         return jsonify({'message': 'Text extraction successful', 'text': text_utf8, 'language': 'hi'})

#     except Exception as e:
#         return jsonify({'error': str(e)})


# if __name__ == '__main__':
#     app.run(debug=True)
#     extract_text()
# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify
import fitz
import requests
import io

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Text Extraction API'})


@app.route('/extract_text', methods=['POST'])
def extract_text():
    try:
        # Get the Google Drive file ID from the request
        file_id = request.form.get('file_id')

        if not file_id:

            return jsonify({'error': 'File ID not provided'})

        # Construct the Google Drive file URL
        file_url = f'https://drive.google.com/uc?id={file_id}'

        # Send a GET request to the URL to fetch the PDF file
        response = requests.get(file_url)

        # Check if the request was successful (status code 200)
        if response.status_code != 200:
            return jsonify({'error': 'Failed to fetch PDF file from URL'})

        # Read the PDF content as bytes
        pdf_bytes = response.content

        # Initialize PyMuPDF (fitz) to work with PDF
        pdf_document = fitz.open(stream=pdf_bytes, filetype='pdf')
        text = " "

        for page_number in range(len(pdf_document)):
            page = pdf_document[page_number]
            text += page.get_text()

        text_utf8 = text.encode('utf-8').decode('utf-8')

        return jsonify({'message': 'Text extraction successful', 'text': text_utf8, 'language': 'mr'})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
    extract_text()
