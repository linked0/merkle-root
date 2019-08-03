# Implementing Merkle Tree in Python

[//]: # (Image References)

[treeImage]: ./tree_structure.png "Hash Tree Structure"

## Merkle Tree coding challenge
[Requirements Details](https://geod24.github.io/infrastructure/)


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for testing purpose.

### Python version
It runs on any version of Python 2.7 or newer.

### Getting source files from the github
Open Terminal and get the source files

```
git clone https://github.com/linked0/merkle-tree.git
```
### Running the script
Go to perkle-tree/python directory and run Python script
```
cd merkle-tree/python
python merkle.py "The quick brown fox" "jump over" "the" "lazy dog"
```
You can get the result as follows.
```
Level 0:
018FB04252A594A8049CBFE9E34848249040E1FA7E170501E17ADC06393D4DC3
Level 1:
836C2FE675884DB41C49215F8A91E6560B1EA752F683DB793E9B86180CA235F8
49B9A6B1346DC768898A16C2DAD9D554349C9150F8B2809AC7D48B305C4D3650
Level 2:
7743034D22491720B723B68AFD046BE66969409254DC79A153E290C81A8F238A
F51DF418D9D7BAFDCFDC4320409E08E39858D0D686FEE959EA545E6D7C214F71
1E7C521A055F0F08CEA3FADED5923CCA2D8F4366A62AAA8A8B843A842AA656B8
144BEE93D8F6350C6E38C96EEB11DE2CD249A7BD5D23FF4C91EB46573B5AF3BA
```

## Data structure and implementation in Python
![alt text][treeImage]