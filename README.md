# Dynamic-NAT-using-Netmiko
Dynamic NAT using Netmiko 


![alt tag](https://github.com/OthmaneBlial/Dynamic-NAT-using-Netmiko/blob/master/Tutorial/1.PNG)

We create three files, one for data, one for configuration and another one for showing results. These files need to be excutable.

![alt tag](https://github.com/OthmaneBlial/Dynamic-NAT-using-Netmiko/blob/master/Tutorial/2.PNG)

Let's add information to data.py about Router 1 and Router 2:

![alt tag](https://github.com/OthmaneBlial/Dynamic-NAT-using-Netmiko/blob/master/Tutorial/3.PNG)

Let's create these two functions which will help us to retrieve a subnet mask and also a wild card mask:

![alt tag](https://github.com/OthmaneBlial/Dynamic-NAT-using-Netmiko/blob/master/Tutorial/4.PNG)

Now, let's define these five function, which will configure an interface, a default route, a NAT interface, an ACL, 
and then Dyanmic NAT:

![alt tag](https://github.com/OthmaneBlial/Dynamic-NAT-using-Netmiko/blob/master/Tutorial/5.PNG)

Now, we configure R1 with the following configuration:

![alt tag](https://github.com/OthmaneBlial/Dynamic-NAT-using-Netmiko/blob/master/Tutorial/6.PNG)


Then R2: 

![alt tag](https://github.com/OthmaneBlial/Dynamic-NAT-using-Netmiko/blob/master/Tutorial/7.PNG)

And we run these two functions:

![alt tag](https://github.com/OthmaneBlial/Dynamic-NAT-using-Netmiko/blob/master/Tutorial/8.PNG)


