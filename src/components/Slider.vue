<script>
import img1 from "../assets/img/jumbo/1.jpg";
import img2 from "../assets/img/jumbo/2.jpg";
import img3 from "../assets/img/jumbo/3.jpg";

export default {
    name: "SliderImg",
    data() {
        return {
            currentSlide: 0,
            images: [img1, img2, img3]
        };
    },
    methods: {
        nextSlide() {
            this.currentSlide = (this.currentSlide + 1) % this.images.length;
        },
        prevSlide() {
            this.currentSlide = (this.currentSlide - 1 + this.images.length) % this.images.length;
        },
        autoSlide() {
            setInterval(this.nextSlide, 5000); // Cambia immagine ogni 3 secondi
        }
    },
    mounted() {
        this.autoSlide(); // Avvia il carosello automatico
    }
};
</script>

<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-12 col-lg-4 p-4">
                <div class="carousel">
                    <div class="carousel-inner">
                        <img v-for="(img, index) in images" :key="index" :src="img"
                            :class="{ active: index === currentSlide }" class="carousel-image img_jumbo rounded-4" alt="Immagine" />
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<style scoped>
.carousel {
    display: flex;
    justify-content: center; /* Centra il carosello */
    align-items: center; /* Allinea verticalmente */
    width: 100%; 
}

.carousel-inner {
    position: relative;
    width: 100%;
    max-width: 400px; /* Imposta una larghezza massima */
    height: 300px; /* Altezza del carosello */
}

.carousel-image {
    position: absolute;
    width: 100%;
    height: 100%;
    object-fit: cover; /* Assicura che l'immagine si adatti */
    opacity: 0;
    transition: opacity 1s ease-in-out;
}

/* Mostra solo l'immagine attiva */
.carousel-image.active {
    opacity: 1;
}



/* Pulsanti */
/* .prev, .next {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background-color: rgba(0, 0, 0, 0.5);
    color: white;
    border: none;
    padding: 10px;
    cursor: pointer;
    font-size: 24px;
    border-radius: 50%;
    width: 40px;
    height: 40px;
}

.prev {
    left: 10px;
}

.next {
    right: 10px;
}

.prev:hover, .next:hover {
    background-color: rgba(0, 0, 0, 0.8);
} */
</style>
