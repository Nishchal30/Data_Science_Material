We have techniques to fine tune the pre-trained large language models, which we can do in our GPU's RAM.

Below are the techniques for fine-tuning:

1) Quantization:
Quantization means conversion of model weights/parameters from higer memory format to a lower memory format.

Exa:- Llama 2 has 70B parameters, so it's almost impossible to fine tune 70B parameters in our local.
so what we can do, if suppose the paramaters are stored in int32 bits, then we can convert this into int8 memory format.
so it will take less memory in RAM to perform the tasks.

SO this process is called as quantization.

<img width="519" alt="image" src="https://github.com/user-attachments/assets/aa7c5568-0870-402c-945b-5def55fd795a" />
