function rng(max) {
    return Math.floor(Math.random() * max);
}

function run() {
    let number = rng(10);
    for (let i = 0; i < 5; i++) {
        let guess = prompt("✨ Podaj liczbę całkowitą ✨")
        
        if (guess == number) {
            alert("🎉 Gratulacje, udało ci się! 🎉 \nPoszukiwaną liczbą było: " + number + "\nUdało ci się za " + (i + 1) + " razem!");
            break;
        }

        if (guess < number) alert("Za mało!");
        if (guess > number) alert("Za dużo!");
    }
}