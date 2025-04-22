<script>

export default {
    name: "WaveMirrow",

};
</script>


<template>
    <div>
        <!-- Onda inferiore specchiata -->
        <svg class="waves flipped" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
            viewBox="0 24 150 28" preserveAspectRatio="none" shape-rendering="auto">
            <g class="parallax">
                <use xlink:href="#gentle-wave" x="48" y="0" fill="url(#waveGradient)" opacity="0.7" />
                <use xlink:href="#gentle-wave" x="48" y="3" fill="url(#waveGradient)" opacity="0.5" />
                <use xlink:href="#gentle-wave" x="48" y="5" fill="url(#waveGradient)" opacity="0.3" />
                <use xlink:href="#gentle-wave" x="48" y="7" fill="url(#waveGradient)" opacity="1" />
            </g>
        </svg>
    </div>
</template>

<style scoped></style>
