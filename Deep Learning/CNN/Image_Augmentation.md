## What is Data Augmentation?

When we have less number of data to train our deep learning model, then we need to generate more images from the images that we already have.
So this type of data generation is called as Data Augmentation.

In this data generation, we add images with slightly modified copies of already existing data.

## Methods of Data Augmentation

We have multiple checkpoints on which we perform the data augmentation.

1) Rotation: Rotate the original image
2) Blur: Blur the original image
3) Contrast: Make contrast color changes in image.
4) Scaling: Scale down or up (zoom) the image
5) Illumination: Illuminate the image
6) Projective: Make the projective look to image 


## Framework for Data Augmentation

1) imgaug
2) Augmentor
3) Albumentation


## Batch Normalization

We do normalization at the start of our deep learning network, like we divide the input image with 255 as that is the max pixel value. So in short we do Normalization for input layer of network.

But in the training of network the inputs get multiplied with weights or kernels and that kernels are randomly initialised. SO when we multiply normalized inputs with unormalized weights then it becomes unormalized again.

So to avoid this we use batch normalization layer before every layer so that the output of previous layers get normalized and then sent to next input layer

    