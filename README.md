#Python SVO Extractor using NLTK
A small SVO extractor written in Python for the great library NLTK.

## Installation/Dependencies

If you are on Mac you can install Stanford Parser *using brew install stanford-parser* as depicted here: http://nlp.stanford.edu/software/lex-parser.shtml#Download

Else use this description to install and use the Stanford Parser for NLTK here https://github.com/nltk/nltk/wiki/Installing-Third-Party-Software

`python setup.py install`

Either remove the first two rows in svo.py

```
os.environ['STANFORD_PARSER'] = ''
os.environ['STANFORD_MODELS'] = ''
```
AND set env variables 
```
export STANFORD_PARSER="<stanford-parser-path>"
export STANFORD_MODELS="<stanford-models-path>"
```

OR

just set 

```
os.environ['STANFORD_PARSER'] = ''
os.environ['STANFORD_MODELS'] = ''
```

to the appropriate values.
## Usage


```
from svo.svo import SVO`

svo = SVO()
```


## Other
Alpha version, so it might not be the best implementation.
Rewritten from https://github.com/pradeep-gnr/SVO_Extractor to be able to run it
without jython.