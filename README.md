# job-search-bot

A Scrapy-based Python web crawler to notify users on a daily basis with up-to-date job postings.

## Getting Started

### Clone the repo
```
git clone git@github.com:WHYjun/job-search-bot.git
```

### Setting up Requirements

The `requirements.txt` file should list all Python libraries that you should install to run `Job Search Bot`. You can install required libraries by using:

```
pip install --upgrade pip
pip install -r requirements.txt
```

If you don't have pip yet, please install `pip` from the following link: https://pip.pypa.io/en/stable/installing/

### Setting up MongoDB

If you don't have MongoDB yet, please install `MongoDB` from the following link: https://docs.mongodb.com/manual/installation/

Once you have installed MongoDB, you should set dbpath first without any authentication.
```
mongod --dbpath "<your_db_path>"
```
If you already set your repository with running `setup.js`, you may want to reset the repository with running `reset.js` in a separate terminal window.
```
mongo reset.js
```
Then, copy the following JSON to any text editor and save as `config.json`. Please update name and password for security.
```
{
  "repo": {
    "name": "repo"
  },
  "admin": {
    "name": "name",
    "pwd": "password"
  },
  "user": {
    "name": "name",
    "pwd": "password"
  }
}
```
Finally, run `setup.js` to set your repository with your own name and password in `config.json`.
```
mongo setup.js
```
Now, stop `mongod` and restart it with the following command (Enabling authentication).
```
mongod --auth --dbpath "<your_db_path>"
```

### Run Job Search Bot

After setting up all requirements, change directory to `/jobbot/jobbot/spiders`, and run `scrapy genspider <company_name> <company_base_url>`. Please update the created file refer to `example.py`. 


## Future Works

- Add the functionality to filter the job title.