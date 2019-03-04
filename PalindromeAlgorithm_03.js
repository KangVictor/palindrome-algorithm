var readline = require('readline');
var rl = readline.createInterface(process.stdin, process.stdout);

function checkPalindrome(b){
	if(b.length == 0 || b.length == 1){// if finished checking
		console.log("True");
		// return 1;
	} else {//if not finished checking
		if(b[0] != (b[b.length - 1])){//wrong
			console.log("False");
			// return 1;
		} else{// if same
			b.shift();//remove first element
			b.pop();//remove last element
			checkPalindrome(b);
			// if (checkPalindrome(b) == 1) {
			// 	return 1;
			// }
		}
	}	
}

rl.question("input text: ", function(answer){
	checkPalindrome(answer.split(''));
});