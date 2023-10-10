<h1>GenPass</h1>

A simple way of generating password as the users requirements. 

<h1>Requirements</h1>

python 3.x

<h1>How to Run the Script</h1>

```
python3 genpass.py len [optional arguments]
```
<h1>Help</h1>

```
python3 genpass.py -h 
```
<br>
usage: generate passwords as required by the user<br>
<br>
positional arguments:<br>
<table>
  <tr>
    <th>len</th>
    <th>define the length of the password</th>
  </tr>
</table>

options:
<table>
  <tr>
    <th>-h, --help</th>
    <th>show this help message and exit</th>
  </tr>
  <tr>
    <th>-u, --upper</th>
    <th>include upper case letters to the password</th>
  </tr>
  <tr>
    <th>-l, --lower</th>
    <th>include lower case letters to the password</th>
  </tr>
  <tr>
    <th>-n, --number</th>
    <th>include numbers to the password</th>
  </tr>
  <tr>
    <th>-s, --special</th>
    <th>include special characters to the password</th>
  </tr>
  <tr>
    <th>-e <characters_to_exclude>, --exclude <characters_to_exclude></th>
    <th>exclude any characters</th>
  </tr>
</table>
