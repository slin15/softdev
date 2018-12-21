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

//document.getElementById('fib').addEventListener("click", function() {
//    console.log(fibonacci(10));
//    document.getElementById("paragraph").innerHTML = fibonacci(10);
//});
//
//document.getElementById('gcd').addEventListener("click", function() {
//    console.log(gcd(10,100));
//    document.getElementById("paragraph").innerHTML = gcd(10, 100);
//});
//
//document.getElementById('randomStudent').addEventListener("click", function() {
//    console.log(randomStudent());
//    document.getElementById("paragraph").innerHTML = randomStudent();
//});

// Lo, what is this? Could it be a VALUE-ADDED-KEY2SUCCESS?!?!

var changeHeading = function(e) {
    var h = document.getElementById("h")
    h.innerHTML = ???
};

var removeItem = function(e) {
 ???
};

var lis = document.getElementsByTagName("li");

for(var i=0; i < lis.length; i++) {
    lis[i].addEventListener('mouseover', ???);
    lis[i].addEventListener('mouseout', ???);
    lis[i].addEventListener('click', ???);
};

var addItem = function(e) {
    var list = ???;
    var item = document.createElement("li");
 ??? = "WORD";
 ???
 ...
 ???
 list.???( item );
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n) {
    if(n < 2){
        return 1;
    } else {
        return fib(n-1) + fib(n-2);
    }
};

var addFib = function(e){
    console.log(e);
 ???
 ...
 ???
};

var addFib2 = function(e){
    console.log(e);
 ???
 ...see QAF re: DYNAMIC PROGRAMMING...
 ???
};

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
