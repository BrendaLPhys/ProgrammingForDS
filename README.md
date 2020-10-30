# Numbers in text
> This is a test library


This is a practice library that contains functions that work with a text file and help analize the text by obtaining numeric values that describe it. 

## Install

`pip install numbers_in_text`

## How to use

Here are some examples:

```python
File = open("regex_sum_928284.txt", 'r')
text = File.read()
File.close()
```

#### Function number_sum finds all numbers within a text and gives back the sum

```python
number_sum(text)
```

    The total is: 390829
    

#### Function lettermax finds the letter that was used the most in the text and the number of times it was used. 

```python
lettermax(text)
```

    The letter used the most is:  e , it was used used:  2548  times.
    

#### Function numwords counts the number of words in the text.

```python
numwords(text)
```

    Total number of words is: 28510
    
