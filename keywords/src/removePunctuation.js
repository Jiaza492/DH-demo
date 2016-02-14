module.exports = (text) => text
	.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g,"") // remove all punctuation
	.replace(/\s{2,}/g," ") // clean up after removing the punctuation
