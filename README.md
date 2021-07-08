# Chronic Kidney Disease Prediction

## CONTENTS OF THIS FILE
1. [Purpose of the project](#purpose-of-the-project)
2. [Software files](#software-files)
3. [Project files](#project-files)
4. [Important Links](#important-links)
5. [Project Execution Steps](#project-execution-steps)

### 1. Purpose of the Project
***
The goal is to build a real time application by using the machine learning techniques, to detect the CKD at an early stage. 

### 2. Software files
***
* Python >= 3.8
* Flask >=2.0.0
* scikit-learn >= 0.24.2
* numpy >=1.20.3
* pandas >=1.2.4
* matplotlib >=1.4.8
* openpyxl >=3.0.7
* sklearn >=0.0
* xlrd >=2.01

### 3. Project files
***
1. Colab Files
	1. Copy_of_ckd (.ipynb)
	2. Copy_of_ckd (.py)
	3. kidneydataset (.csv, Original dataset)
	4. new (.csv, new dataset after data augmentation)
	5. data-augmentation (.py)

2. User-Interface Files
	1. templates (folder, which consists of html pages - homepage2.html)
	2. static (folder, which consists of css files)
	3. dataset1 (comma seperated text file, which contain all the columns)
	4. dataset2 (comma seperated text file, which contain only selected the columns)
	5. proj2 (.py file, contains the code for user interface or flask file)

### 4. Important links
***
The below links are used for finding installation commands.
* NumPy - https://numpy.org/install/
* Pandas - https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html
* scikit-learn- https://scikit-learn.org/stable/install.html
* Flask - https://flask.palletsprojects.com/en/2.0.x/installation/

### 5. Project Execution Steps
***
1. Create a folder and place dataset1.txt,dataset2.txt,proj2.py files in it.
2. Create a folder with name templates in the previous folder.
3. Place the homepage2.html file in templates folder.
4. Open command prompt and Set the location where the python file (proj2.py)  is located
5. Run the python (proj2.py) file
6. Click on the link generated
7. Paste it on the browser and Enter the values and click on the predict button
8. The output is displayed
