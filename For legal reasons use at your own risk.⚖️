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
```
{
    "start_date": "2005-01-02", //Start date of the commit history
    "end_date": "2005-12-30", //End date of the commit history
    "probability_no_weekend_commit": 0.7, //probability that no commits are made on weekends
    "commit_profiles": [
        { "min_commits": 0, "max_commits": 0, "probability": 30 }, 
        { "min_commits": 1, "max_commits": 5, "probability": 55 },
        { "min_commits": 6, "max_commits": 15, "probability": 12 },
        { "min_commits": 16, "max_commits": 100, "probability": 3 }
    ], 
    //set commit profiles where min to max is the range and the probability is the probability of that range being selected. make sure adds up to 100 didnt do error handling for this 😝
    "time_clusters": [
        { "start_hour": 9, "end_hour": 11 },
        { "start_hour": 13, "end_hour": 16 },
        { "start_hour": 19, "end_hour": 21 },
        { "start_hour": 1, "end_hour": 5 }
    ],
    //set commit time profiles example you only code from 1-5am and 19-21pm
    "repo_path": "real-repo-history", //path to the directory containing the commit history
    "email": "dajohndoe@fake.com", //email for the commit history
    "name": "dajohndoe" //name for the commit history

}
```
## End off

For legal reasons use at your own risk.⚖️ I am not Liable for any damages caused by using this tool. Created as a joke.🤡

Note dont set past year 1970, UTC was apparent not a thing back then.



## Author

Zachary Leong

Feel free to report issues will not respond. But feel free to contact me
