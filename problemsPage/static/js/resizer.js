
const resizer = document.getElementById('resizer');
    const leftPanel = document.getElementById('leftPanel');

    resizer.addEventListener('mousedown', function (e) {
        document.addEventListener('mousemove', resize);
        document.addEventListener('mouseup', stopResize);
    });

    function resize(e) {
        const newWidth = e.clientX;
        if (newWidth >= 200 && newWidth <= window.innerWidth * 0.8) {
            leftPanel.style.width = newWidth + 'px';
        }
    }

    function stopResize() {
        document.removeEventListener('mousemove', resize);
        document.removeEventListener('mouseup', stopResize);
    }
