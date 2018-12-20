// team_3_members - Jack Lu, Joyce Liao, Susan Lin
// SoftDev1 pd8
// K28 -- Sequential Progression
// 2018-12-18

var fib = function(n){
    if (n < 2){
        return n;
    }
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

var students = [
    "a", "b", "c"
];
var randomStudent = function(){
    var i = Math.floor(Math.random() * 3);

    return students[i];
}
