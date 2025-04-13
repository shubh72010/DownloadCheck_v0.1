document.getElementById('download-btn').addEventListener('click', function() {
    var url = document.getElementById('url').value;
    if (url) {
        document.getElementById('status-message').textContent = 'Processing...';
        fetch('/download', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'url=' + encodeURIComponent(url),
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                document.getElementById('status-message').textContent = `Video: ${data.title}`;
                var downloadLink = document.getElementById('download-link');
                downloadLink.href = data.url;
                downloadLink.style.display = 'inline-block';
            } else {
                document.getElementById('status-message').textContent = 'Error: ' + data.message;
            }
        })
        .catch(error => {
            document.getElementById('status-message').textContent = 'Error: ' + error;
        });
    } else {
        document.getElementById('status-message').textContent = 'Please enter a valid YouTube URL.';
    }
});
