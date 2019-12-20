# Hadoop-program-for-word-count
Hadoop program for word count in many input files


Environment Setup:

I Install VMware Workstation to set up virtual machines (VMs).
I installed ubuntu ISO file on VMware workstation. 


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

 




