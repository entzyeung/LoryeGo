// Add smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// News Carousel logic
let currentIndex = 0;
const totalCards = 4;
const cardWidth = 280 + 20; // Card width (280px) + margin (20px)

function scrollCarousel(direction) {
    const carousel = document.getElementById('newsCarousel');
    const maxIndex = totalCards - 1;

    if (direction === 'left' && currentIndex > 0) {
        currentIndex--;
    } else if (direction === 'right' && currentIndex < maxIndex) {
        currentIndex++;
    }

    const translateX = -currentIndex * cardWidth;
    carousel.style.transform = `translateX(${translateX}px)`;

    document.querySelectorAll('.news-card').forEach(card => {
        card.style.width = `${280}px`;
        card.style.marginRight = `${20}px`;
    });

    document.querySelectorAll('#newsDots .dot').forEach((dot, index) => {
        dot.classList.toggle('active', index === currentIndex);
    });

    const leftArrow = document.querySelector('#news .carousel-btn.left');
    const rightArrow = document.querySelector('#news .carousel-btn.right');
    leftArrow.style.display = currentIndex === 0 ? 'none' : 'flex';
    rightArrow.style.display = currentIndex === maxIndex ? 'none' : 'flex';
}

function initializeNewsCarousel() {
    document.querySelectorAll('.news-card').forEach(card => {
        card.style.width = `${280}px`;
        card.style.marginRight = `${20}px`;
    });
    scrollCarousel('stay');
}

document.querySelectorAll('#newsDots .dot').forEach(dot => {
    dot.addEventListener('click', () => {
        const newIndex = parseInt(dot.getAttribute('data-index'));
        if (newIndex !== currentIndex) {
            currentIndex = newIndex;
            scrollCarousel('dot');
        }
    });
});

// Screenshot Carousel logic
let screenshotIndex = 0;
const totalScreenshots = 6;
let autoLoopInterval = null;

function scrollScreenshotCarousel(direction) {
    const carousel = document.getElementById('screenshotCarousel');
    const maxScreenshotIndex = totalScreenshots - 1;
    const isResponsive = window.innerWidth <= 770;
    const container = document.querySelector('.screenshot-carousel-container');
    const containerWidth = container ? container.offsetWidth : (isResponsive ? window.innerWidth : 770);

    if (direction === 'left' && screenshotIndex > 0) {
        screenshotIndex--;
    } else if (direction === 'right') {
        screenshotIndex++;
        if (screenshotIndex > maxScreenshotIndex) {
            screenshotIndex = 0; // Loop back to the first screenshot
        }
    }

    const translateX = -screenshotIndex * containerWidth;
    carousel.style.transform = `translateX(${translateX}px)`;

    document.querySelectorAll('.screenshot-item').forEach(item => {
        item.style.width = `${containerWidth}px`;
    });

    document.querySelectorAll('#screenshotDots .dot').forEach((dot, index) => {
        dot.classList.toggle('active', index === screenshotIndex);
    });

    const leftArrow = document.querySelector('#screenshots .carousel-btn.left');
    const rightArrow = document.querySelector('#screenshots .carousel-btn.right');
    leftArrow.style.display = screenshotIndex === 0 ? 'none' : 'flex';
    rightArrow.style.display = screenshotIndex === maxScreenshotIndex ? 'none' : 'flex';
}

function initializeScreenshotCarousel() {
    const isResponsive = window.innerWidth <= 770;
    const container = document.querySelector('.screenshot-carousel-container');
    const containerWidth = container ? container.offsetWidth : (isResponsive ? window.innerWidth : 770);

    document.querySelectorAll('.screenshot-item').forEach(item => {
        item.style.width = `${containerWidth}px`;
    });

    scrollScreenshotCarousel('stay');
}

// Auto-loop functionality for screenshot carousel
function startAutoLoop() {
    if (autoLoopInterval) clearInterval(autoLoopInterval); // Clear any existing interval
    autoLoopInterval = setInterval(() => {
        scrollScreenshotCarousel('right');
    }, 3000); // 3000ms = 3 seconds
}

function stopAutoLoop() {
    if (autoLoopInterval) {
        clearInterval(autoLoopInterval);
        autoLoopInterval = null;
    }
}

// Add event listeners for dots and arrows to stop auto-loop on user interaction
document.querySelectorAll('#screenshotDots .dot').forEach(dot => {
    dot.addEventListener('click', () => {
        stopAutoLoop(); // Stop auto-loop on dot click
        const newIndex = parseInt(dot.getAttribute('data-index'));
        if (newIndex !== screenshotIndex) {
            screenshotIndex = newIndex;
            scrollScreenshotCarousel('dot');
        }
    });
});

document.querySelector('#screenshots .carousel-btn.left').addEventListener('click', () => {
    stopAutoLoop(); // Stop auto-loop on left arrow click
    scrollScreenshotCarousel('left');
});

document.querySelector('#screenshots .carousel-btn.right').addEventListener('click', () => {
    stopAutoLoop(); // Stop auto-loop on right arrow click
    scrollScreenshotCarousel('right');
});

// Update carousels on load and resize
function updateCarousels() {
    initializeNewsCarousel();
    scrollCarousel('stay');
    initializeScreenshotCarousel();
    scrollScreenshotCarousel('stay');
    startAutoLoop(); // Start auto-loop on load
}

document.addEventListener('DOMContentLoaded', updateCarousels);
window.addEventListener('resize', () => {
    stopAutoLoop(); // Stop auto-loop on resize to prevent glitches
    updateCarousels();
    startAutoLoop(); // Restart auto-loop after resize
});