# Format

https://github.com/todotxt/todo.txt

# Ruminations

Remember.
Aspire.
Execute.

This is a river of time I can read from completed to aspirational, or aspirational to completed. I can see views
and slices of this river at will.

* Aspire
  There are todos that are certain, and then there are todos that we hope to accomplish.
  Then there are todos so large and ambiguous they need to be decomposed into smaller todos to be accomplished.
  Then there are learnings and best practices I want to inform my processes.
  Then there are tasks I want to groom before committing to execution
  Then I want to periodically groom my Resources

* Remember
  Then there are memories (days and then days) that I want to remember, and reminisce upon.
  Then there is equipment I find useful, and more that I want to find, and that I want to share.
  Then there are events I've done and places I've been that I want to share with others, or vice versa.
  Then there are people that I want to keep track of, and how consistent they are.

* Execute
  Then there are ones that have to happen at a certain time.
  Then there are habits I want to be reminded of.
  Then there are times I only want to focus on a certain project
  Then there are times I only have availability in a certain context



Done     -> Todos      ->  Aspirations
Memories -> Recurring  ->  Resources
Postcards -> Habits
Characters -> Locations


Upcoming Features:
* I will respect the A-Z priority system from the original CLI. It will take precedence over all other sorting.
* I will implement the listcon autocompete
* autocompletion  https://github.com/pallets/click/blob/main/examples/completion/completion.py
* I will add a command that parses the todo.txt file for errors e.g. errant dates, duplicate tags, etc...
* I will add a memories function
* shorthand date functions for due and time and autocompletion
* I will add a shorthand for date and time for the Python-nized `add` command
* cast of characters autocompletion
* First friday of the month like Nebula
* Handle negative days in ls 
* I'll add a postcard function
* Overlapping start/cease or any date check
* Reverse journal style for history
* MermaidJS compatibility
* Quarto?
* I will parse this project to see if there's anything useful https://github.com/francoischalifour/todo-cli?tab=readme-ov-file
* I will parse the add-on directory for anything useful https://github.com/todotxt/todo.txt-cli/wiki/Todo.sh-Add-on-Directory
* I will be able to parse any todo.txt files and concatenate them with each other.
* I will create a "slot" for a single aspirational thing with a header
* I will implement a dependencies concept like in https://htmlpreview.github.io/?https://github.com/topydo/topydo/blob/master/docs/index.html

  ```bash
  #Things to port:
  # secondary
  pri          -- adds or replace in NUMBER the priority PRIORITY (upper case letter).
  depri        -- remove prioritization from item
  help         -- display help
  listall      -- displays items including done ones containing TERM(s)
  listcon      -- list all contexts
  listfile     -- display all files in .todo directory
  listproj     -- lists all the projects in todo.txt.
  ```
