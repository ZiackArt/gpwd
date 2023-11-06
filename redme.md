<p align=center>
  <span>Gpwd: Password Combination Generator</span>
  <br>
</p>

<p align="center">
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#usage">Usage</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

## Installation

```console
# clone the repo
$ git clone https://github.com/ZiackArt/gpwd.git

# change the working directory to gpwd
$ cd gpwd

# install the requirements
$ python -m pip install -r requirements.txt
```

## Usage

```console
$ python gpwd -h
Run GPWD.
$ python3 gpwd -h
GPWD Passwords Combination Generator
Parameters
----------
`-h`  : to display Helps
`-v`  : to have a runing version of gpwd
`-a`  : to generate a Arangement 
`-c`  : to generate a Combination
`-k`  : (Optional) to give the number of digit (4 by default)
`-w`  : (Optional) to Arangement or Combination with replacement
`-o`  : (Optional) to give output file name ( put nan to use default name)
Good use
----------
Author : ZiackArt
GitHub : https://github.com/ZiackArt
```

To generate a Arangement with ouptup file:
```
python gpwd -a -o result.txt
```

To generate a Combination of 5 with replacement:
```
python gpwd -c -w -k 5
```

## License

Gpwd Project<br/>
Original Creator - [Ziack Art](https://github.com/ZiackArt)