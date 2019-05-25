# Aptoide - Python Challenge

## Autocomplete API

You are asked to implement an Autocomplete API that helps users searching for apps by
their name. When writing the name of an app, the possible results should be shown to
the user. For example, if the user is inputting *Fac*, two possible choices are
*Facebook* and *Facebook Lite*.

The challenge is composed of 2 main components:

* The autocomplete system
* An API (a microservice/web service) that receives a query and returns the possible
results for that query

The autocomplete system can be seen as a composition of 2 subcomponents:

* A data structure to store the possible words (the corpus). This data structure
should enable quick lookups of words.
* A search algorithm that given the above data structure and a query, should
output the possible words

The microservice/web service should be simple enough as to just receive as input a
user query, ask the autocomplete system for the possible results and send them back.


## What we expect to receive from you

When you are ready to submit your answer to this challenge, you should set up a
public GitHub repository with everything we ask below:

* The autocomplete system
* The API to query the autocomplete system
* Set up a virtual machine environment using **docker-compose** to run the test 
task including some short documentation
* **Automated tests** covering as much of the code as possible
* **Documentation** with instructions regarding how to set up the system and how
to test it
* Please build the application in small logical steps and commit each step to
 a **Github** repository so that we can see how you approach the task


## Important remarks

* The challenge should be done using **Python**
* The corpus (i.e. possible words that the autocomplete system can output) of the
autocomplete system is **set in the setup/loading time** and remains **unchanged during runtime**
* The autocomplete system can have a **high setup/loading time** but should be **very fast at runtime**
* It is more important to have **less code and have it completely tested** with automated
tests than to have a **lot of code without automated tests** to ensure its quality


## Helpers

* We're providing 2 corpus in the [*test_files*](./test_files) directory with different sizes that can be used for testing
* Regarding the autocomplete system's data structure, search for **Trie** and **Tree-like data structures**
* As for the autocomplete system's search algorithm, search for **BFS/DFS algorithms**
* For the API and web server, read about **Flask** (Python module)
* For the automated tests, read about **unittest** (Python module) and
**docstrings**
