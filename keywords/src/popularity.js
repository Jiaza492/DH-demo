// this file will determine how common a word is in the English language
// it goes through various books and finds the most common words in each
// it then will determine how common a word is based its ranking
// to find the popularity

const fs = require("fs");
const logarithmic = require("logarithmic");
const popularity = require("./popularity.json"); // previous findings

const writingDirectory = "/data/writing/";

const wordsWithRank = {};

fs.readdir(__dirname + writingDirectory, (err, filenames) => {
	"use strict";

	if (err) {
		logarithmic.error(err);
		return;
	}

	const wordsWithFrequency = {};
	const words = filenames
		.map((filename) => __dirname + writingDirectory + filename) // get the full address
		.map((file) => fs.readFileSync(file, {encoding: "utf8"})) // read the books
		.join(" ") // combine all the books together
		.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g,"") // remove all punctuation
		.replace(/\s{2,}/g," ") // clean up after removing the punctuation
		.split(" ") // split up the words
		.map((word) => word.toLowerCase())
		.forEach((word) => {
			if (wordsWithFrequency[word])
				wordsWithFrequency[word]++;
			else
				wordsWithFrequency[word] = 1;
		})

	let wordsWithFrequencyAsArray = [];
	for (let word in wordsWithFrequency)
		wordsWithFrequencyAsArray.push({
			word: word,
			frequency: wordsWithFrequency[word]
		})
	wordsWithFrequencyAsArray = wordsWithFrequencyAsArray.sort((a, b) => b.frequency - a.frequency);
	for (let i in wordsWithFrequencyAsArray) {
		wordsWithRank[wordsWithFrequencyAsArray[i].word] = Number(i);
	}
	fs.writeFile("popularity.json", JSON.stringify(wordsWithRank));
})

module.exports = (word) => popularity[word] !== undefined ? popularity[word] : Infinity;
