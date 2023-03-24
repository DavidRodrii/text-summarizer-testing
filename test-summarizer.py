
# Sources: 
# https://github.com/lmeulen/SummarizeText
# https://towardsdatascience.com/summarize-a-text-with-python-b3b260c60e72
# https://towardsdatascience.com/summarize-a-text-with-python-continued-bbbbb5d37adb
# AT&T Job Description: https://soft.jobs/posts/1

from SummarizeText import Summarizer

# Define Summarizer() Class
summ = Summarizer()

# Read in File input.txt
out = summ.summarize_file('input.txt', encoding="utf-8", split_at=20, summary_length=1)

# Print Summarized Contents 
print(out)

# Write Ouput to File output.txt
with open("output.txt", "w") as text_file:
    text_file.write("%s" % out)


