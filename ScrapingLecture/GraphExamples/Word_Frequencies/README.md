# Visualizing the Word Frequencies Count

We got the data from [Counting Word Frequencies](../../../Advanced/count_word_frequency/README.md)

## Method 1: matplotlib

### First attempt: in `ipython` load the data and get some insights in the scale

```python
import json
import matplotlib.pyplot as plt

with open('word_frequencies.json') as infile:
    freqData = json.load(infile)
len(freqData)
freqData[0]
```

> `16573`
> `{u'freq': 1150, u'word': u'whale'}`

```python
l = [w['freq'] for w in freqData]
# plot
plt.plot(l)
plt.show()
# flip diagram in histogram
plt.hist(l)
plt.show()
```

## Method 2: plotdevice

