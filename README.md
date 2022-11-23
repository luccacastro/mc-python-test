
# Mitigate Cyber Python Test

This is a small backend script used for create, delete, update and show all tasks in a database.
## Installation

This Project requires Python 3.10.6 in order to run or any newer version

After cloning this project, you need to create a virtual environment,
in order for you to that, run the following commands

```bash
    pip install virtualenv
```

After the installation, run this following command to create a virtual env in your local directory 


```bash
   virtualenv venv
```

And this one for activate

```bash
   source venv/bin/activate
```

Once you're done setting up the venv, run this command to install all of the necessary packages to run the program

```bash
   pip install -r requirements.txt
```

## Running Tests

To run tests, run the following command

```bash
  python test.py
```

## Usage/Commands

The script supports the following commands:

##
Shows a table containing all tasks in a database

```bash
    python3 main.py list
```

Creates a new task with $task_message filling the message field

```bash
    python3 main.py create $task_message
```

Deletes a specific task by Id, if the task doesn't exist it will return -1

```bash
    python3 main.py delete $id
```

Set a status of a specific as False and populate the stopped_at field with the current timestamp

```bash
    python3 main.py stop  $id
```

Updates the message field in a task with id $id with $task_message

```bash
    python3 main.py update $id $task_message
```

Deletes all entries in the database

```bash
    python3 main.py killall
```
