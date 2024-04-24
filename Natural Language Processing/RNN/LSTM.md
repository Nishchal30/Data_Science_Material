## Long Short Term Memory (LSTM) RNN

The Traditional RNN looks like below:

![alt text](image-5.png)

The LSTM RNN looks like

![alt text](image-6.png)

**Important reasons why we use LSTM RNN**
1) Whenever we have longer sentences, we need to understand the context switching.
for example:

I like pizza but my friend like ____
Now here we need to predict the word in place of __

- But we have started with I, and we have to predict the word for my friend.
- So here the context is switched, and the model should understand this to predict perfectly.
- So this problem is cannot be solved by RNN, hence we use LSTM RNN.


**The symbolic representation in LSTM**

![alt text](image-7.png)


## **Intution of LSTM**

Let's understand this with example.

Nishchal likes pizza but his friend likes burger.

- Now in this sentence, after passing the words Nishchal, likes, pizza we are changing the context from but.
- So the LSTM should forget the previous input and just remember the new context, to predict the next word.
- Lets understand the architecture layer by layer.

**1) Memory Cell**

![alt text](image-8.png)

- This first line is called as Memory Cell. This memory cell plays a role like conveyer belt.
- You can add information or you can remove information.


**2) Forget Gate Layer**

![alt text](image-9.png)

- This layer is called as Forget Layer cell. Whenever we are changing the context of word and passing that word as input, the forget cell will detect that context change and will inform memory cell to forget the previous information.
- How this can be done? So in our above example, when we pass the word friend, the information from previous neurons does not match with this word, hence the sigmoid activation function will make all the vectors nearer to 0 so that the memory cell will forget the previous information.
- If the information from previous neuron is similar to the current input word, then the sigmoid activation function will make all the vectors nearer to 1, hence the memory cell will keep that information in memory.


**3) Input Gate Layer**

![alt text](image-10.png)

- In this layer, we have two operations one is passing the information with sigmoid activation which is similar to what we saw in Forget Gate layer.
- Another is passing the information with TanH activation function, TanH will convert the values from -1 to 1.
- So from sigmoid activation we will give the vector nearer to 0, if the new context is passing, and nearer to 1 if the context is same.
- Tanh will give the vector with values ranging from -1 to 1.
- After pointwise operation between these two vactors, we will get only new context information, which is the passed to Memory cell to store.
- Here the point wise operation is x, that means we will take dot product of two vectors.
- Whenever we have + in point wise operation we will take addition of two vectors.  


**4) Point wise operations**

![alt text](image-11.png)

- Here we are doing the point wise dot product and addition operation on vectors from previous layers.
- This will decide which information needs to be stored and which information needs to be forget from memory cell.


**5) Output Gate Layer**

![alt text](image-12.png)

- In this layer, the Tanh is applied on the vectors from memory cell, and again the forget layer operation i.e sigmoid applied on the input vectors.
- We do the dot product of this two vectors and will get an output vector.





