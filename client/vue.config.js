const path = require('path');

module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:5000'
      }
    }
  },
  outputDir: path.resolve(__dirname, '../server/public'),
  pwa: {
    name: "Youtube Downloader",
    iconPaths: {
      favicon32: "images/icons/favicon32.png",
      favicon16: "images/icons/favicon16.png",
      appleTouchIcon: 'images/icons/icon-152x152.png',
      maskIcon: "images/icons/safari-pinned-tab.svg",
      msTileImage: 'images/icons/icon-144x144.png'
    }
  }
};