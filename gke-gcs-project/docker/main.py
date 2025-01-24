from flask import Flask, request, redirect, url_for
from google.cloud import storage
import os

app = Flask(__name__)
BUCKET_NAME = "my-file-upload-bucket"

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        uploaded_file = request.files["file"]
        if uploaded_file:
            client = storage.Client()
            bucket = client.bucket(BUCKET_NAME)
            blob = bucket.blob(uploaded_file.filename)
            blob.upload_from_file(uploaded_file)
            return "File uploaded successfully!"
    return '''
    <!doctype html>
    <title>Upload File</title>
    <h1>Upload File to GCS</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)