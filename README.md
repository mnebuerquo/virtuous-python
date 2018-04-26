# virtuous-python
This is a tool for writing python virtuously. Support linting, testing, deploying and good maintenance.

## What is this?

This is a script to help you be virtuous when writing and running Python
programs.

I had just come back to python after not using it for a while, and I was
annoyed wiith having to set up a virtualenv and activate it for each project.
So I wrote a script to make that easier. Mostly because I didn't want to have
to remember the steps and commands, and I didn't want to have to remember to
pip install or freeze my requirements.

This script is like a cross between a wrapper and a makefile. It runs your
program, but it also creates, activates and cleans up a virtualenv around it.
It can run a linter, test suite, and auto-format your code as well. And it can
be used to run things in production.

## How to use it (in a hurry):

1. Copy the `run` script to your project directory.
2. Edit your requirements.txt and add your dependencies.
3. Call `run` with your main file as the first argument:
```bash
./run my-app.py arg1 arg2 arg3
```
4. Profit!

## Options

The `run` script has some options which help you write clean code.

* `--lint` - Run a linter and output warnings about your code. This uses
  [flake8](http://flake8.pycqa.org/en/latest/) to give warnings for code not 
  following PEP8 conventions.
* `--test` - Run [pytest](https://docs.pytest.org/en/latest/) to evaluate all 
  your tests.
* `--format <path>` - Auto-format your code with 
  [autopep8](https://github.com/hhatto/autopep8) to fix all your annoying little
  whitespace inconsistencies.
* `--clean` - removes virtualenv directories so you can re-install all your
  dependencies.
* Without the above options, it runs any python program you tell it.

## Features

* Simplifies your development workflow.
* Manages your virtualenv directories for the project so you don't have to.
* Provides built-in configuration for flake8 (lint) and pytest.
* Creates a `.gitignore` for python if you don't already have one.
* Automatically installs and freezes your requirements.

## How I use it:

First I copy `run` to my project, either a legacy project or a new one. Then I
follow these steps:

1. `./run my-project-main.py with command line args` - When I run, it sets up
   my virtualenv, activates it for me, and pip installs my requirements. I
   don't have to think about that stuff. I see my code is working or I find a
   bug which I need to fix.
2. Write code to fix a bug or add a feature.
3. Add tests to the code.
4. `./run --test` - Run all my tests, and see if they pass or fail. Fix and
   repeat.
5. `./run --format . && ./run --lint` - Then I fix any lint warnings. Repeat
   until there are no more warnings.
6. Repeat until happy.
7. Commmit code, requirements.txt, and requirements.freeze to git.
