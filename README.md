# PDF Toolkit - Python app
Simple appplication to merge, split and rotate PDF files.


## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
An application written in Python that allows to merge, split and rotate PDF files. The graphical user interface of the application was created in the PyQT5 Designer app.

## Technologies
Project is created with:
* Python version: 3.10.0
* PyQt5 version: 5.15.7
* PyPDF2 version: 2.11.1

## Setup
1) **Create and activate a virtual environment.**

    **Windows**
    ```
    pip install virtualenv
    python -m virtualenv <your-env>
    <your-env>\Scripts\activate
    ```
    **Mac/Linux**
    ```
    pip3 install virtualenv
    python3 -m virtualenv <your-env>
    source <your-env>/bin/activate
    ```

2) **Clone this repository.**
    ```
    git clone https://github.com/paulinacyran/pdf-toolkit.git
    ```

3) **Go into the repository.**
    ```
    cd pdf-toolkit
    ```

4) **Install all dependencies.**

    **Windows**
    ```
    pip install -r requirements.txt
    ```

    **Mac/Linux**
    ```
    pip3 install -r requirements.txt
    ```

5) **Run the app.**

    **Windows**
    ```
    python PDFToolkit.py
    ```

    **Mac/Linux**
    ```
    python3 PDFToolkit.py
    ```
    
6) **When the application starts, select the tool you want to use - merger, splitter or rotator.**

    ![main-menu](https://github.com/paulinacyran/pdf-toolkit/blob/master/images/main%20menu.png)
           
   **To merge your files:**
    * Select PDF files you want to merge. 
    * Select a location for the new PDF file.
    * Choose a name for the new PDF file.
    * Press 'Merge' button to merge selected files.
    * The new PDF file will be created in the selected location.
    
    ![merger](https://github.com/paulinacyran/pdf-toolkit/blob/master/images/merger.png)
    
   **To split your file:**
    * Select PDF file you want to split. 
    * Select a location for the new PDF files.
    * Press 'Split' button to split selected file.
    * The new files will be created in the selected location. The default name of the new files is PDFfile_1.pdf, PDFfile_2.pdf, PDFfile_3.pdf etc.
    
    ![splitter](https://github.com/paulinacyran/pdf-toolkit/blob/master/images/splitter.png)

   **To rotate your file:**
    * Select PDF file you want to rotate.
    * Select a location for the new PDF file.
    * Select the angle of rotation.
    * If you want to rename the target PDF file, select the 'Yes' button and choose a name for the new PDF file. If you do not want to change the name of the target PDF file, select the 'No' button.
    * Press 'Rotate' button to rotate selected file.
    * The new PDF file will be created in the selected location.
    
    ![rotator](https://github.com/paulinacyran/pdf-toolkit/blob/master/images/rotator.png)
  
   **To select a different tool:**
    * Go back to the main menu: on the toolbar select Menu > Home.
    * Or switch to a different tool: on the toolbar select Menu > Merge PDF / Split PDF / Rotate PDF.
    
    ![toolbar](https://github.com/paulinacyran/pdf-toolkit/blob/master/images/toolbar.png)
    

    
    












