import os
from pyfiglet import Figlet
#from os import system,path

def render(text,style):
	f=Figlet(font=style)
	print('\n'*1)
	print(f.renderText(text))
os.system("tput setaf 1")
render('LOAD Balancer','sblood')
os.system("tput setaf 7")

os.system("tput setaf 2")
render('\t by Shashwat Singh','digital')

while True:
	os.system("clear")
	os.system("tput setaf 1")
	render('LOAD Balancer','sblood')
	os.system("tput setaf 5")
	print("""
		Press 1: Pull the image (Content Manegement System) (Choose and Install)
		Press 2: Pull the image (For the Database) (Choose and Install)
		Press 3: SetUp Your Environment.
		Press 4: Deploy Your Services.
		Press 5: Introduction about (How Your Client can Get Access To Your Services ?)
		Press 6: Exit
		""")
	print("Enter Your Choice: ",end=" ")
	os.system("tput setaf 7")
	ch=input()
	if int(ch)==1:
		while True:
			os.system("clear")
			os.system("tput setaf 1")
			render('LOAD Balancer','sblood')
			os.system("tput setaf 3")

			print("""
				-----------------------------------Welcome To SetUp Your WebApp Images -----------------------------------
				                         ----------------Select the CMS------------------
				""")
			os.system("tput setaf 7")
			os.system("tput setaf 6")
			print("""
				Press 1: Joomla
				Press 2: WordPress
				Press 3: Drupal
				Press 4: Back
				""")
			os.system("tput setaf 7")
			print("Enter Your Choice: ",end=" ")
			ch1=input()
			
			if int(ch1)==1:
				os.system("docker pull Joomla:3.9-php7.2-apache")
			elif int(ch1)==2:
				os.system("docker pull wordpress:5.1.1-php7.3-apache")
			elif int(ch1)==3:
				os.system("docker pull drupal:latest")
			elif int(ch1)==4:
				break
	if int(ch)==2:
		while True:
			os.system("clear")
			os.system("tput setaf 1")
			render('LOAD Balancer','sblood')
			os.system("tput setaf 3")
			print("""
				-----------------------Welcome To Setup Your DataBase----------------
				""")
			os.system("tput setaf 6")
			print("""
				Press 1: MySQL
				Press 2: Back
				""")
			os.system("tput setaf 7")
			print("Enter Your Choice: ",end=" ")
			ch1=input()
			os.system("tput setaf 7")
			if int(ch1)==1:
				os.system("docker pull mysql:5.7")
			elif int(ch1)==2:
				break

	elif int(ch)==3:
		while True:
			os.system("clear")
			os.system("tput setaf 1")
			render('LOAD Balancer','sblood')
			os.system("tput setaf 3")
			print("""
				---------------Welcome To SetUp Your Environment----------------
				""")
			os.system("tput setaf 6")
			print("""
				Follow the Steps:
				   Step 1:Lets Create Our Own Network
				   Step 2:Create The Volume/Storage For the CMS and DATABASE
				   Step 3: Back
				""")
			os.system("tput setaf 7")
			print("Enter Your Choice: ",end=" ")
			ch1=input()
			if int(ch1)==1:
				print("Enter The Name of Your Network: ",end=" ")
				net_name=input()

				os.system("docker network create --driver bridge {0}".format(net_name))
				print("""----->>>>Successfully You Have Created Your Network.<<<<<-------
					These List of your Own Network: 
					""")
				os.system("docker network list")
			elif int(ch1)==2:
				print("""
					>>>> For making our environment as persistent/permanent we need make the storage
					     To collect the data from the server....
					     Enter the Suitable-name for your Storage: 
					     """)
				dock_storage_name=input()
				os.system("docker volume create {0}".format(dock_storage_name))
				print("Here the List of your Volume: ",end=" ")
				os.system("docker volume ls")
			elif int(ch1)==3:
				break
	
	elif int(ch)==4:
		while True:
			os.system("clear")
			os.system("tput setaf 1")
			render('LOAD Balancer','sblood')
			os.system("tput setaf 6")
			print("""
				Press 1: First Deploy the Database to Store the data.
				Press 2: Secondly Deploy the WebApp.
				Press 3: Back
				""")
			os.system("tput setaf 7")
			print("Enter the Choice: ",end=" ")
			ch1=input()
			if int(ch1)==1:
				while True:
					print("""
						Choose An Image For the Database: 
						  Press 1: MySQL
						  Press 2: ......
						  """)
					print("Enter Your Choice: ",end=" ")
					ch2=input()

					if int(ch2)==1:
						print("Choose the Root Password and Enter Here: ",end=" ")
						root_pass=input()
						print("Enter the name of the USER: ",end=" ")
						user_name=input()
						print("Enter the Password for this USER: ",end=" ")
						user_pass=input()
						print("Give The name to your Database: ",end=" ")
						db_name=input()
						print(">>>If u don't know about your docker storage name (choose form here): ")
						os.system("docker voulme ls")
						print("Enter the Name of Docker_storage:  ",end=" ")
						db_os_name=input()
						print("Give the name to your container(this name will be used to link): ",end=" ")
						nam_cont=input()
						os.system("docker run -dit -e MYSQL_ROOT_PASSWORD={0} -e MYSQL_USER={1} -e MYSQL_PASSWORD={2} -e MYSQL_DATABASE={3} -v {4}:/var/lib/mysql --name {5} mysql:5.7".format(root_pass,user_name,user_pass,db_name,db_os_name,nam_cont))
						break
					elif int(ch2)==2:	
						print("Check That Here container is running or Not: ")
						os.system("docker ps -a")
			elif int(ch1)==2:
				while True:
					print(""" 
						Choose an image for the WebApp: 
						Press 1: WordPress
						Press 2: Joomla
						Press 3: Drupal
						""")
					print("Enter Your Choice: ",end=" ")
					ch2=input()
					if int(ch2)==1:
						print("""----IMPORTANT NOTE (Give The Informataion Same as the DATABASE IMAGE)
							Enter the Host Name (Host Name means the name of the DATABASE CONTAINER NAME)""")
						host_name=input()
						print("Enter DB USER NAME: ",end=" ")
						user_name=input()
						print("Enter DB USER Password : ",end=" ")
						user_pass=input()
						print("Enter DB name: ",end=" ")
						db_name=input()
						print("These are the Local Storage which you have made choose from here : ")
						os.system("docker volume ls")
						print("Storage Name For this WebApp Image: ",end=" ")
						dock_storage_name=input()
						print("Give the name to for this image: ",end=" ")
						db_os_name=input()
						print("Give the Network Alias Name: ",end=" ")
						net_alias_name=input()
						print("""
							Enter the Network name from this given list(This list shows that Local Networks That You Have Ctreated)
							------------------>>>> Give This Same Network to Which You Have made For load <<<<<<-----------------------------------
							                       Load Balancer                                          
							""")
						os.system("docker network ls")
						net_name=input()
						os.system("docker run -dit -e WORDPRESS_DB_HOST={0} -e WORDPRESS_DB_USER={1} -e WORDPRESS_DB_PASSWORD={2} -e WORDPRESS_DB_NAME={3} -v {4}:/var/www/html --link {0} --network-alias {5} --network {6} -p 8080:80 --name {7} worpress:5.1.1-php7.3-apache")
						break
			elif int(ch1)==3:
				break
	elif int(ch)==5:
		while True:
			os.system("clear")
			os.system("tput setaf 1")
			render('LOAD Balancer','sblood')
			os.system("tput setaf 3")
			print("""
				>>>>>>>>>>>>>>>>>>>--- Module For Access This SetUp ---<<<<<<<<<<<<<<<<<<<<
				""")
			os.system("tput setaf 6")
			print("""
				Now, As we SetUp Everything. Lets See the Steps ......................
				           (How our Client Can Acess these Services ?) 
				Now, These Whole Scenerio we made on The Load Balancer.........
				  Client Should be the Part Of this Network for this Type Scenerio.
				  Now, Client Have Choic to access by: 
				     ------>>> By the Alias Name
				     ------>>> By the Host Name(Container Name)
				     ------>>> By the IP:Port Number
				""")
			os.system("tput setaf 7")
			input("Press Any Key To ..................")
			break
	elif int(ch)==6:
		break

