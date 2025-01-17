## 1)**LORA** (Lower Order Rank Adaptation)

LORA is used for fine-tuning of a pre-trained LLM model. So in fine-tuning generally we have to update all the parameters/weights used in that model.
for exa: if any model has used 175B parameters while training, then we have to update all 175B parameters while fine-tuning.
so this is very resource extensive work to do which involves a lot of cost.

**What does LORA do?**
Instead of updating all the weights, it will track the changes of the new weights based on fine-tuning. So what we will do,

pre-trained weights + LORA tracked weights = fine-tuned weights

Now we may say, this LORA tracked weights will again be the all parameters so how can we solve the resources issue.
So here LORA uses Matrix Decomposition method.

It will split the LORA tracked weights matrix into two smaller rank matrix.
So hence this two matrices will always smaller than the LORA tracked matrix, hence it is much effective for resources.

<img width="593" alt="image" src="https://github.com/user-attachments/assets/ba7ecc6c-c0e1-4dc1-86f7-9b80794ae76d" />


**Interview Question**
1) When should we use high rank?
So whenever we want to solve complex things, or whenever our model is not able to learn some complex pettern of data, then we use higher ranks.


The below image shows, that from 175B parameters from GPT3 model, how we reduced using LORA
<img width="638" alt="image" src="https://github.com/user-attachments/assets/5af8ee57-a4b3-4868-941b-eee2df616fc9" />


# **2)QLORA (Quantized Lower Order Rank Adaptation)**

So in this, we will quantize the model weights, like if our model had used float 16 bit data, so this will convert it into float 4-bit.
Hence it will take less memory to run, and further LORA is applied.


