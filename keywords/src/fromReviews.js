"use strict";

const fs = require("fs");
const removePunctuation = require("./removePunctuation");

const destination = process.argv[2];
console.log("Saving to", destination);

class Review {
	constructor(text) {
		const inQuotes = text.slice(text.indexOf('"')).split('","')
		this.manualTags = inQuotes[0].slice(1).split(",");
		this.content = inQuotes[1].slice(0, inQuotes[1].length - 1);
	}
}

const reviewsFile = fs.readFileSync("./data/reviews.csv", "utf8");

const keys = reviewsFile.split("\n")[0];
const reviewStrings = reviewsFile.split("\n").slice(1);

const wordsWithFrequency = {};
for (let reviewString of reviewStrings.slice(0, 10000)) {
	try {
		let review = new Review(reviewString);
		let words = review.content
			.split(" ")
			.map(removePunctuation)
			.concat(review.manualTags)
			.map((word) => word.toLowerCase())
		for (let word of words)
			wordsWithFrequency[word] = wordsWithFrequency[word] + 1 || 1;
	} catch (e) {}
}

let totalWords = 0;
for (let word in wordsWithFrequency)
	totalWords += wordsWithFrequency[word];

const wordsWithFrequencyAsArray = [];
for (let word in wordsWithFrequency) {
	wordsWithFrequencyAsArray.push({
		word: word,
		frequency: wordsWithFrequency[word],
		percentage: wordsWithFrequency[word] / totalWords
	})
}

wordsWithFrequencyAsArray.sort((a, b) => b.frequency - a.frequency);

fs.writeFileSync(destination, JSON.stringify(wordsWithFrequencyAsArray));
