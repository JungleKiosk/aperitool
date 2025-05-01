<script>
import HomeMain from "../components/main/HomeMain.vue";
import Wave from "./../components/Wave.vue";

export default {
    name: "home",
    components: {
        HomeMain, Wave
    }

};
</script>

<template>
    <div>
        <Wave></Wave>
        <main class="container">
            <HomeMain></HomeMain>
        </main>

    </div>
</template>

<style scoped></style>
