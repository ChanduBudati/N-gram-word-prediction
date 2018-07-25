# NLU

Input – The training data input file- tsdc_test.tct.
The test data will be read from a separate file and processed as indicated below. These file consist of Twitter
messages on the topic of autonomous, self-driving cars. Note: The input data has been cleaned, but may
contain duplicate or incomplete tweets. Furthermore, given the limited number of characters allowed per
tweet, messages may contain misspellings, abbreviations, and improper grammar. The verbiage is the
responsibility of the original authors of the tweets.
• Processing – The processing requirements include:
• Each line in the file is considered a sentence. N-grams should be extracted at the line/sentence level,
and should not crossover line boundaries. Some lines may in fact contain more than one sentence, but
should be handled as a single sentence.
• Lines/sentences should be stripped of commas, semicolons, colons, periods, question marks, and
exclamation points.
• The data structure used to hold the tokens/words (likely a list) should be augmented with the special
start sentence symbols, as required for each n-gram.
• The extracted bigrams and trigrams must be kept in separate data structures (dictionaries work well
here), and must include the special sentence delimiter markers. To avoid having very large but sparse
data structures, only n-grams that are encountered are entered into the data structures.
• Once the n-grams have been extracted, the test file will be read for testing. A single word per
line/sentence will be randomly selected for prediction (the random seed should be set to 1000 at the
beginning of the main function). The first attempt will be to match using trigrams. If this fails, bigram
prediction is used. If no prediction is possible with either trigrams or bigrams, a match failure is
declared. DO NOT USE SMOOTHING FOR ZERO N-GRAM COUNTS. Counts should be maintained of
correct predictions, incorrect predictions, and failed predictions.
• Output – The program should display the following output:
• The number of bigrams and trigrams extracted
• The number of correct, incorrect, and failed predictions
