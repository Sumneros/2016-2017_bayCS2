# homework
For due dates and details of assignments, please see the Bay School community site page for this class!

# How to use git
You are reading this becuase we have created an organization called "15-16bayCS2", and a repository within that organization called "homework".  The homework respository has several "branches", one called "master" and one for each student.  If you haven't already, ask a git-maven to create a branch of master called [yourname].  Open a bash terminal on your laptop, navigate to your Documents directory and execute the following commands to create a local version of your branch on your laptop:  
```
git clone https://github.com/15-16bayCS2/homework.git
cd homework
git branch [yourname]
git checkout [yourname]
git pull origin [yourname]
```
When there are new homework questions in master, or any other changes, e.g., to this README.md file, pull from master to your local branch, and push from your local branch to your branch on GitHub: 
```
git pull origin master
git push origin [yourname]
```
So now you might actually want to do some homework.  If you ...
```
cd ~/Documents/homework/cs61a/hw01
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
