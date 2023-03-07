# Passwords

Using a given word list of 10551 words we can generate long, secure, easy to remember passwords by combining 3 words

```
$ python main.py 
classified reliable bigger 
$ python main.py 
results consecutive sweets 
$ python main.py 
elected incomprehensible hovering 
$ python main.py 
misses device officers
```

## Testing outputs

https://www.security.org/how-secure-is-my-password/
https://bitwarden.com/password-strength/

Even small answers from above such as `misses device officers` will take over 100 years to crack

## Probability

The probability of randomly choosing 3 words from a list of 10551 words and getting a specific combination of 3 words is:

(3/10551) * (2/10550) * (1/10549) = 5.794e-9

## Entropy

> How many bits of entropy are in the password 'misses device officers' ?

To estimate the number of bits of entropy in a password, we can use the formula:

H = log2(N^L)

where H is the number of bits of entropy, N is the size of the character set (i.e., the number of possible characters that can appear in the password), and L is the length of the password.

Assuming that the password "misses device officers" is composed of lowercase letters, uppercase letters, digits, and spaces (i.e., a character set of size 26 + 26 + 10 + 1 = 63), we can calculate the entropy as follows:

H = log2(63^22) ≈ 127.2 bits

This means that the password "misses device officers" has an estimated entropy of approximately 127.2 bits, which is a very strong password. This estimate assumes that the password was chosen randomly from a set of passwords with equal probability, and that an attacker has no additional information that would help them guess the password. However, in practice, the strength of a password also depends on other factors such as the vulnerability of the system where the password is used and the likelihood that an attacker would try to guess the password using various techniques.
