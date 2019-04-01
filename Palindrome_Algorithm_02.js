function checkPalindrome(a){ //check if the String a is a palindrome. returns string test "true" if so.
	var b = a.split('');// split the string into array of char

	for(var n = 0; n < b.length/2; n++) {
		if (b[n] != b[b.length - n - 1]) {
			return false;
		}
	}
	return true;
}