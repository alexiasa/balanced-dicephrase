---
layout: page
title: Proposal
permalink: proposal/
---

## Background
The “Balanced Dicephrase” generator is a program written in Python that uses the diceware library as a dependency. Diceware is a method for generating passphrases that technically calls for the use of dice rolls as a random number generation mechanism. It has, however, been implemented in multiple languages with popular libraries written in Python, C++, and Go.

I began developing the program with a then-coworker after complaining about my constant typographical errors entering what I described as an “unbalanced” diceware passphrase. It was a long (~30 characters) and memorable passphrase but it was also difficult to type. We decided to write a Python program that would help solve this problem. We assigned values to each key related to distance from the perceived center of a standard QWERTY keyboard. With a large wordlist from online and some free time, we set out to write a basic passphrase generator. We spent about a day on it and I spent a few hours beginning to integrate diceware. The current state is minimally usable but it is in need of many improvements to really be valuable.

The execution of the program (currently) is as follows:
1. Open dictionary and filter words by length to normalize overall passphrase length
2. 5 iterations of passphrase generation and scoring occur (100 phrases per iteration)
3. Passphrases are generated using x words from the dictionary
4. At each iteration, create, score, sort, and remove all but the best scoring passphrase
5. Print the 5 most balanced passphrases

## Objectives
* Improve “Balanced Password” Python program with the following enhancements:
	* Diceware integration (in development)
	* Passphrase length options
	* Delimiter options
	* Wordlist options
	* Solid test suite with continuous integration
	* User-friendly CLI and help
	* PyPi package (in development)

* Compare the time it takes to crack the hashes of passphrases generated with the balanced diceware generator and passphrases generated with the original diceware library. Conduct additional attacks against the phrases themselves. Attempt to determine if there is a notable reduction in entropy due to the balance of the passphrases.

## Experiment

### Constraints
* Use identical source dictionaries
* Use the same passphrase length (8 characters - NIST minimum) and complexity
* Use the same hashing method (simulated NTLM with hashlib)

### Methodology

* Testing hardware:
	* AWS EC2 Linux instance(s) with Elastic GPUs
* Testing method: 
	* Generate 10 passphrases with each method and simulate NTLM hashing on each phrase with the Python hashlib library 
	* Run each list of hashes through Hashcat with Combinator Attack and/or Mask Attack modes
	* Record and compare times to crack hashes from both methods
	* Attack the passphrases (not hashes) using other methods
	* Attempt the same methods with other hash types/complexities/lengths if timeframes and hardware usage costs permit

Project [timeline](/timeline/)

Please check out [Literature Review](/litreview/) or [Bibliography](/biblio) for some analysis into what I'm reading to support my work.


v1.0