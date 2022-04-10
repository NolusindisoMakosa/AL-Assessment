# AL-Assessment
AL python Assessment 

#How to create the docker Image for the python script

#Linux
1. Install Git
2. install Docker
3. Create a custom script (e.g /q3solution.py)
4. Create Dockerfile (e.g /Dockerfile)
	-  Define the image type
	- Make a directory of the container
	-  Copy the script into the container
	- Define the entrypoint
	
5. Build the image
	- docker build . -t <name_of_the_image>

6. Allow it to install the dependencies defined.
7. Once it's done, check the docker images
	- docker images
8. Test if the image created is is running
	- docker run <image_name>