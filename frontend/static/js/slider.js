const cardContainer = document.getElementById('cardContainer');
let currentSlide = 0;

function updateSlide() {
    cardContainer.style.transform = `translateX(-${currentSlide * 320}px)`;
}

function prevSlide() {
    if (currentSlide > 0) {
        currentSlide--;
        updateSlide();
    }
}

function nextSlide() {
    if (currentSlide < cardContainer.children.length - 1) {
        currentSlide++;
        updateSlide();
    }
}
