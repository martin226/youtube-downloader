<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style>
html,
body {
  color: black;
  text-align: center;
}

input{
  box-shadow: none;
  border-bottom: none !important;
}
.info-box {
  background: white;
  padding: 2em;
}
.divider {
  font-size: 50px;
  position: absolute;
  margin: -25px 0 0 -25px;
}
.title {
  font-size: 45px;
}
.sub-title {
  font-size: 30px;
}
</style>
