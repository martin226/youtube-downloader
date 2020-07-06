<template>
  <nav class="navbar navbar-light">
    <router-link id="nav-logo" class="navbar-brand" to="/">
      <i class="fab fa-youtube"></i>
      Youtube Downloader
    </router-link>
  </nav>
</template>

<script>
export default {
  name: "Navbar"
};
</script>

<style scoped>
.navbar-light {
  background: #3c096c;
  padding-left: 6em;
  padding-top: 2em;
}
.navbar-brand,
.navbar-light:focus,
.navbar-light:hover {
  color: white !important;
}

@media screen and (max-width: 732px) {
  .navbar {
    position: relative;
  }
  .navbar-brand {
    position: absolute;
    left: 50%;
    margin-left: -100px !important; /* 50% of your logo width */
    display: block;
  }
}
</style>