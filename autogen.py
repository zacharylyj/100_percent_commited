import subprocess
import os
import random
import json
from datetime import datetime, timedelta

def adjust_for_timezone(dt, offset_hours=8):
    return dt + timedelta(hours=offset_hours)
def load_config(path):
    with open(path, "r") as file:
        return json.load(file)


def create_commit_date_list(start_date, end_date, commit_profiles, time_clusters, probability_no_weekend_commit):
    commit_dates = []
    total_probability = sum(profile['probability'] for profile in commit_profiles)
    weighted_profiles = [(profile, profile['probability'] / total_probability) for profile in commit_profiles]

    current_date = start_date
    
    while current_date <= end_date:
        if current_date.weekday() in [5, 6] and random.random() <= probability_no_weekend_commit:
            pass
        else:
            profile = random.choices(weighted_profiles, weights=[wp[1] for wp in weighted_profiles])[0][0]
            commit_count = random.randint(profile['min_commits'], profile['max_commits'])
            
            if commit_count > 0:
                cluster = random.choice(time_clusters)
                
                for _ in range(commit_count):
                    random_hour = random.randint(cluster['start_hour'], cluster['end_hour'])
                    random_time = current_date.replace(hour=random_hour, 
                                                       minute=random.randint(0, 59),
                                                       second=random.randint(0, 59))
                    commit_dates.append(random_time)
        current_date += timedelta(days=1)
    return commit_dates

def generate_commits(commit_dates, repo_path, email, name):
    if not os.path.exists(repo_path):
        os.makedirs(repo_path)
    os.chdir(repo_path)
    subprocess.run(["git", "init"])
    for commit_date in commit_dates:
        date_str = commit_date.strftime('%Y-%m-%d %H:%M:%S')
        with open("dummy_file.txt", "a") as file:
            file.write(f"Commit on {date_str}\n")
        subprocess.run(["git", "add", "dummy_file.txt"])
        subprocess.run(["git", "config", "user.email", f"{email}"])
        subprocess.run(["git", "config", "user.name", f"{name}"])
        subprocess.run(["git", "commit", "-m", "real commit", "--date", date_str], env={"GIT_AUTHOR_DATE": date_str, "GIT_COMMITTER_DATE": date_str})

if __name__ == "__main__":
    config = load_config("config.json")
    start_date = datetime.strptime(config['start_date'], '%Y-%m-%d')
    end_date = datetime.strptime(config['end_date'], '%Y-%m-%d')  
    
    commit_dates = create_commit_date_list(start_date, end_date, config["commit_profiles"], config["time_clusters"], config["probability_no_weekend_commit"])
    generate_commits(commit_dates, config["repo_path"], config["email"], config["name"])
    print("Done generating 100% real commits.")
