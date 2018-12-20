// team_bogo: Susan Lin and Kenny Liang
// SoftDev1 pd8
// K#29: Sequential Progression II: Electric Boogaloo...
// 2018-12-20

var fib = function(n){
    if (n < 2)
        return n;

    else
        return fib(n-1) + fib(n-2);
}

var gcd = function(a ,b) {
    if ( a < b )
        var c = a;

    else
        var c = b;

    for (var i = c; i >= 1; i--) {
        if (a % i == 0 && b % i == 0)
            return i;
    }
    return 1;
}

var students = ["a", "b", "c"];

var randomStudent = function(){
    var i = Math.floor(Math.random() * 3);

    return students[i];
}

document.getElementById('fib').addEventListener("click", function() {
    console.log(fibonacci(10));
    document.getElementById("paragraph").innerHTML = fibonacci(10);
});

document.getElementById('gcd').addEventListener("click", function() {
    console.log(gcd(10,100));
    document.getElementById("paragraph").innerHTML = gcd(10, 100);
});

document.getElementById('randomStudent').addEventListener("click", function() {
    console.log(randomStudent());
    document.getElementById("paragraph").innerHTML = randomStudent();
});
