from flask import Flask, render_template, request, jsonify
import youtube_dl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': './downloads/%(title)s.%(ext)s',
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', None)
            video_url = info_dict.get('url', None)
        return jsonify({'status': 'success', 'title': video_title, 'url': video_url})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
