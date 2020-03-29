# Instagram Unfollow Bot

## What does it do?

This is an automation script coded by Hamza Mughal that logs into your Instagram account and get your following list clean. Basically this script unfollows all the accounts you've been following and don't have much time to do it manually. Worth noting that I created this script while in quarantine period due to Corona Virus for fun.

## Do I need this?

Tricky Question! The answer is maybe yes or maybe no. Yes in that case you've blindly followed people on Instagram and you aren't sure how to get rid of them. This simple script would help you get rid of them

## How to use?

- Clone this repository to your system or try downloading the zip file. If using commandline make sure that you've installed git.

- Navigate to the project directory and in the terminal execute the following commands. But before make sure python and pip are installed and added to the path

```
$ pip install virtualenv
```

- The last command would install virtualenv. Now you need to create a virtual environment, execute the following command and give a name to your environment. mostly called `venv`

```
$ virtualenv <name for virtual environment> eg:(venv)
```

- The virtual environment is created and is ready for use. execute the following command and replace `venv` with your environment name. This would activate the venv

```
$ source venv/bin/activate
```

- Copy `.env.example` to `.env` and fill out your username and password in the required fields

```
$ cp .env.example .env
$ vim .env
```

- At last run the script and using python command and it would get everything done for you. Make sure you're using python v3.x.x

```
$ python --version
$ python main.py # For linux
$ python3 main.py # For mac
```

## Issues you might face

Remember this script was created on March 29, 2020. So if you get an error that the element doesn't exists you can try changing the `sleep(time_in_seconds)` time to something higher and it might also depend on your internet connection.

Secondly it may have issues when instagram gets updated.

## Useful Links

- Website: [ProDeSquare](https://prodesquare.com/)

## What I ask?

If you like this script and found this useful you can star this repo and share with your friends.
