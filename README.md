# text-summarizer-testing
Informal fork of @Imeulen's [SummarizeText](https://github.com/lmeulen/SummarizeText) Repo

## Getting started:
1. Clone the [repo](https://github.com/DavidRodrii/text-summarizer-testing):
```
git clone https://github.com/DavidRodrii/text-summarizer-testing

```

2. Install the python dependencies via `requirements.txt`:
```
cd text-summarizer-testing
python -m pip install -r requirements.txt
```

3. Download NLTK Data

Follow the NLTK Data download steps on: [https://www.nltk.org/data.html](https://www.nltk.org/data.html)

* Run python interpreter followed by the commands:
```
import nltk
nltk.download()
```

4. Run the python test code with the command:
```
python -m test-summarizer.py

```

5. Compare Results between the `input.txt` and `output.txt` files:

* `output.txt` is generated by the test code
* `input.txt` can be modified with any long block of text


## Appendix

### SummarizeText - Python Class Usage:

A Python class to generate a summary for a given text or text file.

Usage:
```
summ =  Summarizer(language='dutch', summary_length=3)
# or (defaults to dutch, summary length of 3:
summ =  Summarizer()

# Initialize manualy
summ.set_language('dutch')
summ.set_summary_length(3)

# Or detect language to use
summ.detect_language(text)

# Summarize a text
print(summ.summarize("..."))
# Summarize the contents of a text file
print(summarize_file('longtext.txt', split_at=250))
```
For more information, see:
* [Summarize a text in Python](https://towardsdatascience.com/summarize-a-text-with-python-b3b260c60e72?sk=9d66f3557b7f41b4e7eae1688c5b8120) on Medium

