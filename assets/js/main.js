// Smooth scroll para links de navegação
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Menu mobile
const mobileMenu = document.createElement('div');
mobileMenu.className = 'mobile-menu';
mobileMenu.innerHTML = '<i class="fas fa-bars"></i>';

mobileMenu.addEventListener('click', () => {
    document.querySelector('.nav-links').classList.toggle('active');
});

document.querySelector('.navbar').appendChild(mobileMenu);

// Animação de números
const observerOptions = {
    threshold: 0.5
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate');
        }
    });
}, observerOptions);

document.querySelectorAll('.stat-number').forEach(stat => {
    observer.observe(stat);
});

// Formulário de contato
document.querySelector('.contact-form').addEventListener('submit', function(e) {
    e.preventDefault();
    // Aqui você pode adicionar a lógica para enviar o formulário
    alert('Mensagem enviada com sucesso!');
    this.reset();
});

// Newsletter
document.querySelector('.newsletter-form').addEventListener('submit', function(e) {
    e.preventDefault();
    // Aqui você pode adicionar a lógica para cadastrar na newsletter
    alert('E-mail cadastrado com sucesso!');
    this.reset();
});

// Adicionar ao final do arquivo
const portfolioSwiper = new Swiper('.portfolio-swiper', {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    centeredSlides: true,
    autoplay: {
        delay: 3000,
        disableOnInteraction: false,
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    breakpoints: {
        640: {
            slidesPerView: 1.5,
        },
        1024: {
            slidesPerView: 2.5,
        },
        1400: {
            slidesPerView: 3.5,
        },
    },
    effect: 'coverflow',
    coverflowEffect: {
        rotate: 0,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows: false,
    },
});

// Adicionar efeito de hover pause
const swiperContainer = document.querySelector('.portfolio-swiper');
swiperContainer.addEventListener('mouseenter', () => {
    portfolioSwiper.autoplay.stop();
});
swiperContainer.addEventListener('mouseleave', () => {
    portfolioSwiper.autoplay.start();
}); 