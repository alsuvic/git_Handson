**Task 1**: Initialize an empty Git repo in the git_HandsOn folder. Notice the message Initialized empty Git repository in: /path/to/git_hands_on/.git/. Explore the content of the .git folder.

We initializate the Git repo.
git init
We explote the content of the .git folder.
ls .git/

**Task 2**: Check the status of the git_HandsOn project.

git status

**Task 3**: Add seqClass.py to the staging area and check the status of the project. In the output, notice that Git indicates the changes to be committed with new file: seqClass.py in green text. Here Git tells us the file was added to the staging area.

We add the script.
git add seqClass.py
We check the status of the project.
git status

**Task 4**: Make your first commit!

git commit -m "First commit"

**Task 5**: use this command to check the difference between the working directory and the staging area. Changes to the file are marked with a + and are indicated in green. Then commit the changes in seqClass.py.

git diff
git add seqClass.py
git commit -m "Corrected script"

**Task 6**: log a list of your commits.

git log

**Task 6**: Display the last commit using git show HEAD.

git show HEAD

**Task 7**: Edit your script to modify the message it prints when the sequence is not RNA nor DNA. Monitor the change using git status. Then, undo it using git checkout.

After doing some changes, we can review them with:
git status
We undo last changes
git checkout

**Task 8**: Remove any line from your script. Then, add the changes to the staging area, and undo this action using git reset. Use git status to monitor these steps. Hint: This command resets the file in the staging area to be the same as the HEAD commit. It does not discard file changes from the working directory, it just removes them from the staging area, so you will need to use git checkout to recover the erased line in your working directory!.

git reset

**Task 9**: Edit your script to modify the help message, stage it and commit. Then use git revert to undo your commit.

nano seqClass.py
git add seqClass.py
git commit -m "Bad script"
git revert HEAD

**Task 10**: Create a new branch named motif and check on which branch you are located.

git branch motif
git branch

**Task 11**: Switch branch to motif. Verify that you switched branches succesfully and that the commit history of both branches is identical.

git checkout motif
git branch
git log

**Task 12**: Modify seqClass.py

gedit seqClass.py
git add seqClass.py
git commit -m "Modified script"

**Task 12**: Switch again to the master branch and merge your motif branch back to master.

git checkout master
git merge motif
git log

**Task 13**: In the master branch, modify the message that seqClass.py prints when it finds the motif, add and commit the changes. Then, switch to the motif branch and modify the message that seqClass.py prints when it does not find the motif, add and commit the changes. Finally, merge the motif branch back into master.

nano seqClass.py
git add seqClass.py
git commit -m "Modified1 script"
git checkout motif
nano seqClass.py
git add seqClass.py
git commit -m "Modified2 script"
git checkout master
git merge motif

**Task 14**: Repeat the previous task but modifying in both cases the message that seqClass.py prints when it finds the motif.

nano seqClass.py
git add seqClass.py
git commit -m "Modified3 script"
git checkout motif
nano seqClass.py
git add seqClass.py
git commit -m "Modified4 script"
git checkout master
git merge motif

**Task 15**: Delete the content of the line as it appears in the master branch as well as all Git's special markings including the words HEAD and motif. Then save the file, add and commit your changes.

nano seqClass.py
git add seqClass.py
git commit -m "Modified4 script"

**Task 16**: Delete the motif branch.

git branch -d motif

**Task 17**: Edit your script to add some comment lines explaining what every piece of code does, stage it and commit. Then push the commits to your remote repository. The changes will be visible at GitHub.

gedit seqClass.py
git add seqClass.py
git commit -m "Modified4 script"

**Task 18**: Through the GitHub webpage, add a README.md file explaining the usage of the script seqClass.py and commit. It can contain just a line, or something more elaborated. Then, pull the commit to your local repository.

git pull

**Task 20**: Clone ggsashimi repository from guigolab.

git clone https://github.com/guigolab/ggsashimi

## Exercise 1:

Make a new branch called fix and move to it.
Fix the seqClass.py script so that it is able to classify correctly any RNA or DNA sequence.
We change our code and add some notes.
Merge the fix branch back to master.
Make sure you add comments to explain your changes.
Stage and commit the changes on master in your local repository.
Push your commits on master to your GitHub repository.
Stage, commit and push your changes in the fix branch to your GitHub repository.

git branch fix
git checkout fix
gedit seqClass.py
git add seqClass.py
git commit -m "Comments script"
git checkout master
git merge fix
git pull
git push
git checkout fix 
git push -u origin fix
