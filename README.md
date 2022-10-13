# Attendance-And-Surveillance-System
Attendance &amp; Surveillance System using Face Recognition.

This is an ‘Attendance Monitoring & Surveillance System’ which monitors the attendance with the help of face recognition. 
It is written in python and it has 3 different files, one for training, one for both surveillance and face recognition and one for uploading the attendance to Google Spreadsheet. 
Each file contains the basic instructions to run the program properly and each file clearly describes how the program works.
	

**All the three files should be kept in the same folder!!**
  
  
First, run the train.py file:
1.  Make a folder named **faces** to store images.
2.  Make folders inside the above created folder and **name** them. **This name should be the name of the person.**
3.  Store **above 100 images** of faces of **each person** to the folders created.
4.  Download the ‘**face_detector.xml**’ file from this repository.
5.  **Install cv2** library.
6.  Assign the **path** of the **faces** folder to the variable **DIR**.
7.  assign the **path** of the ‘**face_detector.xml**’ to the variable **haar_cascade**.
8.  **Run** the file.
9.  You will get the **face_trained.yml** file by running this.
	
  
  
Second, give required values to the uploading.py file:
1.	**Watch** https://youtu.be/4ssigWmExak and follow the instructions.
2.	Give your **Spreadsheet id**
3.	Give your **Service Account Key**



Third, run the detection.py file:
1.  Make a folder named ‘**video**’.
2.  Give the **path** to **face_trained.yml, face_detector.xml and path to video folder**.



The program is **ready** to run.
1.  Open **detection.py** an **run**.
2.  After recognising all the faces, the **attendance** will be **uploaded** to the **Spreadsheet**.



**ENJOY**

---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---
