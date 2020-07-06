<template>
  <div class="w-100">
    <div v-if="isFetching" id="loader" />
    <div v-else class="slide-in">
      <Navbar />
      <Searchbar />
      <div v-if="streams.length > 0">
        <div class="info-box">
          <h1 class="display-4 video-title">{{ info.title }}</h1>

          <p class="lead">
            <i class="far fa-user-circle"></i>
            {{ info.author }} |
            <i class="far fa-eye"></i>
            {{ info.viewcount }} |
            <i class="far fa-thumbs-up"></i>
            {{ info.likes }} |
            <i class="far fa-thumbs-down"></i>
            {{ info.dislikes }}
          </p>

          <div class="video-container">
            <iframe
              type="text/html"
              :src="`https://www.youtube.com/embed/${$route.params.video_id}?rel=0`"
              frameborder="0"
              width="500px"
              height="235px"
              allow="modestbranding"
            />
          </div>
        </div>

        <div class="info-box">
          <p class="lead">
            There are
            <strong>{{ streamcount }}</strong> formats available for download!
          </p>
          <div class="row">
            <div v-for="(streamtype, index) in filterStreams(streams)" :key="index" class="col-xl">
              <p class="lead">
                <strong>{{ streamtype[0].mediatype }} formats</strong>
              </p>
              <table class="table">
                <thead>
                  <tr>
                    <th scope="col">Type</th>
                    <th scope="col">Quality</th>
                    <th scope="col">Extension</th>
                    <th scope="col">Download</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="stream in streamtype" :key="stream.url">
                    <td>{{ stream.mediatype }}</td>
                    <td>{{ stream.quality }}</td>
                    <td>{{ stream.extension }}</td>
                    <td>
                      <button class="btn btn-primary" @click="download(stream.url)">
                        Download
                        <i class="fas fa-arrow-circle-down"></i>
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
      <div v-else class="info-box-2">
        <img src="@/assets/warning.png" alt="Error" width="256" />
        <h1 class="display-4">An error has occurred :(</h1>
        <p class="lead">Error: {{ error }}</p>
      </div>
      <Footer />
    </div>
  </div>
</template>

<script>
import ApiClient from "../ApiClient";
import Searchbar from "./Searchbar.vue";
import Footer from "./Footer.vue";
import Navbar from "./Navbar.vue";

export default {
  name: "Download",
  components: {
    Searchbar,
    Footer,
    Navbar,
  },
  data() {
    return {
      isFetching: true,
      streams: [],
      info: {},
      error: "An unknown error has occurred."
    };
  },
  computed: {
    streamcount() {
      return this.streams.flat().length;
    }
  },
  watch: {
    "$route.params.video_id": function() {
      this.isFetching = true;
      this.streams = [];
      this.loadPage();
    }
  },
  beforeMount() {
    this.loadPage();
  },
  methods: {
    async downloadVideo(videoID) {
      await ApiClient.downloadVideo(videoID)
        .then(streams => {
          this.streams = streams;
        })
        .catch(err => {
          this.error = err.error;
        });
    },
    async infoVideo(videoID) {
      await ApiClient.infoVideo(videoID)
        .then(info => {
          this.info = info;
        })
        .catch(err => {
          this.error = err.error;
        });
    },
    loadPage() {
      this.downloadVideo(this.$route.params.video_id).then(() => {
        this.infoVideo(this.$route.params.video_id).then(() => {
          this.isFetching = false;
        });
      });
    },
    download(url) {
      window.open(url);
      this.$swal(
        "Downloaded",
        "Successfully downloaded Youtube video!",
        "success"
      );
    },
    filterStreams(streams) {
      return streams.filter(el => el.length);
    }
  }
};
</script>

<style scoped>
tr,
td {
  color: black;
}

table {
  display: inline-table;
}

.video-title {
  font-size: 40px;
}

#loader {
  position: absolute;
  left: 50%;
  top: 50%;
  z-index: 1;
  width: 150px;
  height: 150px;
  margin: -75px 0 0 -75px;
  border: 16px solid #f3f3f3;
  border-radius: 50%;
  border-top: 16px solid #3498db;
  width: 120px;
  height: 120px;
  -webkit-animation: spin 2s linear infinite;
  animation: spin 2s linear infinite;
}


.slide-in {
  position: relative;
  -webkit-animation-name: slide-in;
  -webkit-animation-duration: 1s;
  animation-name: slide-in;
  animation-duration: 1s;
}

@media screen and (max-width: 550px) {
  .video-container {
    display: none !important;
  }

  tr th:nth-child(1),
  tr td:nth-child(1) {
    display: none;
  }

  .info-box-2 {
    padding: 0;
  }
}

@-webkit-keyframes spin {
  0% {
    -webkit-transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
  }
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

@-webkit-keyframes slide-in {
  from {
    bottom: -100px;
    opacity: 0;
  }
  to {
    bottom: 0px;
    opacity: 1;
  }
}

@keyframes slide-in {
  from {
    bottom: -100px;
    opacity: 0;
  }
  to {
    bottom: 0;
    opacity: 1;
  }
}
</style>
