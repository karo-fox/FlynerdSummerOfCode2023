function createNode(tag, content, classes = null) {
  let node = document.createElement(tag);
  node.innerText = content;
  if (classes) {
    classes.forEach(cls => node.classList.add(cls));
  }
  return node;
}

function createUserPanel(user) {
  let node = document.createElement('section');
  node.appendChild(createNode('div', user.first_name + ' ' + user.last_name, ['user-elem', 'user-name']));
  node.appendChild(createNode('div', user.email, ['user-elem', 'user-email']));
  node.classList.add('user-panel');
  return node;
}

async function getUsers() {
  fetch('https://reqres.in/api/users?page=1')
    .then(res => res.json())
    .then(data => data.data.forEach(elem => {
      document.getElementById('get-result').appendChild(createUserPanel(elem));
    }));
}

async function postUser() {
  fetch('https://reqres.in/api/users', {
    method: 'post',
    body: JSON.stringify({
      first_name: document.getElementById('first-name').value,
      last_name: document.getElementById('last-name').value,
      email: document.getElementById('email').value,
    }),
    headers: {
      'Content-type': 'application/json',
    }
  })
    .then(res => res.json())
    .then(data => document.getElementById("post-card").appendChild(createUserPanel(data)));
}
