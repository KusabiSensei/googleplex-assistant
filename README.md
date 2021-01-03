# googleplex-assistant
This is a connector for IFTTT (and by extension Google Assistant) to send commands to a Plex server on your network, and cast the requested media to a Chromecast.

## Our Principles
We are all adults, and we should all want to help each other out. I'm doing this because I thought this was an interesting
idea, and should try it out.

So if there are disagreements, we should work things out. The best way to work things out is by talking. Maybe there is
something that can be put in the project, maybe there isn't. We won't know until we talk about it. 

Software engineers fix bugs and do awesome things, so with that in mind, the following three bullet points shamelessly lifted
from [Jordan Sissel's fpm project](https://github.com/jordansissel/fpm):

* If something isn't working when you send a request in to the software, then it's a bug.
* Make it work first, then make it right, then make it fast.
* If it doesn't do a thing today, we can make it do a thing tomorrow.

If you need a guiding principle (like MINASWAN), then...

```Be Excellent To Each Other```

## How does it work? 
### (Or more correctly, How do you envision it to work?)
Inspired by [plex-assistant](https://github.com/maykar/plex_assistant), I am looking to remove the dependency upon the
Home Assistant package. This is because I already have a setup where I have Google Home already set up, and I don't need
additional controllers just to be able to talk to my Plex server from Google Assistant.

This is not saying that Home Assistant is bad, rather that it doesn't meet my requirements. That's okay.

I also have a router that supports uPNP and NAT-PMP (so I can dynamically map an external port), and I want to support
the container automatically fetching a certificate from Let's Encrypt based on a DNS01 challenge (HTTP01 challenge would
require the use of port 80)

## What do I need?

All of this is driven off of how my home network is set up, since I want to make it work there first. So far:

* DNS Domain hosted by AWS
* AWS API credentials with permissions to update records in the hosted zone
* A uPNP router
* A local Plex server
* A Chromecast
* A ___Linux___ Docker host (Host Networking is not supported on Docker for Mac, Docker for Windows, or Docker EE for Windows Server)
* IFTTT or DialogFlow

Oh, also Python 3.9 and `pipenv`. The startup shell script is in Bourne shell, so it should work on just about anything
(e.g. `busybox` in Alpine Linux)

## Other documentation

Other documentation about the program can be found in the project wiki.