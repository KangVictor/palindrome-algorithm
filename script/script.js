const palindromeModel = [];

		function palindromeSuccess(word) {
			// add word to palindromeModel
			// write palindromeModel to textarea
			palindromeModel[palindromeModel.length] = word
			myText.innerHTML = palindromeModel;
		}

		function palindromeFailure(word) {
			// warn user
			alert(`${word} is not a palindrome`);
		}
		// get a reference to the form
		const form = document.querySelector('#submit-words');
		// get a reference to the textarea
		const myText = document.querySelector('#MyTextArea');
		// listen for submit event
		form.addEventListener('submit', (event) => {
			// prevent the default behavior
			event.preventDefault();

			// get the word from the input
			const word = form.querySelector("[name=words-input]").value;

			// pass the word to our palindrome function
			const isPalidrome = checkPalindrome(word);

			if (isPalidrome) {
				// update UI
				palindromeSuccess(word);
			} else {
				// warn user
				palindromeFailure(word);
				console.warn(`${word} is not a palindrome`);
			}
		});