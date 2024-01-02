## Activation Functions

1) Sigmoid:

![Alt text](image-3.png)

**Advantages:**
- Clear prediction either 1 or 0.

**Disadvantages:**
- Prone to vanishing gradient problem
- Function output is not zero centered

Not zero centered output means the function is line not passing through zero.
It does not smoothen the weight updation as the weights get scattered before converging a lot as shown below.

![Alt text](image-4.png)


2) TanH:

The tanH function is given as,

![Alt text](image-5.png)

The derivative of tanH function is given as,

![Alt text](image-6.png)

**Advantages:**
- Zero centered function as the line is passing through zero

**Disadvantages:**
- Time complexity increases
- vanishing gardient problem for deep layer neural network

3) ReLu:

The activation function is given as,

![Alt text](image-8.png)

The derivative of RelU is given as,

![Alt text](image-7.png)


