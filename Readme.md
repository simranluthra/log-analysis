# Introduction
Project - Log Analysis

The database includes three tables:

1. The authors table includes information about the authors of articles.
2. The articles table includes the articles themselves.
3. The log table includes one entry for each time a user has accessed the site.

# Readme file consists of:
- Prerequisites.
- Getting Started.

# Prerequisites
- Python
- Vagrant
- Virtual Box

#Getting Started        

## Instructions On How TO Run The Given Project:
- Install Vagrant and Virtual Box.
- Download or Clone fullstack-nanodegree-vm repository.
- Download the data.
- unzip this file.
- Put the file `newsdata.sql` into the vagrant directory.


## Setting up the Virtual machine:

  - Launch the Vagrant inside Vagrant directory using command: $ vagrant up
  - Then Log into this using command: $ vagrant ssh
  - Change directory to cd /vagrant and look around with ls.

## Setup Database

  - Load the database using command `psql -d news -f newsdata.sql`
  - Use psql -d news to connect to database.
  - Create the following view in order to successfully run third query.
	```
	CREATE VIEW bad_status as
	SELECT date(time) as Date,
	round(100.0*sum(
	    case status
	    	when '404 NOT FOUND'
	    	then 1
	    	else 0
	    end)/count(status),1)
	as percentage_error
	FROM log
	GROUP BY Date;
	```

## Running the queries
  - $ python log.py

## RESULTS
The file `log_output.txt` contains the results of the queries.
