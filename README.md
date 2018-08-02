# Game Night

Game Night is a game night planning app whether it's in person or online. It allows signups, adding friends, and creating events to schedule (with responses from users on attendance) with a list of games available to play [here](https://game-nighter.herokuapp.com/).

## Getting Started

1. Clone this repository.

  ```shell
  git clone git@github.com:jrambold/gamenight.git
  ```
2. Change into the `gamenight` directory

3. Create a virtualenv

  ```shell
  virtualenv -p python .venv
  source .venv/bin/activate
  ```
4. Updgrade pip and install dependencies
  ```shell
  pip install -r requirements.txt
  ```

3. Set up the database in psql

  ```shell
  CREATE DATABASE gamenight;
  CREATE DATABASE gamenight;
  ```

4. Set appropriate environemntal variables (SECRET_KEY, SENDGRID info if wanting email functionality)

5. Start Redis server if requiring email functionality

6. Migrate Database
  ```shell
  python manage.py migrate
  ```

6. Create SuperUser
  ```shell
  python manage.py createsuperuser
  ```

### Prerequisites

You'll need [Python3](https://www.python.org/downloads/) installed

## Running the Server Locally

To see your code in action locally, you need to fire up a development server. Use the command:

```shell
python manage.py runserver
```

Once the server is running, visit.

* `http://localhost:8000/` to run the application.

## Deployment

Deployed project is [here](https://game-nighter.herokuapp.com/)

## Contributing

Please follow the Getting Started guide to set up your local dev environment.

This guide assumes that the git remote name of the main repo is `upstream` and that your fork is named `origin`.

Create a new branch on your local machine to make your changes against (based on `upstream/master`):

    git checkout -b branch-name-here --no-track upstream/master

### Making a change

Make your changes to the codebase.

Once the tests are passing you can commit your changes. See [How to Write a Good Commit Message](https://chris.beams.io/posts/git-commit/) for more tips.

    git add .
    git commit -m "Add a concise commit message describing your change here"

Push your changes to a branch on your fork:

    git push origin branch-name-here

### Submitting a Pull Request

Use the GitHub UI to submit a new pull request against upstream/master. To increase the chances that your pull request is swiftly accepted please have a look at this guide to [making a great pull request](https://www.atlassian.com/blog/git/written-unwritten-guide-pull-requests)

## Built With

* [Django](https://www.djangoproject.com/) - Web Framework
* [Bootstrap](https://getbootstrap.com/) - Bootstrap for styling


## Acknowledgments

* A shoutout to [Shelby Klein](https://shelbyklein.design/) for help with styling.
