const ROOT_URL = "https://swapi.dev/api";

let moviesData = fetchData("films");
let planetsData = fetchData("planets");
let charactersData = fetchData("people");

async function fetchData(type) {
  let result = await fetch(`${ROOT_URL}/${type}/`)
    .then((res) => res.json())
    .then((data) => data.results);
  console.log(result);
  return result;
}

function moviesPage() {
  moviesData
    .then((res) =>
      res
        .sort(
          (movieA, movieB) =>
            Date.parse(movieA.realease_date) - Date.parse(movieB.release_date)
        )
        .reverse()
        .map((movie) => createMovieCard(movie))
    )
    .then((cards) => populateContent(cards));
}

function planetsPage() {
  planetsData
    .then((res) => res.map((planet) => createPlanetCard(planet)))
    .then((cards) => populateContent(cards));
}

function charactersPage() {
  charactersData
    .then((res) => res.map((character) => createCharacterCard(character)))
    .then((cards) => populateContent(cards));
}

function createMovieCard(movieData) {
  let node = createNode("section", "", ["card", "card-content"]);
  node.appendChild(createNode("h2", movieData.title, ["sub-heading"]));
  node.appendChild(createNode("div", "Directed by " + movieData.director, ['week-description']));
  node.appendChild(createNode("div", new Date(movieData.release_date).toDateString(), ['week-description']));
  return node;
}

function createPlanetCard(planetData) {
  let node = createNode("section", "", ["card", "card-content"]);
  node.appendChild(createNode("h2", planetData.name, ['sub-heading']));
  node.appendChild(createNode("div", "terrain: " + planetData.terrain, ['week-description']));
  node.appendChild(createNode("div", "climate: " + planetData.climate, ['week-description']));
  return node;
}

function createCharacterCard(characterData) {
  let node = createNode("section", "", ["card", "card-content"]);
  node.appendChild(createNode("h2", characterData.name, ['sub-heading']));
  return node;
}

function createNode(tag, content, classes) {
  let node = document.createElement(tag);
  node.innerText = content;
  classes.forEach((cls) => node.classList.add(cls));
  return node;
}

function populateContent(cards) {
  document.getElementById("results").innerHTML = "";
  cards.forEach((card) => document.getElementById("results").appendChild(card));
}

moviesPage();