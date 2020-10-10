const multiply = (a, b) => {
    let res = 0;
    for (i = 0; i < a; i++)
        res += b;
    return res;
}
const a = multiply(2, 4);
console.log(a);