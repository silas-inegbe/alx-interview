#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];

async function starwarsCharacters (filmId) {
	const endpoint = 'https://swapi-api.hbtn.io/api/films/' + filmId;
	let response = await (await request(endpoint)).body;
	response = JSON.parse(response);
	const characters = response.characters;

	for (let i = 0; i < characters.length; i++) {
		urlCharacter = characters[i];
		let character = await (await request(urlCharacter)).body;
		character = JSON.parse(character);
		console.log(character);
	}
}

starwarsCharacters(filmID)
