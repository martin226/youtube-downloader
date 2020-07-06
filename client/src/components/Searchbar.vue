<template>
  <div>
    <div id="searchbar">
      <h1 id="title" class="text-center display-3">
        <router-link to="/">Youtube Downloader</router-link>
      </h1>
      <p class="lead">The #1 Youtube video downloader.</p>
      <div class="input-group input-group-lg mb-3">
        <div class="input-group-prepend">
          <span class="input-group-text">
            <i class="far fa-play-circle"></i>
          </span>
        </div>
        <input
          v-model="url"
          type="text"
          class="form-control"
          placeholder="Ex. https://www.youtube.com/watch?v=dQw4w9WgXcQ"
          @keyup.enter="downloadURL()"
        />
        <button class="btn btn-primary" @click="downloadURL()">Download!</button>
      </div>
    </div>
    <svg
      version="1.1"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 1440 126"
      xml:space="preserve"
    >
      <path
        fill="#3c096c"
        d="M685.6,38.8C418.7-11.1,170.2,9.9,0,30v96h1440V30C1252.7,52.2,1010,99.4,685.6,38.8z"
      />
    </svg>
  </div>
</template>

<script>
export default {
  name: "Searchbar",
  data() {
    return {
      url: ""
    };
  },
  methods: {
    downloadURL() {
      const videoID = this.youtube_parser(this.url);
      if (videoID) {
        this.$router.push({ name: "Download", params: { video_id: videoID } });
      } else {
        this.url = "";
        this.$swal(
          "Invalid URL",
          "You have provided an invalid Youtube link!",
          "error"
        );
      }
    },
    youtube_parser(url) {
      const regExp = /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*/;
      const match = url.match(regExp);
      return match && match[7].length === 11 ? match[7] : false;
    }
  }
};
</script>

<style scoped>
p {
  color: white;
}
#title a {
  color: white;
}
#title a:hover {
  text-decoration: none;
}
#searchbar {
  background: #3c096c;
  padding: 3em;
}

svg {
  margin-top: -1.5px;
  -webkit-transform: rotate(-180deg);
  -moz-transform: rotate(-180deg);
  -o-transform: rotate(-180deg);
  transform: rotate(-180deg);
}
</style>
