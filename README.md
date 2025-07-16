# CTF Lab: Extract Database Names via Union-Based SQL Injection in MySQL

## Description
In this lab, you'll exploit a classic union-based SQL injection vulnerability in a simulated e-commerce PHP webapp to enumerate the underlying MySQL database names using information_schema.

## Objectives
- Detect and exploit SQL injection in numeric input.
- Enumerate original query column count and columns echoed in output.
- Craft UNION-based SQLi payloads using information_schema.schemata.
- Enumerate all database names and submit them as the challenge flag.

## Difficulty
Intermediate

## Estimated Time
30-45 minutes

## Prerequisites
- Basic SQL and SQL injection knowledge
- Familiarity with HTTP requests and web proxies
- Basic Linux command line
- Burp Suite or similar proxy (optional: sqlmap familiarization)

## Skills Learned
- Information_schema enumeration
- Manual SQL injection exploitation
- Identifying injectable parameters
- Paginating UNION SELECT injection outputs

## Project Structure
- folder:src
- folder:docker
- folder:docs
- file:README.md
- file:.gitignore

## Quick Start
**Prerequisites:** Docker and Docker Compose installed.

**Installation:**
Clone the repository. Run `docker-compose up --build` in the lab root directory. Access the vulnerable webapp at http://localhost:8080.

## Issue Tracker
https://github.com/Cyber-Library/issues 