# AL-Assessment
AL python Assessment 

#Question 1
The is a missing stateteme to declare counter as global

#2
- The output of the test is pass. The value needed to change to inc(4) 

#3
A simple python to calculate the total time it takes to hit a website

#4
How to create the docker Image for the python script and Recreate the output


#Linux
1. Install Git
2. install Docker
3. Create a custom script (e.g /q3solution.py)
 - Run the script using $ python3 q3solution.py
 - The output of the script should display the time is it took to his the specified websites.
 - To check a different website, edit the script
		- in the URL variable add and website of your choice from 
		
#Create a docker image
4. To Create Dockerfile (e.g /Dockerfile) (Using VS code)
	- Open a new file
	- selecte type as Dockerfile
	- Add the environent variables
	- Define the image type 
	- Make a directory of the container
	-  then Copy the script into the container
	- Define the entrypoint
	- run $  docker build --tag pytheonimage .
	 - Do not forget the "." at the end which set to build context to the current directory
	 - Don't forget to run at the directory of the project

6. Allow it to install the dependencies defined.
7. Once it's done, check the docker images
	$ docker images
8. Test if the image created is is running
    $ docker run pytheonimage
 