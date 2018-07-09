import datetime
import math
import cv2
import numpy as np

#global variables
width = 0
height = 0
CounterEntries = 0
AccountReceiver = 0
AreaLimitMin = 3000  #This value is empirical. Adjust it as required 
ThresholdBinary = 40  #This value is empirical. Adjust it as required
OffsetLinesRef = 80  #This value is empirical. Adjust it as required

#Checks whether the detected body is entering the monitored area
def IntersectionTest(y, CoordinateYLineInput, CoordinateYLineOutput):
    DifferentialAbsolute = abs(y - CoordinateYLineInput)	

    if ((DifferentialAbsolute <= 2) and (y < CoordinateYLineOutput)):
        return 1
    else:
        return 0

#Checks if the detected body is leaving the monitored area
def ForeheadIntersectionExit(y, CoordinateYLineInput, CoordinateYLineOutput):
    DifferentialAbsolute = abs(y - CoordinateYLineOutput)	

    if ((DifferentialAbsolute <= 2) and (y > CoordinateYLineInput)):
        return 1
    else:
        return 0

camera = cv2.VideoCapture(0)

#forces the camera to take resolution 640x480
camera.set(3,640)
camera.set(4,480)

FirstFrame = None

#does some frame reads before consenting the analysis
#Reason: some cameras may take longer to "acuminate the light" when they connect, capturing consecutive frames with a lot of brightness. In order not to bring this effect to image processing, successive captures are made outside the image processing, giving the camera time to "get accustomed" to the brightness of the environment

for i in range(0,20):
    (grabbed, Frame) = camera.read()

while True:
    #first frame and determines image resolution
    (grabbed, Frame) = camera.read()
    height = np.size(Frame,0)
    width = np.size(Frame,1)

    #if it was not possible to get frame, nothing else should be done
    if not grabbed:
        break

    #converts frame to grayscale and applies blur effect (to enhance the contours)
    FrameGray = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
    FrameGray = cv2.GaussianBlur(FrameGray, (21, 21), 0)

    #as the comparison is made between two subsequent images, if the first frame is null (ie first "passed" in the loop), this is initialized
    if FirstFrame is None:
        FirstFrame = FrameGray
        continue

    #absolute difference between initial frame and current frame (background subtraction)
    #in addition, it makes the binarization of the frame with subtracted background 
    FrameDelta = cv2.absdiff(FirstFrame, FrameGray)
    FrameThresh = cv2.threshold(FrameDelta, ThresholdBinary, 255, cv2.THRESH_BINARY)[1]
    
    #dilates the binarized frame, in order to eliminate "holes" / white zones within detected contours. 
    #In this way, detected objects will be considered a "mass" of black color 
    #In addition, it finds the contours after dilation.
    FrameThresh = cv2.dilate(FrameThresh, None, iterations=2)
    _, cnts, _ = cv2.findContours(FrameThresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    ContourQty = 0

    #draws reference lines 
    CoordinateYLineInput = (height / 2)-OffsetLinesRef
    CoordinateYLineOutput = (height / 2)+OffsetLinesRef
    cv2.line(Frame, (0,CoordinateYLineInput), (width,CoordinateYLineInput), (255, 0, 0), 2)
    cv2.line(Frame, (0,CoordinateYLineOutput), (width,CoordinateYLineOutput), (0, 0, 255), 2)


    #Scans all contours found
    for c in cnts:
        #Contours of small areas are ignored.
        if cv2.contourArea(c) < AreaLimitMin:
            continue

        #For purification purposes, count the number of contours found
        ContourQty = ContourQty+1    

        #gets coordinates of the contour (in fact, of a rectangle that can cover the whole contour)
        #and outlines with a rectangle.
        (x, y, w, h) = cv2.boundingRect(c) #x e y: coordinates of the upper left vertex
                                           #w e h: respectively width and height of the rectangle

        cv2.rectangle(Frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        #determines the center point of the contour and draws a circle to indicate
        CoordinateXContourCenter = (x+x+w)/2
    	CoordinateYContourCenter = (y+y+h)/2
    	OutlineCenter = (CoordinateXContourCenter,CoordinateYContourCenter)
    	cv2.circle(Frame, OutlineCenter, 1, (0, 0, 0), 5)
        
        #intersect the centers of the contours with the reference lines
        #dessa forma, contabiliza-se quais contornos cruzaram quais linhas (num determinado sentido)
    	if (IntersectionTest(CoordinateYContourCenter,CoordinateYLineInput,CoordinateYLineOutput)):
        	CounterEntries += 1

    	if (ForeheadIntersectionExit(CoordinateYContourCenter,CoordinateYLineInput,CoordinateYLineOutput)):  
        	AccountReceiver += 1

        #If necessary, uncomment the lines below to show the frames used in image processing
        #cv2.imshow("Frame binary", FrameThresh)
        #cv2.waitKey(1);
        #cv2.imshow("Frame with background subtraction", FrameDelta)
        #cv2.waitKey(1);


    print("Found contours: "+str(ContourQty))

    #Write in the picture the number of people who entered or left the surveillance area
    cv2.putText(Frame, "Entrances: {}".format(str(CounterEntries)), (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (250, 0, 1), 2)
    cv2.putText(Frame, "Exits: {}".format(str(AccountReceiver)), (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("Original", Frame)
    cv2.waitKey(1);


# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()

