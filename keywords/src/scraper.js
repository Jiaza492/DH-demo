// this file uses the internet to find common makeup keywords, like 'mascara'
"use strict";

const logarithmic = require("logarithmic");
const makeRequest = require("request");
const fs = require("fs");

Array.prototype.flatten = function() {
	var ret = [];
	for(var i = 0; i < this.length; i++) {
		if(Array.isArray(this[i])) {
			ret = ret.concat(this[i].flatten());
		} else {
			ret.push(this[i]);
		}
	}
	return ret;
};

const filename = process.argv[2];
const subreddits = process.argv.slice(3);
logarithmic.alert(`Writing ${subreddits} to ${filename}`);

const wordsWithFrequency = {};
let requests = 0;
const request = (url, next) => {
	requests++;
	makeRequest(url, (a, b, c) => {
		requests--;
		next(a, b, c);
	});
}

subreddits.forEach((subreddit) => {
	request(`https://www.reddit.com/r/${subreddit}/comments.json`, (err, code, response) => {
		"use strict";

		if (err) {
			logarithmic.error(err);
			return;
		}

		const posts = JSON.parse(response).data.children;
		const postURLs = posts
			.map((post) => `http://reddit.com/r/${subreddit}/comments/${post.data.link_id.substring(3)}`)

		postURLs.forEach((postURL) => {
			request(postURL + "/comments.json", (error, responseCode, postRaw) => {
				if (err) {
					logarithmic.error(err);
					return;
				}

				const post = JSON.parse(postRaw);
				const commentObjects = post[1].data.children;
				const comments = commentObjects.map((comment) => comment.data.body)
				const words = comments
					.filter((comment) => Boolean(comment))
					.map((comment) => comment.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g,"")) // remove all punctuation
					.map((comment) => comment.replace(/\s{2,}/g," ")) // clean up after removing the punctuation
					.map((comment) => comment.split(" "))
					.flatten()
					.map((comment) => comment.toLowerCase())

				words.forEach((comment) => {
					wordsWithFrequency[comment] = wordsWithFrequency[comment] + 1 || 1;
				})
			})
		})
	})
})

setInterval(() => {
	if (requests === 0) {
		const wordsWithFrequencyAsArray = [];

		let totalWords = 0;
		for (let word in wordsWithFrequency)
			totalWords += wordsWithFrequency[word];

		for (let word in wordsWithFrequency) {
			wordsWithFrequencyAsArray.push({
				word: word,
				frequency: wordsWithFrequency[word],
				percentage: wordsWithFrequency[word] / totalWords
			});
		}

		wordsWithFrequencyAsArray.sort((a, b) => b.frequency - a.frequency);

		fs.writeFile(filename, JSON.stringify(wordsWithFrequencyAsArray), (err) => {
			if (err) {
				logarithmic.error(err);
				process.exit(1);
			}

			console.log("Written to " + filename);
			process.exit(0);
		});
	}
}, 1000);
