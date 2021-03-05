**Task 1**: Initialize an empty Git repo in the git_HandsOn folder. Notice the message Initialized empty Git repository in: /path/to/git_hands_on/.git/. Explore the content of the .git folder.

We initializate the Git repo.

<code>git init</code>

We explote the content of the .git folder.

<code>ls .git/</code>

**Task 2**: Check the status of the git_HandsOn project.

<code>git status</code>

**Task 3**: Add seqClass.py to the staging area and check the status of the project. In the output, notice that Git indicates the changes to be committed with new file: seqClass.py in green text. Here Git tells us the file was added to the staging area.

We add the script.

<code>git add seqClass.py</code>

We check the status of the project.

<code>git status</code>

**Task 4**: Make your first commit!

<code>git commit -m "First commit"</code>

**Task 5**: use this command to check the difference between the working directory and the staging area. Changes to the file are marked with a + and are indicated in green. Then commit the changes in seqClass.py.

```git diff
  git add seqClass.py
  git commit -m "Corrected script"```

**Task 6**: log a list of your commits.

<code>git log</code>

**Task 6**: Display the last commit using git show HEAD.

<code>git show HEAD</code>

**Task 7**: Edit your script to modify the message it prints when the sequence is not RNA nor DNA. Monitor the change using git status. Then, undo it using git checkout.

After doing some changes, we can review them with:

<code>git status</code>

We undo last changes

<code>git checkout</code>

**Task 8**: Remove any line from your script. Then, add the changes to the staging area, and undo this action using git reset. Use git status to monitor these steps. Hint: This command resets the file in the staging area to be the same as the HEAD commit. It does not discard file changes from the working directory, it just removes them from the staging area, so you will need to use git checkout to recover the erased line in your working directory!.

<code>git reset</code>

**Task 9**: Edit your script to modify the help message, stage it and commit. Then use git revert to undo your commit.

<code>
  nano seqClass.py
  
  git add seqClass.py
  
  git commit -m "Bad script"
  
  git revert HEAD
</code>

**Task 10**: Create a new branch named motif and check on which branch you are located.

<code>
  git branch motif
  
  git branch
</code>

**Task 11**: Switch branch to motif. Verify that you switched branches succesfully and that the commit history of both branches is identical.

<code>
  git checkout motif
  
  git branch
  
  git log
</code>

**Task 12**: Modify seqClass.py

<code>
  gedit seqClass.py
  
  git add seqClass.py
  
  git commit -m "Modified script"
</code>

**Task 12**: Switch again to the master branch and merge your motif branch back to master.

<code>
  git checkout master
  
  git merge motif
  
  git log
</code>

**Task 13**: In the master branch, modify the message that seqClass.py prints when it finds the motif, add and commit the changes. Then, switch to the motif branch and modify the message that seqClass.py prints when it does not find the motif, add and commit the changes. Finally, merge the motif branch back into master.

<code>
  nano seqClass.py
  
  git add seqClass.py
  
  git commit -m "Modified1 script"
  
  git checkout motif
  
  nano seqClass.py
  
  git add seqClass.py
  
  git commit -m "Modified2 script"
  
  git checkout master
  
  git merge motif
</code>

**Task 14**: Repeat the previous task but modifying in both cases the message that seqClass.py prints when it finds the motif.

<code>
  nano seqClass.py
  
  git add seqClass.py
  
  git commit -m "Modified3 script"
  
  git checkout motif
  
  nano seqClass.py
  
  git add seqClass.py
  
  git commit -m "Modified4 script"
  
  git checkout master
  
  git merge motif
</code>

**Task 15**: Delete the content of the line as it appears in the master branch as well as all Git's special markings including the words HEAD and motif. Then save the file, add and commit your changes.

<code>
  nano seqClass.py
  
  git add seqClass.py
  
  git commit -m "Modified4 script"
</code>

**Task 16**: Delete the motif branch.

<code>git branch -d motif</code>

**Task 17**: Edit your script to add some comment lines explaining what every piece of code does, stage it and commit. Then push the commits to your remote repository. The changes will be visible at GitHub.

<code>
  gedit seqClass.py
  
  git add seqClass.py
  
  git commit -m "Modified4 script"
</code>

**Task 18**: Through the GitHub webpage, add a README.md file explaining the usage of the script seqClass.py and commit. It can contain just a line, or something more elaborated. Then, pull the commit to your local repository.

<code>git pull</code>

**Task 20**: Clone ggsashimi repository from guigolab.

<code>git clone https://github.com/guigolab/ggsashimi</code>

## Exercise 1:

Make a new branch called fix and move to it.
Fix the seqClass.py script so that it is able to classify correctly any RNA or DNA sequence.
We change our code and add some notes.
Merge the fix branch back to master.
Make sure you add comments to explain your changes.
Stage and commit the changes on master in your local repository.
Push your commits on master to your GitHub repository.
Stage, commit and push your changes in the fix branch to your GitHub repository.

<code>
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
</code>
