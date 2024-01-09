## Convolutional Neural Network (CNN)

CNN mainly used for image, video related datasets.
ANN can solve the image dataset but cannot get much better accuracy as CNN get.


## RGB & Gray scale channels

In CNN, every image is a combination of 3 color channels.
1) Red
2) Green
3) Blue

![Alt text](image.png)

now in every colorful image in background there are pixels. The pixel value ranges from (0, 256)

In gray scale there is only one channel with (0, 255) pixles.
That pixel value for white becomes 255 and for black the pixel value is 0



## Convolution Operation in CNN:

![Alt text](image-1.png)

Now let's take an above image.
This is a black and white image so the matrix values ranges from (0, 255)
0 means black and 255 means white.

- step1: We will perform min max scaler on this data first to convert all the values within range (0, 1) as min becomes 0 and max becomes 1.
- step2: Now we apply one filter on top of the above matrix.

![Alt text](image-2.png)

Now as shown in the above image, we apply filter on top of the original matrix. Multiply the same values and add all the values.

like for first 3 rows and first 3 columns.
value = 10*1 + 10*0 + 10*-1 + 10*1 + 10*0 + 10*-1 + 10*1 + 10*0 + 10*-1
value = 0

so this 0 will be placed at first place in new matrix

After finding the first place of new matrix we will shift the filter one step right and after all right completed we will shift the filter one step down.

Now like this we will fill all the boxes of new matrix.

Now here in the above image the input matrix is 6*6, filter is 3*3 but output matrix is 4*4.

The formula for output matrix is,

output = no of input - filter + 1
output = 6 - 3 + 1
output = 4