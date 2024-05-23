document.addEventListener('DOMContentLoaded', function () {
    fetch('BandsPlaying.txt')
      .then(response => response.text())
      .then(data => {
        document.getElementById('content').innerText = data;
      })
      .catch(error => console.error('Error fetching the text file:', error));
  });
  