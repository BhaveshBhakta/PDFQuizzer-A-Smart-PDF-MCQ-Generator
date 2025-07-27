document.getElementById('pdf_file').addEventListener('change', function(e) {
    const label = document.querySelector('.file-input-label');
    if (e.target.files.length > 0) {
        label.innerHTML = `📄 ${e.target.files[0].name}`;
        label.style.borderColor = '#667eea';
        label.style.background = '#edf2f7';
    }
});

document.getElementById('mcqForm').addEventListener('submit', function() {
    document.getElementById('loading').style.display = 'block';
    document.querySelector('.submit-btn').disabled = true;
    document.querySelector('.submit-btn').innerHTML = 'Generating...';
});