### create and push
**1. create git folder**
```shell
git init
```
**create/clone remote repo**
```shell
git remote add origin git@github.com:<username>/<reponame>.git
```
```shell
git clone git@github.com:<username>/<reponame>.git
```
**check status**
```shell
git status
```
**2. update changes**
```shell
git add .
```

**3. commit changes**
```shell
git commit -m '<your notes>'
```
**4. push commit to Github**
```shell
git push
```
* may fail if conflicts exist

or push to master branch specifically
```shell
git push -u origin master
```
* `origin`: name of the remote repo
* `master`: name of the remote branch

**7. cancel the commit**
```shell
git reset HEAD~1
```
- `1` is the index of commit. To check commit indexes:
  ```shell
  git log
  ```

### if comflicts exist:
**4-1. copy new commits to local repo**
```shell
git fetch origin master
```
**then integrate the remote changes with local changes**
```shell
git rebase origin/master
```
* `origin/master`: local tracking branch pointing to the local copy
* or `4-1` + `4-2`:
  ```shell
  git pull --rebase origin master
  ```
**4-2. reset local branch to origin**
```shell
git reset --head origin/master
```

**5. push**
```shell
git push origin master
```
- to check which repo this folder is pushing to:
  ```shell
  git remote -v
  ```

**or force push, will override all the changes in `origin master` (instead of `4-1` + `4-2` + `5`):**
```shell
git push -f -u origin master
```


### branch
**1. fetch the remote branch**
```shell
git fetch origin <remote branch name>
```
or **fetch remote branch and name it**
```shell
git fetch origin <remote branch name>:<local branch name>
```
**2. create local branch and change to it**
```shell
git checkout -b <local name> origin/<remote branch name>
```
* just change to a branch:
  ```shell
  git checkout <branch name>
  ```
**3. pull from branch**
```shell
git pull origin <remote branch name>
```

**4. create relationship btn remote and local branches**
- check relationship
  ```shell
  git branch -vv
  ```
- create relationship
  ```shell
  git branch -u origin/<remote branch>
  ```
  or
  ```shell
  git branch --set-upstream-to origin/<remote branch>
  ```
**5. delete**
```shell
git branch --unset-upstream
```
**6. check**
- check all remote branches
  ```shell
  git branch -r
  ```
- check all local branches
  ```shell
  git branch
  ```
- check all branches
  ```shell
  git branch -a
  ```


### gitignore
`.gitignore` is to prevent untracked files from being tracked. if files are already tracked:

**1. remove from cache:**
```shell
git rm --cached <filename>
git rm -r --cached <foldername>
```
**2. after remove, `commit` the changes without `add`.**

**3. gitignore patterns**
[patterns to match files](https://www.atlassian.com/git/tutorials/saving-changes/gitignore#git-ignore-patterns)