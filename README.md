# MCQ_Scanner
Analyzes an image of a questionnaire, automatically encodes it in excel and is imported in a Quiz App ( Quizizz ). This is done with Optical character recognition and Computer vision in Python. Saves time in manually encoding hundreds of Questions for studying or creating Question banks. 

# How to use the python script?
First you need to gather images of multiple choice questions and then simply process them in the script.
 
### Gathering Questions
Any Multiple choice question image with this format. <br />
If the questions comes from books its much better to scan them 
for better image quality.

 <br  />
 <br  />
 <br  />

![Sample Question](/Sample%20Images/format_mcq.JPG) <br />

 <br  />
 <br  />



You can **combine multiple questions** using any photo editor or using Paint. <br    />
For online questions just copy paste it in word then you take a screenshot <br  />
similar to the image below.<br  />
 <br  />
 <br  />
![Sample Question](/Sample%20Images/testImage.JPG)

 <br  />
 <br  />

# How does the python script work?
The code works in just **3 steps** <br  />
 <br  />
**1. Processes the image using OpenCV** <br  />
Our goal is to tell python to separate or differentiate the questions from the answers. <br  />
Using functions in  OpenCV it loads, dilates, thresholds and adds bounding boxes to the image. <br  />
![Output Image](/Image%20Proccesing/image%20with%20bounding%20boxes.JPG) <br  />
 <br  />
 <br  />
**2. Extracts the questions and answers** <br  />
using pytesseract a optical character recognition (OCR) tool for python to <br  />
convert the images to texts. <br  />
 <br  />
![Extracted Question](/Image%20Proccesing/ROI_1.png) <br  />
 <br  />
![Extracted Question](/Image%20Proccesing/ROI_0.png) <br  />
 <br  />
 <br  />
 
 **3. Encoding in Excel** <br  />
I used the xlsxwriter module in python to encode the texts to excel. <br  />
 <br  />
![Excel](/Image%20Proccesing/ExcelOutput.JPG) <br  />
 <br  />
 <br  />
 
# Limitations
As you use this script you may find limitations in the following: <br  />
 <br  />
**1. Image Proccesing** <br  />
According to what I've experience this is due to low quality images, wrong format ( you can observe this at the output ROI images) or incorrect parameters in the code for the image. I've coded this with a specific format in mind and will further improve this so that the code is not "static" and maybe apply AI to differentiate the questions from the answers. 
 <br  />
 <br  />
**2. Incorrect conversion of text** <br  />
As you can see in my output excel image. There are some text's that are not understandable and this is due to the image quality or there are special symbols in the image. <br  /> 

**3. Encoding Issues** <br  />
This issue arises from choices having long text's , it does not encode the entire choice in a certain cell in excel. <br  />
See example image below <br  /> 
![Sample Question](/Sample%20Images/Limitations1.JPG) <br />
 <br  />
 <br  />
 as you can see letter **a** occupies two lines of the image this will cause issues in the encoding






