// this is the script that finds keywords in a sample of text

const removePunctuation = require("./removePunctuation");
const usageDiff = require("./usagediff");
const normalWords = require("./data/normal.json");
const reviewWords = require("./data/reviews.json");

const keywords = usageDiff([reviewWords, normalWords]);
console.log(keywords);

const isIn = (array) => (elem) => array.indexOf(elem) !== -1;

const keywordsIn = (text) => text
	.split(" ")
	.map(removePunctuation)
	.map((word) => word.toLowerCase())
	.filter(isIn(keywords))

module.exports = keywordsIn;
