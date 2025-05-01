<script>
import python from "../assets/img/logo/py_logo.svg";
import js from "../assets/img/logo/js.svg";
import vue from "../assets/img/logo/vuejs.svg";

export default {
    name: "wave",
    data() {
        return {
            images: [python, js, vue],
            currentIndex: 0,
            currentImage: python
        };
    },
    mounted() {
        this.startImageRotation();
    },
    methods: {
        startImageRotation() {
            setInterval(() => {
                this.currentIndex = (this.currentIndex + 1) % this.images.length;
                this.currentImage = this.images[this.currentIndex];
            }, 2000);
        }
    }
};
</script>

<template>
    <div style="position: relative">
        <svg class="waves" xmlns="http://www.w3.org/2000/svg" viewBox="0 24 150 28" preserveAspectRatio="none">
            <defs>
                <linearGradient id="waveGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" style="stop-color:transparent; stop-opacity:1" />
                    <stop offset="100%" style="stop-color:transparent; stop-opacity:1" />
                </linearGradient>
                <path id="gentle-wave" d="M-160 44c30 0 58-18 88-18s 58 18 88 18 58-18 88-18 58 18 88 18 v44h-352z" />
            </defs>
            <g class="parallax">
                <use xlink:href="#gentle-wave" x="48" y="0" fill="url(#waveGradient)" opacity="0.7" />
                <use xlink:href="#gentle-wave" x="48" y="3" fill="url(#waveGradient)" opacity="0.5" />
                <use xlink:href="#gentle-wave" x="48" y="5" fill="url(#waveGradient)" opacity="0.3" />
                <use xlink:href="#gentle-wave" x="48" y="7" fill="url(#waveGradient)" opacity="1" />
            </g>
        </svg>

        <!-- Logo dinamico -->
        <img class="boat" :src="currentImage" alt="Rotating image"
            style="position: absolute; top: -30px;" />
    </div>
</template>

<style scoped>
.waves {
    width: 100%;
    height: 120px;
}
</style>
