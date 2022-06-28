from flask import Flask, render_template,request,Response,url_for
from video_run import gen_frames
app = Flask(__name__)


print(type(gen_frames()))

#ホーム画面の表示
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/video_run')
def video_run():
    
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/laugh")
def laugh():
    return render_template("laugh.html")        



if __name__ =='__main__':
    app.run(debug=True)