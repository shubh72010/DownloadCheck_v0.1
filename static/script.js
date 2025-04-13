document.addEventListener('DOMContentLoaded', () => {
  const tiles = document.querySelectorAll('.tile');
  tiles.forEach((tile, i) => {
    tile.style.animation = `popIn 0.4s ease ${i * 0.1}s both`;
  });
});

const style = document.createElement('style');
style.innerHTML = `
@keyframes popIn {
  from {
    opacity: 0;
    transform: scale(0.8);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}`;
document.head.appendChild(style);