### directory-level editor

# max number of sub-directory
# max number of files
# collect results
# for file in files
  # run file-level editor
  # collect results
# for directory in sub-directories
  # run directory-level editor
  # collect results
# output results

### file-level editor

## language agnostic (although configurable) -- general "density"
# - max number of char -> line -> block -> file
  # - number of chars in a line
  # - number of lines in a block (empty line or other separator)
  # - number of blocks in a file (this could be lines also? but there's something satisfying about the way blocks ladders up)
# - min number of char -> line -> block -> file
  # - a little trickier than max :thonk: maybe it's a multi-level thing, like, the number of files with only one block, the number of dirs with only one file
# - indent level
# - number of blocks in a file
# - directory depth
# - variable name length
# - repetition of non-dictionary words (avoid acronyms)
# - density of special characters on a line
# - overly repetitive terms (not keywords of course)
# - comment to code ratio (rather than needing to document each block, look at the overall ratio of comment lines to code lines)

## more language specific
# - ignore library code of course!
# - method call tracing
  # - max non-recursive call stack depth
  # - daisy-chain methods vs controller method (a->b->c->d vs a->b a->c a->d)
  # - max scroll diff (how far are you going up and down, how often do you have to switch directions)
  # - max file changes in stack trace
# - "empty" files (e.g just a class definition)
# - avoid use of `not` in complex expressions
# - avoid mixing `and` and `or`
# - recommend type-hinting? :squint: recommend at a certain size of codebase?
