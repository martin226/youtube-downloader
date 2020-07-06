// REST API URL
const url = '../api';

// Asynchronous Client using Javascript Fetch APIs
class ApiClient {
  // Retrieve video streams
  static downloadVideo(videoID) {
    return new Promise((resolve, reject) => {
      fetch(`${url}/download/${videoID}/`)
        .then((response) => {
          if (!response.ok) {
            response.json()
              .then(resp => reject(resp));
          } else {
            resolve(response.json());
          }
        })
        .catch((err) => {
          reject({
            error: err.message,
          });
        });
    });
  }

  // Retrieve video info
  static infoVideo(videoID) {
    return new Promise((resolve, reject) => {
      fetch(`${url}/info/${videoID}/`)
        .then((response) => {
          if (!response.ok) {
            response.json()
              .then(resp => reject(resp));
          } else {
            resolve(response.json());
          }
        })
        .catch((err) => {
          reject({
            error: err.message,
          });
        });
    });
  }
}

export default ApiClient;
