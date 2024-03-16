## Object Detection 

In object detection our aim is to define where the object is in the image.
So where means we have to find out the location or co-ordinates of the object from that image.

**Object Detection always comes with image classification and regression problems**
like object = classification + regression

- classification will tell us what type of object it is
- Regression will tell us where the object is located in an image.

So to find co-ordinates the axis is always +ve on both x & y sides
Like the origin is top left corner of image, and down the line through y-axis is +ve y-axis and right side of origin is +ve x-axis.

![alt text](image.png)

In the above image the different rectangles define the different bounding boxes. Each bounding box refer to an single object in the image.

Now to create a bounding box we need to know the location of object and to know location we have to know the co-ordinates of object. Hence predicting the co-ordinates means number become regression problem.

So to create a rectangle we will always require 4 points:
a) either (x1, y1) & (x2, y2)
b) or midpoint with (x, y) and height & width (h, w)

**Predicting this co-ordinates is the main aim in object detection, which the conventional CNN cannot do, as softmax activation function cannot predict the regression problem**

## Why do we always use rectangle to detect and object and not circle?

So the idea behind the rectangle is that we want to minimize the background noise in the bounding box.

If we compare the rectange of height 20 and width 80, so the centre point will be 40.
Now if we try to draw circle of radius 40 it will be much bigger than the rectangle so it will contain more background noise than rectangle.

And also we can stretch the height or width of rectangle as per the object, that cannot be done with the help of circle.



## Bounding Box Regression

Now we have the Ground truth points which are the actual co-ordinates of the boundig box and the predicted co-ordinates of bounding box.

- We will use here L2 Loss to check the accuracy of our predicted co-ordinates.
- The difference  between ground truth and predicted co-ordinates should be minimum.
- So the model should predict the co-ordinates in such as way that the loss value should be minimum


## Metrics in Object Detection

1) Intersection Over Union (IOU):
The area of intersection between the two bounding boxes is called IOU

The formula is given as,
![alt text](image-1.png)

0 < IOU > 1 ; 0 is worse and 1 is perfect.

- If the IOU is 0, then it means the predicted boundix box is not overlapping with the Ground Truth i.e. actual bounding box of object
- Hence the more IOU, the better object is detected.


2) Confusion Matrix:

**The confusion matrix in Object Detection**

![alt text](image-2.png)

So in object detection we uses classifiaction + regression, so classification score is given as confidence score. The higher the confidence score it means it is predicted what object it is in ground truth correctly.


3) Average Precision:

**Interpolation Method**

In this we average precision value with either all points or through only specific number of points.

![alt text](image-3.png)


![alt text](image-4.png)





