from flask import Flask,Response, request, jsonify, copy_current_request_context

app = Flask(__name__)
__app_version = "1.0.0"
__app_base_url = "/v1/api"
__upload_folder = "data/"
__allowed_extension = set(['pdf','PDF'])

app.config['UPLOAD_FOLDER'] = __upload_folder
app.config['ALLOWED_EXTENSIONS'] = __allowed_extension
app.config['MAX_CONTENT_LENGTH'] = 10*1024*1024

@app.route(__app_base_url+'extract_pdf',methods=['GET','POST'])
def extract_pdf():
    try:
        print(__app_version)
        resp = jsonify({'status':'success'})
        resp.status_code = 200
    except Exception as e:
        resp = jsonify({'error':'Exception occured :'+e.message})
        resp.status_code = 200

    return resp
