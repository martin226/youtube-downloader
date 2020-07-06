<template>
  <div>
    <svg
      version="1.1"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 1440 126"
      xml:space="preserve"
    >
      <path
        fill="black"
        d="M685.6,38.8C418.7-11.1,170.2,9.9,0,30v96h1440V30C1252.7,52.2,1010,99.4,685.6,38.8z"
      />
    </svg>
    <div id="footer">
      <p id="footer-text" class="lead">
        © 2020 YouTube Downloader, made with
        <i class="fas fa-heart"></i> by Martin Sit.
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer"
};
</script>

<style scoped>
#footer {
  background: black;
  color: white;
  padding: 3em;
  padding-top: 0;
}
#footer-text {
  margin-bottom: 0;
}

svg {
  margin-bottom: -1.5px;
}
</style>