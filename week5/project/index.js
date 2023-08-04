let flowers = []
let ID = 1;

function update() {
  document.getElementById('garden').innerHTML = '';
  flowers.forEach((flower) => {
    let node = document.createElement('div');
    node.id = `${flower.id}`;
    node.style = `font-size: ${flower.size}rem`;

    if (flower.healthy) {
      node.innerText = `${node.id} 🌷`;
    } else {
      node.innerText = `${node.id} 🍂`;
    }

    document.getElementById('garden').appendChild(node);
  })
}

function getFlower() {
  let id = document.getElementById('flowerID').value;
  if (id != 0 && id != -1) {
    return flowers.find((elem) => elem.id == id);
  }
  return null;
}

function addFlower() {
  flowers.push({id: ID, size: 1, healthy: true});
  ID++;
  update();
}

function waterFlower() {
  let flower = getFlower();
  if (flower) {
    if (flower.size < 2) {
      flower.size += 0.2;
    } else {
      flower.healthy = false;
    }
    update();
  }
}

function helpFlower() {
  let flower = getFlower();
  if (flower && !flower.healthy) {
    flower.size = 1;
    flower.healthy = true;
    update();
  }
}

function removeFlower() {
  let flower = getFlower();
  let newFlowers = [];
  flowers.forEach((elem) => {
    if (elem.id != flower.id) {
      newFlowers.push(elem);
    }
  });
  flowers = newFlowers;
  update();
}

