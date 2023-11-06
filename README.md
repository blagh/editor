# editor
## I swore I made this private but I guess I didn't :laughing: There is nothing here to see yet really, just notes on what this could be.

This is not just a linter, this is an editor to help you write scalable, human-readable code. (Scalable here meaning: to any size of codebase, not to the amount of traffic.)

Because sometimes, when people complain about a framework and its scalability, they are actually complaining about how hard it is to navigate things when things get out of hand. Also sometimes, it's easy to do premature optimization that doesn't actually help -- breaking up a script into modules when it would be more understandable (and therefore maintainable) in a single file.

The interesting thing is that you can do a lot without getting into language specifics -- e.g counting the number of files in a directory, the directory depth in general. You might need it to be configurable _to_ a specific language (a Java project is going to need deeper allowances than a Python one), but the logic is the same. It's also not intended to supplant language-specific linters -- if this tool contradicts any of those more specific tools, please accept those recommendations instead!

Some folks are still going to hate the idea. That's ok! I don't think this is ever going to be a tool for everyone, and I don't think I'd ever encourage, say, having it as a blocking step in a build pipeline. It's purely to help make _suggestions_ about code navigatability and readability! And all such automated suggestions should only be applied with your best judgement -- at the end of the day, you're the human, and you'll always be the best entity to make stylistic judgement calls about your codebase.
