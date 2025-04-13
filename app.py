import os
import uuid
import tempfile
from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import yt_dlp

app = Flask(__name__)
app.secret_key = 'replace_this_with_a_secure_random_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        if not video_url:
            flash("Please provide a valid YouTube URL.")
            return redirect(url_for('index'))
        try:
            temp_dir = tempfile.mkdtemp()
            output_template = os.path.join(temp_dir, '%(title)s.%(ext)s')
            ydl_opts = {
                'outtmpl': output_template,
                'format': 'best',
                'noplaylist': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(video_url, download=True)
                video_title = info_dict.get('title', str(uuid.uuid4()))
                ext = info_dict.get('ext', 'mp4')
                file_path = os.path.join(temp_dir, f"{video_title}.{ext}")
            return send_file(file_path, as_attachment=True)
        except Exception as e:
            flash(f"Error: {str(e)}")
            return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)