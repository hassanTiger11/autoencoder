Auto Encoder to drop shodows from pics. In the previous iteration, I used tiff images which required a lot of overhead to convert to processable tensors.
In th

### Data source
I am using data from Cyverse that I downloaded manually. 

## Processing
Process_tiff_img_set.py has a wrapper class that takes in a directory of tiff images and turn them into a dictionary of tensors. 

