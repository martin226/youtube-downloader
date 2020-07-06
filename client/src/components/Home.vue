<template>
  <div>
    <Navbar />
    <SearchBar />

    <div class="info-box">
      <h1 class="title display-4">How To Use The Downloader</h1>
      <div id="tutorial">
        <div>
          <i class="fab fa-searchengin"></i>
          <h3 class="sub-title display-4">Find a video on Youtube</h3>
          <p
            class="lead"
          >Search for a video you'd like to download on Youtube, and then copy the link to it.</p>
        </div>
        <div>
          <i class="fas fa-clipboard"></i>
          <h3 class="sub-title display-4">Paste the link</h3>
          <p class="lead">Paste the link to the Youtube video in our website's input field.</p>
        </div>
        <div>
          <i class="fas fa-cloud-download-alt"></i>
          <h3 class="sub-title display-4">Download video</h3>
          <p
            class="lead"
          >Press the "Download!" button and browse through the list of formats to find the one you'd like to download.</p>
        </div>
        <div class="col">
          <i class="fas fa-film"></i>
          <h3 class="sub-title display-4">Enjoy the video</h3>
          <p class="lead">Have some popcorn while you enjoy watching your ad-less downloaded video!</p>
        </div>
      </div>
      <div id="cta-div">
        <button class="btn btn-lg btn-primary cta" @click="scrollUp()">Download Now!</button>
      </div>
    </div>

    <Footer />
  </div>
</template>

<script>
import SearchBar from "./Searchbar.vue";
import Footer from "./Footer.vue";
import Navbar from "./Navbar.vue";

export default {
  name: "Home",
  components: {
    SearchBar,
    Footer,
    Navbar
  },
  methods: {
    scrollUp() {
      window.scrollTo(0, 0);
    }
  }
};
</script>

<style scoped>
#tutorial, #cta-div {
  padding-top: 2.5em;
}
#tutorial div svg {
  font-size: 30px;
}
.fa-searchengin {
  color: #023e7d;
}
.fa-clipboard {
  color: #f28f3b;
}
.fa-cloud-download-alt {
  color: #008000;
}
.fa-film {
  color: #235789;
}
.cta {
  background: #3c096c;
}
</style>
