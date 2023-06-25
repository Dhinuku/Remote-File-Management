import os
import shutil
import pathlib
import json
import sys
import zlib
import io
import random
from flask import Flask, render_template, request, redirect, make_response, send_file
from werkzeug.utils import secure_filename


def folder(path,filename):
    if filename!='':
        filename+='/'
        path=path+r'\\'+filename
    var='['
    for i in os.listdir(path):
        if os.path.isfile(path + r'\\' + i):
            var +='{"name":"'+i+'","size":'+str(os.path.getsize(path + r'\\' + i))+',"type":"'+pathlib.Path(path + r'\\' + i).suffix+'","path":"'+filename+i+'"},'
        else:
            var +='{"name":"'+i+'","size":'+str(os.path.getsize(path + r'\\' + i))+',"type":"folder","path":"'+filename+i+'"},'
    var+='{"name":"no"}]'
    return var


if os.path.exists('user_details.txt') and os.path.exists('MainDirectory.txt') and os.path.exists('main_path.txt'):
    print("CriticalFileCheck")
else:
    input("MissingFiles")
    sys.exit()
f = open('user_details.txt')
user_details = json.load(f)
f.close()
f = open('main_path.txt', 'r')
main_path = r'' + f.read()
f.close()
if os.path.exists(main_path):
    print("StorageDirectoryExists")
else:
    input("StorageDirectoryMissing")
    sys.exit()
Sessions = []
Session_Tokens=[]
f = open('MainDirectory.txt', 'r')
template_dir = r'' + f.read()
print(f"MainDirectory={template_dir}")
template_dir = os.path.join(template_dir, 'templates')
print(f"TemplateDirectory={template_dir}")
f = open('MainDirectory.txt', 'r')
static_dir = r'' + f.read()
static_dir = os.path.join(static_dir, 'assets')
print(f"StaticDirectory={static_dir}")

app = Flask(__name__, template_folder=template_dir,static_folder=static_dir)

user = "Admin"
password = "Password"


@app.route('/', methods=["GET"])
def home():
    get_user = request.cookies.get('user')
    get_token = request.cookies.get('token')
    if get_user in Sessions and get_token in Session_Tokens:
        return redirect('/dashboard')
    else:
        return redirect('/index')


@app.route('/index', methods=["GET"])
def index():
        return render_template('index.html')

@app.route('/about', methods=["GET"])
def about():
        return render_template('about.html')


@app.route('/services', methods=["GET"])
def services():
        return render_template('services.html')

@app.route('/login', methods=['GET'])
def login0():
    get_user = request.cookies.get('user')
    get_token = request.cookies.get('token')
    if get_user in Sessions and get_token in Session_Tokens:
        return redirect('/dashboard')
    else:
        return render_template('login.html')


@app.route('/login', methods=['POST'])
def login1():
    usr = request.form['uname']
    psw = request.form['psw']
    log = {'user': usr, 'password': psw}
    if log in user_details:
        global Sessions
        Sessions.append(usr)
        token=str(random.randint(100000, 999999))
        Session_Tokens.append(token)
        resp = make_response(redirect('/dashboard'))
        resp.set_cookie('user', usr)
        resp.set_cookie('token', token)
        return resp
    else:
        return "Incorrect User Name or password Try Again"


@app.route('/signup', methods=['GET'])
def signup0():
    return render_template('sin.html')


@app.route('/signup', methods=['POST'])
def signup1():
    usr = request.form['uname']
    psw = request.form['psw']
    if usr=="" or psw=="":
        return "All fields must be filled";
    global user_details
    for d in user_details:
        if d["user"] == usr:
            return "User exists try another name"
    user_details.append({"user": usr, "password": psw})
    f = open('user_details.txt', 'w')
    json.dump(user_details, f)
    f.close()
    os.mkdir(path=main_path + r'/' + usr)
    return redirect('/login')


@app.route('/filedat/<path:filename>')
def filedata(filename):
    get_user = request.cookies.get('user')
    get_token = request.cookies.get('token')
    if get_user in Sessions and get_token in Session_Tokens:
        path = main_path + r'\\' + get_user
        var = folder(path, filename)
        return var
    else:
        return "ERROR"


@app.route('/filedata')
def filedat():
    get_user = request.cookies.get('user')
    get_token = request.cookies.get('token')
    if get_user in Sessions and get_token in Session_Tokens:
        path = main_path + r'\\' + get_user
        var = folder(path, '')
        return var
    else:
        return "ERROR"


@app.route('/dashboard')
def dashboard():
    get_user = request.cookies.get('user')
    get_token = request.cookies.get('token')
    if get_user in Sessions and get_token in Session_Tokens:
        return render_template('/dashboard.html',user=get_user.upper())
    else:
        return redirect('/login')


@app.route('/upload', methods=['GET'])
def upload0():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload1():
    get_user = request.cookies.get('user')
    get_token = request.cookies.get('token')
    if get_user in Sessions and get_token in Session_Tokens:
        path = main_path + r'\\' + get_user + r'\\'
        f = request.files.getlist('folder')
        for file in f:
            vari = file.filename
            vari = vari.replace('/', '\\')
            makit = vari.split('\\')
            if not os.path.exists(path + makit[0]):
                os.mkdir(path + makit[0])
            varit = vari.rsplit('\\', 1)
            varity = varit[len(varit) - 2]
            if os.path.exists(path + varity):
                filer = open(os.path.join(path,vari),"wb")
                filer.write(zlib.compress(file.read()))
                filer.close()
            else:
                os.makedirs(path + varity)
                filer = open(os.path.join(path,vari),"wb")
                filer.write(zlib.compress(file.read()))
                filer.close()
        return redirect('/dashboard')
    else:
        return 'ERROR'


@app.route('/uploadfile', methods=['GET'])
def upload2():
    return render_template('uploadfile.html')


@app.route('/uploadfile', methods=['POST'])
def upload3():
    get_user = request.cookies.get('user')
    get_token = request.cookies.get('token')
    if get_user in Sessions and get_token in Session_Tokens:
        path = main_path + r'\\' + get_user
        f = request.files['file']
        if get_folder_size(main_path + r'\\' + get_user)>5000000 or (5000000-get_folder_size(main_path + r'\\' + get_user))<int(request.headers['Content-Length']):
            return redirect('/dashboard')
        file=open(os.path.join(path, secure_filename(f.filename)),"wb")
        file.write(zlib.compress(f.read(),level=9))
        file.close()
        return redirect('/dashboard')
    else:
        return 'ERROR'


@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    get_user = request.cookies.get('user')
    get_token = request.cookies.get('token')
    if get_user in Sessions and get_token in Session_Tokens:
        path = main_path + r'\\' + get_user + r'\\' + filename
        varit = filename.rsplit('\\', 1)
        varity = varit[len(varit) - 1]
        f=open(path,"rb")
        ff=io.BytesIO(zlib.decompress(f.read()))
        return send_file(ff, as_attachment=True,download_name=varity)
    else:
        return "ERROR"


@app.route('/signout', methods=['GET'])
def signout():
    get_user = request.cookies.get('user')
    get_token = request.cookies.get('token')
    if get_user in Sessions and get_token in Session_Tokens:
        Sessions.remove(get_user)
        Session_Tokens.remove(get_token)
        resp = make_response(redirect('/login'))
        resp.set_cookie('user', '', expires=0)
        resp.set_cookie('token', '', expires=0)
        return resp
    else:
        return redirect('/login')


@app.route('/delete/<path:filename>', methods=['GET', 'POST'])
def delete(filename):
    get_user = request.cookies.get('user')
    get_token = request.cookies.get('token')
    if get_user in Sessions and get_token in Session_Tokens:
        path = main_path + r'\\' + get_user + r'\\' + filename
        os.remove(path)
        return redirect('/dashboard')
    else:
        return "ERROR"


@app.route('/deletefolder/<path:filename>', methods=['GET', 'POST'])
def deletefolder(filename):
    get_user = request.cookies.get('user')
    get_token = request.cookies.get('token')
    if get_user in Sessions and get_token in Session_Tokens:
        path = main_path + r'\\' + get_user + r'\\' + filename
        shutil.rmtree(path)
        return redirect('/dashboard')
    else:
        return "ERROR"


@app.route('/compress/<path:filename>', methods=['GET', 'POST'])
def compress(filename):
    get_user = request.cookies.get('user')
    get_token = request.cookies.get('token')
    if get_user in Sessions and get_token in Session_Tokens:
        path = main_path + r'\\' + get_user + r'\\' + filename
        shutil.make_archive(path, 'zip', path)
        return redirect('/dashboard')
    else:
        return "ERROR"


@app.route('/openfile/<path:filename>', methods=['GET', 'POST'])
def openfile(filename):
    get_user = request.cookies.get('user')
    get_token = request.cookies.get('token')
    if get_user in Sessions and get_token in Session_Tokens:
        path = main_path + r'\\' + get_user + r'\\' + filename
        f=open(path,"rb")
        ff=io.BytesIO(zlib.decompress(f.read()))
        varit = filename.rsplit('\\', 1)
        varity = varit[len(varit) - 1]
        return send_file(ff,download_name=varity)
    else:
        return "ERROR"


@app.route('/sign-in-check', methods=['GET'])
def signcheck():
    get_user = request.cookies.get('user')
    get_token = request.cookies.get('token')
    if get_user in Sessions and get_token in Session_Tokens:
        return "1"
    else:
        return "0"


@app.route('/search/<path:filename>', methods=['GET', 'POST'])
def search(filename):
    get_user = request.cookies.get('user')
    get_token = request.cookies.get('token')
    if get_user in Sessions and get_token in Session_Tokens:
        path = main_path + r'\\' + get_user
        var='['
        var+=search_folder(path,'',filename,'')
        var+='{"name":"no"}]'
        return var
    else:
        return "ERROR"


def search_folder(path, filename,search_term,carry):
    carry+=filename+'/'
    if filename != '':
        path = path + r'\\' + filename
    var = ''
    for i in os.listdir(path):
        if i.lower().startswith(search_term.lower()):
            if os.path.isfile(path + r'\\' + i):
                var += '{"name":"' + i + '","size":' + str(os.path.getsize(path + r'\\' + i)) + ',"type":"' + pathlib.Path(
                    path + r'\\' + i).suffix + '","path":"' + carry + i + '"},'
            else:
                var += '{"name":"' + i + '","size":' + str(
                    get_folder_size(path + r'\\' + i)) + ',"type":"folder","path":"' + carry + i + '"},'
        if not os.path.isfile(path + r'\\' + i):
            var+=search_folder(path,i,search_term,carry)
    return var


def sortfiletypes(path, filename,search_term,carry):
    carry+=filename+'/'
    if filename != '':
        path = path + r'\\' + filename
    var = ''
    for i in os.listdir(path):
        if os.path.isfile(path + r'\\' + i):
            if pathlib.Path(path + r'\\' + i).suffix in search_term:
                var += '{"name":"' + i + '","size":' + str(os.path.getsize(path + r'\\' + i)) + ',"type":"' + pathlib.Path(
                    path + r'\\' + i).suffix + '","path":"' + carry + i + '"},'
        else:
            var+=sortfiletypes(path,i,search_term,carry)
    return var


def get_folder_size(folder_path):
    total_size = 0

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)

    return total_size


@app.route('/sortfiles', methods=['POST'])
def sortfiles():
    json_data = request.get_json()
    get_user = request.cookies.get('user')
    get_token = request.cookies.get('token')
    if get_user in Sessions and get_token in Session_Tokens:
        path = main_path + r'\\' + get_user
        var = '['
        var += sortfiletypes(path, '', json_data, '')
        var += '{"name":"no"}]'
        return var
    else:
        return "ERROR"


@app.route('/reset', methods=['GET'])
def reset():
    global user_details
    for i in user_details:
        path=main_path+r'\\'+i["user"]
        shutil.rmtree(path)
    user_details=[]
    global Sessions
    global Session_Tokens
    Session_Tokens=[]
    Sessions=[]
    f = open('user_details.txt', 'w')
    json.dump(user_details, f)
    f.close()
    return "Resetted"


if __name__ == '__main__':
    app.run('0.0.0.0',80)
