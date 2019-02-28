function checkPalindrome(a){ //check if the String a is a palindrome. returns string test "true" if so.
	var b = a.split('');// split the string into array of char

	if(b.length % 2 == 0) {// if even number of letters
		for(var n = 0; n < b.length/2; n++) {
			if (b[n] != b[b.length - n - 1]) {
				return 'false';
			}
		}
	} else{// if odd number of letters
		for(var n = 0; n < (b.length + 1) / 2; n++) {
			if (b[n] != b[b.length - n - 1]) {
				return 'false';
			}
		}
	}

	return 'true';
	
}
//var input = [];

var readline = require('readline');
var rl = readline.createInterface(process.stdin, process.stdout);


rl.question("input text: ", function(answer){
	console.log(checkPalindrome(answer));
});

//}
//checkPalindrome(answer);
		//input[0] = checkPalindrome(answer);
//for(var n = 0; n < 3; n++) {
	//console.log(input[n]);
//}
