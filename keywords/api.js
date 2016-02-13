// this is a Node.js script that powers a small API for finding keywords
// make sure that you have NPM and Node.js installed
// install for Mac: http://blog.teamtreehouse.com/install-node-js-npm-mac
// once you have NPM and Node.js, run the API with the following command:
// npm start

const express = require("express");
const keywordsIn = require("./src/keywords.js");

const app = express();

app.get("/text/:text", (request, response) => {
	const text = request.params.text;
});
