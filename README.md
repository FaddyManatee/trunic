# trunic
Translate between English and Trunic - A runic language from the game TUNIC.

This is a work in progress python module and currently only supports
english to trunic translation without symbols or punctuation.

Output methods include trunic to png, or an encoded string that the trunic font
can render appropriately, though the former is not yet reliable.

## Credit
TUNIC font (aka Trunic) in `src/trunic.otf` courtesy of Adrián Jiménez Pascual 
([dirdam.github.io](https://dirdam.github.io)) which is [available here](https://github.com/dirdam/fonts).

## Usage
To convert english text to trunic:
```python
from trunic import Trunic

my_str = Trunic("Humans are endowed with reason and conscience and should act toward one another in a spirit of brotherhood")

print(my_str.to_ipa())
>>> '/hjumənz ɑɹ ɛndaʊd wɪð ɹizən ænd kɑnʃəns ænd ʃʊd ækt tɔɹd wən ənəðɝ ɪn eɪ spɪɹət əv bɹəðɝhʊd/'

print(my_str.get_phonemes())
>>> [['h', 'j', 'u', 'm', 'ə', 'n', 'z'], ['ɑɹ'], ['ɛ', 'n', 'd', 'aʊ', 'd'], ['w', 'ɪ', 'ð'], 
['ɹ', 'i', 'z', 'ə', 'n'], ['æ', 'n', 'd'], ['k', 'ɑ', 'n', 'ʃ', 'ə', 'n', 's'], ['æ', 'n', 'd'], 
['ʃ', 'ʊ', 'd'], ['æ', 'k', 't'], ['t', 'ɔɹ', 'd'], ['w', 'ə', 'n'], ['ə', 'n', 'ə', 'ð', 'ɝ'], 
['ɪ', 'n'], ['eɪ'], ['s', 'p', 'ɪɹ', 'ə', 't'], ['ə', 'v'], ['b', 'ɹ', 'ə', 'ð', 'ɝ', 'h', 'ʊ', 'd']]

# The resulting string could be printed on a website with src/trunic.otf font.
# src/test.py generates a simple web page that outputs a CLI string argument in trunic (see below image). 
print(my_str.encode())
>>> 'hyumanz car ne_daud widh riizan nae_d konshans nae_d shxd kae_t tord wan na_dha_cxr ni_ cei spirta_ va_ bradhxrhxd'
```
<img src="https://cdn.discordapp.com/attachments/810862843620098099/1100570041902182410/image.png">
