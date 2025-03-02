/**
 * Configuração do Swiper para os projetos do portfólio
 * @type {Object}
 */
const SWIPER_CONFIG = {
    effect: 'fade',
    autoplay: {
        delay: 5000,
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
    loop: true,
    on: {
        init: function() {
            console.log('Swiper inicializado com sucesso');
        },
        error: function(error) {
            console.error('Erro ao inicializar Swiper:', error);
        }
    }
};

/**
 * Classe responsável pelo gerenciamento do portfólio
 */
class PortfolioManager {
    constructor() {
        this.filterButtons = document.querySelectorAll('.filter-btn');
        this.projectCards = document.querySelectorAll('.project-card');
        this.swipers = [];
        this.init();
    }

    /**
     * Inicializa o gerenciador de portfólio
     */
    init() {
        this.initializeSwipers();
        this.setupFilterButtons();
        this.setupProjectCards();
        this.setInitialState();
    }

    /**
     * Inicializa os Swipers para cada projeto
     */
    initializeSwipers() {
        try {
            const projectSwipers = document.querySelectorAll('.project-swiper');
            projectSwipers.forEach(swiperElement => {
                const swiper = new Swiper(swiperElement, SWIPER_CONFIG);
                this.swipers.push(swiper);
            });
        } catch (error) {
            console.error('Erro ao inicializar Swipers:', error);
        }
    }

    /**
     * Configura os botões de filtro
     */
    setupFilterButtons() {
        this.filterButtons.forEach(button => {
            button.addEventListener('click', (e) => this.handleFilterClick(e));
        });
    }

    /**
     * Manipula o clique nos botões de filtro
     * @param {Event} event - Evento de clique
     */
    handleFilterClick(event) {
        const button = event.target;
        const filterValue = button.getAttribute('data-filter');

        this.updateActiveButton(button);
        this.filterProjects(filterValue);
    }

    /**
     * Atualiza o botão ativo
     * @param {HTMLElement} activeButton - Botão que foi clicado
     */
    updateActiveButton(activeButton) {
        this.filterButtons.forEach(btn => btn.classList.remove('active'));
        activeButton.classList.add('active');
    }

    /**
     * Filtra os projetos com base na categoria selecionada
     * @param {string} filterValue - Valor do filtro selecionado
     */
    filterProjects(filterValue) {
        const animationDuration = 300;

        this.projectCards.forEach(card => {
            this.animateCardOut(card);

            setTimeout(() => {
                const shouldDisplay = this.shouldDisplayCard(card, filterValue);
                card.style.display = shouldDisplay ? 'block' : 'none';

                if (shouldDisplay) {
                    this.animateCardIn(card);
                }
            }, animationDuration);
        });
    }

    /**
     * Verifica se o card deve ser exibido
     * @param {HTMLElement} card - Card do projeto
     * @param {string} filterValue - Valor do filtro
     * @returns {boolean}
     */
    shouldDisplayCard(card, filterValue) {
        if (filterValue === 'all') return true;
        const categories = card.getAttribute('data-category')?.split(',') || [];
        return categories.includes(filterValue);
    }

    /**
     * Anima a saída do card
     * @param {HTMLElement} card - Card do projeto
     */
    animateCardOut(card) {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
    }

    /**
     * Anima a entrada do card
     * @param {HTMLElement} card - Card do projeto
     */
    animateCardIn(card) {
        requestAnimationFrame(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        });
    }

    /**
     * Configura os cards dos projetos
     */
    setupProjectCards() {
        this.projectCards.forEach(card => {
            card.style.transition = 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
            
            card.addEventListener('mouseenter', () => {
                this.handleCardHover(card, true);
            });

            card.addEventListener('mouseleave', () => {
                this.handleCardHover(card, false);
            });
        });
    }

    /**
     * Manipula o hover nos cards
     * @param {HTMLElement} card - Card do projeto
     * @param {boolean} isEntering - Indica se o mouse está entrando ou saindo
     */
    handleCardHover(card, isEntering) {
        const swiper = card.querySelector('.swiper-container')?.swiper;
        if (swiper) {
            isEntering ? swiper.autoplay.start() : swiper.autoplay.stop();
        }
    }

    /**
     * Define o estado inicial da página
     */
    setInitialState() {
        const allButton = document.querySelector('.filter-btn[data-filter="all"]');
        if (allButton) {
            allButton.classList.add('active');
        }
    }
}

// Inicializa o gerenciador de portfólio quando o DOM estiver pronto
document.addEventListener('DOMContentLoaded', () => {
    try {
        new PortfolioManager();
    } catch (error) {
        console.error('Erro ao inicializar o PortfolioManager:', error);
    }
}); 