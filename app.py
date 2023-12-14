import os
from flask import Flask, request, jsonify
import requests
from PIL import Image
import pytesseract
import io

app = Flask(__name__)


@app.route('/extract_text', methods=['POST'])
def extract_text():
    try:
        file_url = request.json.get('file_url')
        if not file_url:
            return jsonify({'error': 'File URL not provided'})

        for _ in range(3):
            response = requests.get(file_url)
            try:
                response.raise_for_status()
                break
            except requests.exceptions.HTTPError as errh:
                return jsonify({'error': f'HTTP Error: {errh}'})
            except requests.exceptions.RequestException as err:
                return jsonify({'error': f'Request Exception: {err}'})

        image_bytes = response.content
        try:
            image = Image.open(io.BytesIO(image_bytes))
            file_extension = file_url.split('.')[-1]
            file_path = f'image.{file_extension}'
            with open(file_path, 'wb') as f:
                f.write(response.content)
        except Exception as e:
            return jsonify({'error': f'Failed to open image: {str(e)}'})

        try:
            text = pytesseract.image_to_string(image, lang='eng')
            print(text)
            os.remove(file_path)

            # Extract name and DOB using simple string manipulation or regular expressions
            name_start = text.find('Name:') + len('Name:')
            name_end = text.find('DOB:')
            name = text[name_start:name_end].strip()

            dob_start = text.find('DOB:') + len('DOB:')
            dob_end = text.find('Gender:')
            dob = text[dob_start:dob_end].strip()

            return jsonify({'message': 'Text extraction successful', 'name': name, 'dob': dob, 'language': 'eng'})
        except Exception as e:
            return jsonify({'error': f'Failed to extract text using OCR: {str(e)}'})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=60001)
