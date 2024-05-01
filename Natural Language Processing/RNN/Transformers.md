## **Transformers**

Transformer can convert the machine language translation from one language to other.

The transformer model consist of encoders and decoders.
The input sentence is given to encoder, and we get the tranlated sentence after decoder.

- In the encoder block, we have multiple encoder and decoder layers. As in the below image.

![alt text](image-15.png)

- Inside the encoder, we have two layers again one is self-attension layer and other is feed forward neural network which is similar to ANN.
- Self-attension model is very important here.

- The input of sentence is converted to embeddings using word embedding methods like Word2Vec.
- The each word of the sentence will get converted into some fixed dimensions.

![alt text](image-16.png)

As in the above image, the converted vectors are then passed to the self-attension layer.
- The all words of a sentence are passed at same time unlike the RNN, in RNN we pass one word at a time.


## **What are self-attension layers**

Let's see this with an example

The animal didn't cross the street because it was too tired

**Now in the above sentence, what the it is referring to?**

As converting this english sentence to some other language, the model should know this it is refering to animal or street or something else, to convert the sentence properly.

- The below steps are performed first whenever the word is given to the self-attension layer.
- We create 3 weights matrices, and multiply the input vectors with the 3 weight matrices.
- With these multiplications we will get queries, keys, and values matrices.

![alt text](image-17.png)


- The next step is we will create scores by multiplying the queries with keys of all the words, like given in below image.
- This score is calculated with multiplication of queries and keys to find the word is related or not, as we need to find out the word it is referring to what?

![alt text](image-18.png)

- In next step, we will divide the score with the square root of dimensions used.
- And then apply softmax activation function on top of this square root value.
- We will apply the softmax to decide whichever feature has the highest probability values out of 1.

![alt text](image-19.png)

- In the next step, we will multiply the values matrix created above with the softmax score.
- And we will add the multiplication for the words, to get final vector.

![alt text](image-20.png)

- The z1 for word thinking will be the output of self-attension model and z2 will be the output of 2nd word. These outputs then passed as input to Feed Forward Neural Netwrok.

- **If we use the same matrix of Wq, Wk, Wv for all the wordsthen it is called as single-head attension model.**
![alt text](image-17.png)

- And if we use different weights for different words, then it is called as multi-head attension model.
- IF we use single-head attension, we may not capture the reference of word like what the it word is referring to. We may not get accurate result as it will give the highest weightage to one of the word like 'animal' but what if the it word is referring to the 'street' actually.
- For this we have to use multi-head attensions.

![alt text](image-21.png)

- We will get something like given in above image if we use multi-head attension.
- When we use more heads, we will get more z values.
- So we will combine the all the z matrix, and multiply again a new matrix with the concatenated matrix of all z.
- So we will get the final one Z matrix, which is them passed to feed forward neural network.


## **Positional Encoding**

- The ordering of words is very important when it comes to th refernece of any word.
- SO to maintain the order of words, we use positional encodings.
- Which will find the distance between the word embeddings, and create a matrix out of that.
- This positional encodings are placed right after the input embeddings and before passing it to encoders.
- SO the embedding vector and positional embeddings are added to form 'embedding with time signal' vectors.
- And this 'embedding with time signal' vectors are then passed to encoders.


## **Residual Layer**

In residual layer, which is also called as Add & Normalize layer, we can skip the self-attension layer if needed and directly pass the inputs to this layer.

As given in below image.

![alt text](image-22.png)


**The final combined architecture will looks like**

![alt text](image-23.png)

- The output of the encoders layer is connected to every decoder, and in decoder also we have almost same architecture as encoders.
- Threr is additional one layer in decoder as Encoder-Decoder Attension, which takes the input from encoders in all decoders layer.
- As we pass the input of all words at a time, but the output will produces word by word at a time.
- SO the output of first decoder will be passed to the self-attension layer of decoder as input along with the output of encoders, the two outputs of decoders then passed as input to decoders to predict third word, and so on.
- We will apply first linear activation function and then we will perform softmax activation function.



## **Different types of transformer architectures**
1) Encoder only
2) Decoder Only
3) Encoder-Decoder

**1) Encoder Only:**
There are many Encoder only models, we will see each of them as below

1) BERT
- First encoder only model is BERT based on transformer architecture.
- BERT is used in use cases like Text classification, NER(Named Entity Recognition)
- BERT is (Bidirectional Encoder Represntations from Transformers)
- BERT is trained on Masked Language Modelling (MLM) and Next Sentence Prediction (NSP)

2) DistilBERT:
- DistilBERT is lightweight model of BERT.
- It's less memory consuming yet fast performing model.

3) RoBERTa
- Robustly Optimized BERT Pre-training Approach.
- This is trained on longer sentences than BERT and on more data.
- It drops the NSP training objective of BERT.

4) XLM
- Improved version of BERT
- XLM is widely used for cross-lingual language tasks, like text classification and machine translation.
- XLM is trained on Translation Language Modelling (TLM) which is an extended version of Masked Language Modelling (MLM).

5) XLM-R (combination of XLM, and RoBERTa)
6) ALBERT
7) ELECTRA
8) DeBERTa



**2) Decoder Only:**
There are many Decoder only models, we will see each of them as below
Decoder models are mostly used for text generation tasks, which is mainly used by OpenAI.

1) GPT (Generative Pre-trained Transformers)
- GPT is trained for predicting the next word based on the previous words.

2) CTRL (Conditonal Transformer Language)
- GPT is used to autocomplete an input sentence, but the user has no control on the format of generated sentences.
- CTRL solves this issue by introducing "control tokens" at the begining of sequence.

3) GPT-2 (Successor of GPT)
- GPT-2 can produce long sequences and also trained on more data than GPT.

4) GPT-3 (Successor of GPT-2)
-  GPT3 is much more refined version of GPT-2 as it is trained on more data, and the accuracy also increased.



**3) Encoder-Decoder models**

1) T5 (Text-to-text transfer Transformer)
- The T5 combined the NLU (Natural Language Understanding) and NLG (Natural Language Generation) tasks.

2) BART (Bidirectional Auto-regressive Transformers)

3) M2M 100 
- M2M 100 is the first model which is capable for converting the text into 100 languages, while other model supports only one language translatation.

4) BigBird
