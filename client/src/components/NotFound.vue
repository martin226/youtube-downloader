<template>
  <div class="info-box">
    <h1 class="display-1">
      404 Not Found
    </h1>
    <p class="lead">
      :( Would you like to go back to the
      <router-link to="/">
        homepage
      </router-link>?
    </p>
  </div>
</template>

<script>
export default {
  name: 'NotFound',
};
</script>

<style scoped>
div{
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>