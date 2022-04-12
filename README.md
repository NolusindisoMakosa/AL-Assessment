# AL-Assessment
AL python Assessment 

#Question 1
- There is a missing statetement to declare counter as global

#2
- The output of the test is pass. The value needed to change to inc(4) 

#3
A simple python to calculate the total time it takes to hit a website

#4
How to create the docker Image for the python script


#Linux
1. Install Git
2. install Docker
3. Create a custom script (e.g /q3solution.py)
 - Run the script using $ python3 q3solution.py
 - The output of the script should display the time is it took to his the specified websites.
 - To check a different website, edit array in  the script (q3solution.py)
	- in the URL variable add and website of your choice from 
		
#Create a docker image
4. To Create Dockerfile (e.g /Dockerfile) (Using VS code)
	- Open a new file
	- select the filetype as Dockerfile
	- Add the environent variables
	- Define the image type. [for this docker file I chose python]
	- Make a working directory of the container [I created directory / App]
	- Copy the script into the container. Use [COPY . /]
	- Define the entrypoint, execute the python command ["python",<script_name>]
	- run $  docker build . [This is will run ]
	- Do not forget the "." at the end which set to build context to the current directory
	 - Don't forget to run at the directory of the project

6. Allow it to install the dependencies defined.
7. Once it's done, check the docker images
	$ docker images
8. Test if the image created is is running
    $ docker run pytheonimage
 
