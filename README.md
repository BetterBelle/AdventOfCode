# AdventOfCode

A repository for all of my Advent Of Code needs. Every year, every programming language that I've done.
You can also create your own fork from this project as a template for your own. I'll be updating this as I solve more problems, 
or create new solutions to old ones in either Python or whatever other language I decide to use.

Feel free to create your own branch for your own personal use!

## Python Solutions

Python solutions are run from the root. So running them from command line would look something like

python python/2015/day01.py

When running python programs, because I was using relative filepaths from the root in VSCode, python needs to run from the root to see the input files.
If running from command line, you could easily change the filepaths to be relative from the python directory and access them this way.

## J Solutions

I use a J extension in VSCode that allows me to load and display the scripts, again from the root.

## Rust Solutions

The rust directory is a cargo project. Move into the rust directory from the command line and do cargo run.

To run a specific day (provided it exists), you can do the command

cargo run -- -y (year) -d (day)

and the specific day and year you selected will be run. If none is selected, runs 2015 day 1.
