# Homework assignments for 2016-2017 Bay CS2
For due dates and details of assignments, please see the Bay School community site page for this class!

# How to use git
You are reading this because we have created an organization called "bayCS2", and a repository within that organization called "2016-2017_bayCS2".  You have been invited to be an owner of this repository, so act responsibly.
The homework respository has several "branches", one called "master" and, eventually, one for each student.  If you haven't already, create a branch of master called [yourfirstname].
Open a bash terminal in Cloud9, make sure you are in your workspace directory and execute the following commands.  This creates a "local" version of your branch in your Cloud9 workspace:  
```
git clone https://github.com/bayCS2/2016-2017_bayCS2.git
cd 2016-2017_bayCS2
git branch [yourbranchname]
git checkout [yourbranchname]
git push origin [yourbranchname]   # otherwise, you have only created the branch locally
```
When there are new homework questions in master, or any other changes, e.g., to this README.md file, pull from master to your local branch, and push from your local branch to your branch on GitHub: 
```
git pull origin master
git push origin [yourbranchname]
```
So now you might actually want to do some homework.  If you ...
```
cd ~/workspace/2016-2017_bayCS2/cs61a/hw01
ls
```
... you will see a list of *.py files, one for each assigned question.  Open one for editing using, e.g.:
```
nano Q2.py
```
After you have made edits to Q2.py, push those edits from your local branch to your branch on GitHub :
```
git add -A
git commit -m "Here's my final answer to Q2"
git push origin [yourname]
```
What could be simpler? ;)