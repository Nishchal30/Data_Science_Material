We have techniques to fine tune the pre-trained large language models, which we can do in our GPU's RAM.

Below are the techniques for fine-tuning:

# **1) Quantization:**
Quantization means conversion of model weights/parameters from higer memory format to a lower memory format.

Exa:- Llama 2 has 70B parameters, so it's almost impossible to fine tune 70B parameters in our local.
so what we can do, if suppose the paramaters are stored in int32 bits, then we can convert this into int8 memory format.
so it will take less memory in RAM to perform the tasks.

So this process is called as quantization.

<img width="519" alt="image" src="https://github.com/user-attachments/assets/aa7c5568-0870-402c-945b-5def55fd795a" />

Advantages of Quantization:
1) Lower bit width results in less memory for storage
2) This is due to efficient computation due to its lower memory bandwidth requirements
3) Can quantize to suit the need and deploy to device with samller hadware specifications.

Disadvantages of Quantization:
1) Potential loss in accuracy due to squeezing of high precision weight to lower precision.

**This squeeing process from higher numbers to lower numbers is called as calliberation**

# **Modes of Quantization**
1) Post Training Quantization: In this we will do calliberation or squeezing after the LLM model is trained, so we will take the pre-trained model first, then we will apply this calliberation and then use that quantized pre-trained LLM model for our use.

2) Quantization-Aware Training: In this we will not quantize the model, we will use as it is, but instead we will use fine-tuning. So the calliberation and quantizatiom will be done during the fine-tuning process itself. So here will will not loose any data hence we will not loose any acuraccy of model

<img width="535" alt="image" src="https://github.com/user-attachments/assets/91e2d741-7d47-4fae-903a-b1821c1fc432" />
