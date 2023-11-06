# editor
I swore I made this private but I guess I didn't :laughing: There is nothing here to see yet really, just notes on what this could be.

Not just a linter, an editor to help you write scalable, human-readable code. (Scalable here meaning: to any size of codebase, not to the amount of traffic.)

Because sometimes, when people complain about a framework and its scalability, they are actually complaining about how hard it is to navigate things when things get out of hand. Also sometimes, it's easy to do premature optimization that doesn't actually help -- breaking up a script into modules when it would be more understandable (and therefore maintainable) in a single file.

Some folks are going to hate the idea. That's ok! I don't think this is ever going to be a tool for everyone, and I don't think I'd ever encourage, say, having it as a blocking step in a build pipeline.

It's also not intended to supplant language-specific linters -- if this tool contradicts any of those more specific tools, please accept their recommendations instead!

It's purely to help make suggestions about code navigatability and readability! And all such automated suggestions should only be applied with your best judgement -- at the end of the day, you're the human, and you'll always be the best entity to make stylistic judgement calls about your codebase.
