# Results

## Task 1.1

### Task 1.1A
Running the script with root priviledges the attacker is able to sniff all the packages exchanges by the victims, in our examples the victims pinged google.com. While by running the script using a non-root user the program throws a Operation not permitted exception.**live demonstration**

### Task 1.1B
We can set the filter with "host <IP> and tcp port 23", as the IP we used 10.9.0.5 and since telnet uses port 23 we tried contacting the host B at 10.9.0.6 with the command `telnet 10.9.0.6 23`. The attacker was able to capture these packets. **live demonstration**

## Task 1.2
`tcpdump -w /tmp/packets -v icmp`
**live demonstration**

## Task 1.3
**live demonstration**

## Task 1.4
fix 10.9.0.99 with arp spoofing
**live demonstration**

## Task 2.1

### Task 2.1A Question 2
We need to execute the program as root because we interact with the promiscuous mode and the network devices to listen to the traffic. Without it we get a "Segmentation fault (core dumped)". **live demonstration**

### Task 2.1A Question 3
Setting the mode to "not promiscuous" the program is still working and able to sniff the network because of our configuration which is not using promiscuous mode at all, instead is set to "host mode" on docker. As a matter of fact, the promiscuity in the attacker VM is set to 0. **add screenshot**

### Task 2.1B
**live  demonstration**

### Task 2.1C
**live demonstration**
