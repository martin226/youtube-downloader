# Youtube Downloader

<p align="center">
    <img src="./docs/logo.png" alt="Project Logo"></img>
</p>

Youtube video downloader Progressive Web App built using Flask and VueJS.

## Built With

Name | Description
------------ | -------------
Bootstrap 4 | The most popular front-end framework for developing responsive, mobile first projects on the web.
Vue.JS | Vue.js is a progressive, incrementally-adoptable JavaScript framework for building UI on the web.
@vue/cli-plugin-pwa | pwa plugin for vue-cli
Font-Awesome 5 | The iconic SVG, font, and CSS toolkit
Vue-Router | 🚦 The official router for Vue.js.
Vue-Sweetalert2 | A convenient wrapper for sweetalert2.
Flask | The Python micro framework for building web applications.
Flask-Cors | A Flask extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.
Pafy | Python library to download YouTube content and retrieve metadata

## Quickstart

### Prerequisites

- (optional) Create a .env file in the server directory with the variables YOUTUBE_API_KEY and FLASK_ENV with your respective Youtube API key and Flask environment (production/development). Both variables may be kept blank, as the shared Pafy Youtube API key will be used and the production environment will be set by default.

- Have NodeJS and Python 3 installed

### Installation

```bash
# Install backend dependencies
cd server
pip install -r requirements.txt

# Start backend Flask DevServer
cd server
export FLASK_ENV=development
flask run

# Install frontend dependencies
cd client
npm install

# Start frontend Vue DevServer
cd client
npm run serve

# Build frontend for production
cd client
npm run build

```

## API Routes

* GET /api/download/:video_id (retrieves download links for the given video_id, as well as basic info for each of them)

* GET /api/info/:video_id (retrieves video info and statistics)

## Version

1.0.0

## License

[MIT](http://opensource.org/licenses/MIT)
Copyright (c) 2020 Martin Sit
