let books = [];
let globalID = 1;

function displayBooks() {
  document.getElementById("library").innerHTML = '';
  books.forEach((book) => {
    let bookNode = document.createElement("div");
    let title = book.title.length < 40 ? book.title : book.title.slice(0, 40) + "..."
    bookNode.innerText = "{" + book.id + "} " + title + '\n' + book.author;
    bookNode.className = "book vertical"
    document.getElementById("library").appendChild(bookNode);
  })
}

function addBook() {
  let title = document.getElementById("title").value;
  let author = document.getElementById("author").value;
  let publisher = document.getElementById("publisher").value;
  let year = document.getElementById("year").value;
  books.push({id: globalID, title, author, publisher, year});
  globalID++;
  displayBooks();
}

function deleteBook() {
  let id = document.getElementById("id").value;
  let idx = books.findIndex((book) => book.id == id);
  if (idx != -1) books.splice(idx, 1);
  displayBooks();
}