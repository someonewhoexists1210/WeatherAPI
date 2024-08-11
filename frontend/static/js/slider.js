document.addEventListener('DOMContentLoaded', function() {
	const slides = document.querySelectorAll('.weather-info');
	const prevButton = document.getElementById('prevSlide');
	const nextButton = document.getElementById('nextSlide');
	let currentSlide = 0;

	function showSlide(index) {
		slides.forEach((slide, i) => {
			slide.style.display = (i === index) ? 'block' : 'none';
		});
	}

	prevButton.addEventListener('click', function() {
		currentSlide = (currentSlide > 0) ? currentSlide - 1 : slides.length - 1;
		showSlide(currentSlide);
	});

	nextButton.addEventListener('click', function() {
		currentSlide = (currentSlide < slides.length - 1) ? currentSlide + 1 : 0;
		showSlide(currentSlide);
	});

	showSlide(currentSlide);
});
