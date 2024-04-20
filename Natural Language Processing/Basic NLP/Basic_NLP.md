## Natural Language Processing

The NLP is required where we are handling text data. It is the part of Deep Learning.


**Roadmap of NLP**
1) Text Preprocessing - Convert text or sentences into numerical format to understand the model.
(Tokernization, Lemmetization, Stemming, Stopwords)
2) Text Preprocessing 2 - Convert text or sentences into numerical format to understand the model
(Bag of Words, TF-IDF, Unigrams, Bigrams)
3) Text Preprocessing 3 - Convert text or sentences into numerical format to understand the model
(Word2Vec, AvgWord2Vec)
4) Deep Learning - RNN, LSTM RNN, 
5) Advanced Text Preprocessing - Word Embeddings
6) Advanced Deep learning - Bidirectional LSTM, Encoders, Decoders, Attention models.
7) Transformers
8) BERT



## Basic Preprocessing Techniques

1) Tokenization:

Let us consider an example to predict the email is Spam or Ham.

We will predict the spam or ham based on email body, email subject.
So for this we will need to convert the words into number so there are various techniques for this.

**Tokenization converts sentence into words.**


2) Stopwords:
**Remove the words which are repeated and does not have much meanings in problem statement.**
The words like The, is, of, he, she etc. We can remove this words from the sentences.


3) Stemming:
Find out the base stem of any word or root word.

historical 
history 

Both the words are have same context and if we apply stemming on this we will get a word histori.
**Stemming reduces the words to its base word, but it may not have any meaning.**
As histori is meaningless word.

Advantages:
1) It is fast

Disadvantage:
1) Removing the meaning of word.

**Usecases:**
1) Spam Classification
2) Review Classification


4) Lemmetization:
We will convert a word to its base word but we will get a meaningful word.
as exa we will get a base word as history for above example.

Advantages:
1) It is slow

Disadvantage:
1) Meaning of word is maintained.

**Usecases:**
1) Text Summarization
2) Language Translation
3) Chatbot


## Basic Terminologies used in NLP

1) Corpus :- Corpus is nothing but the Paragraph, or the complete text data.
2) Documents :- Sentences from the Corpus.
3) Vocabulary :- Number of unique words of the corpus.
4) Words :- Each and every word in the corpus.


