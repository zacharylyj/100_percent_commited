# 100 Percent Committed ❤️

## Introduction

Are you a poser aspiring to display a GitHub profile brimming with constant activity and commits just like the pros? Well look no further, because you've come to **100 Percent Committed ❤️** - your go-to repository for generating a dazzling commit history! Our cutting-edge technique produces "real commits" that are bound to captivate your future job prospects, employers and collaborators. 😎💼

# Quick Start

Transform your GitHub activity graph with these simple steps:

## 1. Clone the Repository

Begin by cloning the repository to your local machine:

```bash
git clone https://github.com/zacharylyj/100_percent_commited
```

## 2. Run the Program


cd into the project directory:

```bash
cd 100_percent_commited
```

run the following python program:

```bash
python autogen.py
```

## 3. Push to Github!!!


After generating your commit history with our tool, follow these steps to push it to your new GitHub repository. This will make your GitHub profile stand out with a rich history of contributions.

#### Create a New GitHub Repository

1. Go to GitHub and create a new repository. Note the repository name for the steps below.

#### Configure and Push Your Commit History

2. **Navigate to the `real-repo-history` Directory**:

Open a terminal and change into the directory containing your newly generated commit history.

```bash
cd real-repo-history
```

#### Remove the Existing Git Remote

3. This step ensures that the local repository is no longer linked to the previous remote source.


```bash
git remote remove origin
```

#### Add Your New GitHub Repository as the Remote Origin:

4. Replace `<YOUR_NEW_REPO_NAME>` with the name of the GitHub repository you created. Ensure you use the correct URL format provided by GitHub.

```bash
git remote add origin https://github.com/yourusername/<YOUR_NEW_REPO_NAME>.git
```

#### Rename Your Local Branch to Main (if it's not already named main)

5. Rename your local branch to `main`.

```bash
git branch -m main
```

#### Push Your Commit History to GitHub:

6. Finally, push your commit history to the new repository, setting the upstream branch to main.


```bash
git push -u origin main
```

## Config Features


## End off

For legal reasons use at your own risk.⚖️ I am not Liable for any damages caused by using this tool. Created as a joke.🤡



## Author

Zachary Leong

Feel free to report issues will not respond. But feel free to contact me