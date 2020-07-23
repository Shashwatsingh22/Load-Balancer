<img src=images/main.png></img>
<b>I have completed my DOCKER  project which is based on the Load Balancer…..
    Lets Take you in depth of LOAD BALANCING:------------------------</b> 

<h2>What is  Load Balancing ?</h2>
   <img src=images/jo.jpg height=200px width=700px></img>
<h3>Let Here is the two containers (A and B) which have same clients and also 
providing services but as; Client 1  Wants to access that services then 
it render to the container A….When Client 2 Access the same service then 
it redirected to the container B ….After some time Client 3  come and access
that same  service  then he redirected to container A…… 
<b><i>So, This Whole process is know as Load Balancing.</b></i> 
<h2>
Why we need load balancing ?
</h2>
<h4>
We need Load Balancing to maintain the loads on the server.
</h4>
<h2>Usage:</h2> 
 <h4>
 Lets take an Example of the Google …
 So ,Google have thousand ‘s of webserver or thousand’s of IP’s and all the IP’s 
 What are they have those are put exactly same in website ! But as we are  the client
 we never type the different-different type of the IP of the GOOGLE !!
 We just go on the Browser and search directly for (www.google.com) . 
Now the whole scenario will use only one type of the system called LOAD-BALANCER.
When we  type (www.google.com) so, we directly hit  the google internal 
LOAD BALANCER & Balancer will maintain there System of load……    
For the Load Balancing we have many ALGORITHMS but the famous one is ROUND ROBIN….
    </h4>
    <h2>
        Implementation
    </h2>
    <img src=images/main1.png></img>
    <h4>
But Here In this project, without the use of any software or Devices I used an 
trick of DNS Server(This will work as Load balancer for us) ..
First I created  our own Docker Network with use of the Driver called BRIDGE….. 
and Lunch those CMS under this NETWORK …. And under 
this network we have also attach every WebApp Containers with the 
same Database which is storing data in every single bit… We have also done one thing that 
without knowing the hostname or IP’s of our webserver or container we have provided one unique name 
and our client will connect by the help of that unique name  and  that unique name will update the DNS. 

Now Clients Have There Have three Choices : 
1.	They can connect by the that unique name (network-alias).
2.	They can connect by the HOSTNAME.
3.	They can connect by the IP:Port No.  
</h4>

<h2> Now Lets See How you can use this project ? </h2>
<pre><p> First Clone This Project From the GitHub by the Command .....
<b> $ git clone https://github.com/Shashwatsingh22/Load-Balancer.git </b></p></pre>

<pre><p> How to Run this ?....
<b> $ python3 main.py </b></pre></p>

<pre><p><b> Now You Can Easily Proceed Your Work Easily.... </b></p></pre>
