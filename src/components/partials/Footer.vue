<script setup></script>

<template>
  <footer id="footer" class="p-5 bg-dark">
    <div class="row justify-content-center mt-5">
      <div class="col-sm-4 col-md-3 text-center">
        <h3 class="">Follow me</h3>
        <a target="_blank" href="https://github.com/JungleKiosk"
          ><img
            class="icon_social mx-2"
            src="../../assets/img/logo/github_footer.svg"
            alt=""
        /></a>
        <a
          target="_blank"
          href="https://www.linkedin.com/in/francescominutella/"
          ><img
            class="icon_social mx-2"
            src="../../assets/img/logo/linkedin_footer.svg"
            alt=""
        /></a>
        <a target="_blank" href="https://www.youtube.com/@JungleKiosk"
          ><img
            class="icon_social mx-2"
            src="../../assets/img/logo/youtube_footer.svg"
            alt=""
        /></a>
      </div>
    </div>
    <div class="row justify-content-center mt-5">
      <div class="col-12 col-lg-2 text-center"></div>
    </div>
  </footer>
</template>

<style scoped>
.icon_social {
  width: 10%;
}

ul li {
  list-style: none;
}

#footer {
  height: 400px;
}

@media (max-width: 786px) {
  .icon_social {
    width: 20%;
  }
}
</style>
