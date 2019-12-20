# Hadoop-program-for-word-count
Hadoop program for word count in many input files


Environment Setup:

I Install VMware Workstation to set up virtual machines (VMs).
I installed ubuntu ISO file on VMware workstation. 

HADOOP Problem:
-------------------------------
Description of the design:
-------------------------------

The program has more than one step. So I used MRStep that return list of steps. The step mapper_init initializes the array that contains for each file the list of unique words in file. The step mapper puts unique words in a file to the check array. The step mapper_final will map words in each file to one (i.e., each word in check array which contains unique word in a file). The step reducer_final finally adds the values for each key(i.e., each word). So it counts the number of files the word is in.

Installation of Hadoop:
-----------------------

Installing Java-
helena@ubuntu:~$ sudo apt-get update
helena@ubuntu:~$ sudo apt-get install default-jdk
helena@ubuntu:~$ java –version

Adding a Hadoop User-
helena@ubuntu:~$ sudo adduser --ingroup hadoop hduser

Installing SSH:
It is used to connect remote machine.
helena@ubuntu:~$ sudo apt-get install ssh

Install Hadoop:
hduser@ubuntu:~$ wget http://mirrors.sonic.net/apache/hadoop/common/hadoop-2.6.0/hadoop-2.6.0.tar.gz
hduser@ubuntu:~$ tar -xvzf hadoop-2.6.0.tar.gz
hduser@ubuntu:~$ sudo mv hadoop-2.6.0 /usr/local/Hadoop




Install Hadoop single node cluster.

To start the single node cluster:
helena@ubuntu: ~$ cd /usr/local/hadoop/sbin
helena@ubuntu:/usr/local/hadoop/sbin$ sudo su hduser  
hduser@ubuntu: ssh localhost
hduser@ubuntu:~$ start-all.sh



 
Assuming the PATH:
 export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar

Compile wordCountProgram.py by running the below command:
hduser@ubuntu:~$ $ python wordCountProgram.py -r hadoop hdfs://my_home/input1.txt input2.txt input3.txt


input1.txt input2.txt, etc are the input files to the program.

 
SPARK PROBLEMS:
--------------------

SPARK INSTALLATION:
--------------------

Install java and check the version
java -version

I installed Anaconda and Pyspark to do the spark program in python

python --version


Download Spark from website and extract it.
The downloaded file is spark-2.4.0-bin-hadoop2.7.tgz
I extracted the files in the location C:\Users\helen\Desktop
So, all spark files will be in the path C:\Users\helen\Desktop\spark-2.4.0-bin-hadoop2.7

I opened Anaconda Prompt, changed to directory to C:\Users\helen\Desktop\spark-2.4.0-bin-hadoop2.7
 And typed bin\pyspark

I created directory hadoop\bin inside C:\Users\helen\Desktop\spark-2.4.0-bin-hadoop2.7

I created system environment variables SPARK_HOME that has the path
C:\Users\helen\Desktop\spark-2.4.0-bin-hadoop2.7

I downloaded winutils.exe and saved in the Hadoop/bin folder



I created system environment variables SPARK_HOME that has the path
C:\Users\helen\Desktop\spark-2.4.0-bin-hadoop2.7



I created system environment variables HADOOP_HOME that has the path
C:\Users\helen\Desktop\spark-2.4.0-bin-hadoop2.7\hadoop

 

In anaconda prompt I installed pyspark by
python -m pip install findspark command

I started spark standalone cluster by following commands:

To start master:
In command prompt go to directory C:\Users\helen\Desktop\spark-2.4.4-bin-hadoop2.7\sbin and type
spark-class org.apache.spark.deploy.master.Master

To start slave:
spark-class org.apache.spark.deploy.worker.Worker spark://169.254.124.97:7077

where 169.254.124.97 is the IP address of master.

Go to  http://localhost:8080/ this will give the cluster details.

Description of the design:
-------------------------------


FOR PROBLEM 1:
---------------- 

In the review data set. We should find reviews with more than 100 words in reviewText and group by overall key. Print this in an output file.
 
I loaded the data a json format. Created a variable and put the contents in review.data. I filter the data by comparing the reviewText word count to greater than 100. If it is greater than 100 than I ‘groupby’ the key ’overall’ and stored it in a variable and printed the output into a text file. The path I used for the input and output files is C:\Users\helen\Desktop\sparkhomework. This path should be changed in program accordingly when run on different system. The output is printed in the folder Outputreview.

I ran the python code in Jupiter Notebook as it supports Pyspark

FOR PROBLEM 2:
---------------

We should calculate the average number of words in each review that belong to Music category. 

The meta.data contains asin and categories field. Review.data contains asin and reviewText. So primary key is asin.

I take a read to files meta.data and review.data and out in two variables.
     
I join both files with a key field asin as its common in both files.Now I filter only reviews with category “Music”. I count the words in each record under the field “reviewTest”.

I take average of all the word count.

The output is 94.27.


I ran the python code in Jupiter Notebook as it supports Pyspark







