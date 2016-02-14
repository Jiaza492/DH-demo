// this finds the difference in the usage percentage between 2 sets of word data
"use strict";

const fs = require("fs");
const popular = require("./popular");

module.exports = (datasets) => {
	const wordsWithFrequencies = [];
	for (let i in datasets) {
		wordsWithFrequencies[i] = {};
		for (let word of popular(datasets[i])) {
			wordsWithFrequencies[i][word.word] = word.percentage;
		}
	}

	const firstMostly = []; // more common in the first than the second
	const moreCommonIn = (first, second) =>
	first > 4 * second
	for (let word in wordsWithFrequencies[0]) {
		if (!wordsWithFrequencies[1][word])
			firstMostly.push(word);
		else if (moreCommonIn(wordsWithFrequencies[0][word], wordsWithFrequencies[1][word]))
			firstMostly.push(word);
	}

	return firstMostly;
}
