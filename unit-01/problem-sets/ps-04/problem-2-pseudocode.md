# Problem 2 Pseudocode

* Loop with n = 0 to 27
	* shift ciphertext by n
	* split test decryption on spaces
	* test if all "words" in decryption are in the word list
	* if all words are valid, return n
	* otherwise, test next n