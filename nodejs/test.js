const promise = new Promise((resolve, reject) => {
    const number = Math.floor(Math.random() * 12);
    setTimeout(() => {
        number > 4
            ? resolve(number)
            : reject(new Error('Menor a 4'))
        },
        500
    );
});

promise
    .then(
        number => console.log(number)
    ).catch(
        error => console.error(error.toString())
    );