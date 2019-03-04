function isPalindrome(a){ //check if the String a is a palindrome. returns string test "true" if so.
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

var readline = require('readline');
var rl = readline.createInterface(process.stdin, process.stdout);
console.log("input text: ");
rl.on('line', (line) => {
	if (line.toLowerCase() === 'q') rl.close();

  if (isPalindrome(line)) {
  	console.log(`"${line}" is a palindrome :-)`)
  } else {
  	console.log(`"${line}" is not a palindrome :-(`)
  }

	console.log("input text: ");
});
