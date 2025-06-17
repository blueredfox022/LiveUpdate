function updateCountdown() {
  const countdown = document.getElementById("countdown");
  const target = new Date(targetTime);
  const now = new Date();
  const diff = target - now;

  if (diff <= 0) {
    countdown.innerText = "⏰ Waktu Habis!";
    return;
  }

  const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
  const minutes = Math.floor((diff / (1000 * 60)) % 60);
  const seconds = Math.floor((diff / 1000) % 60);

  countdown.innerText = `${hours}j ${minutes}m ${seconds}d`;

  setTimeout(updateCountdown, 1000);
}

function fetchDonatur() {
  fetch("/data")
    .then(response => response.json())
    .then(data => {
      const list = document.getElementById("donatur-list");
      list.innerHTML = "";
      data.forEach(d => {
        const li = document.createElement("li");
        li.textContent = `${d.username} - ${d.status_verifikasi}`;
        li.className = d.status_verifikasi;
        list.appendChild(li);
      });
    });
}

setInterval(fetchDonatur, 5000);
window.onload = () => {
  updateCountdown();
  fetchDonatur();
};
