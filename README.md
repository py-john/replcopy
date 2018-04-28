## replcopy

Parse clipboard copied code from the interpreter REPL. 

The idea is to be able to test code in the interpreter, copy it, and then use `replcopy.copy()` to bring a parsed version to the clipboard that can be pasted into a code editor and run as a normal script. 

The parsed version of the code has as much unnecessary and potentially error causing text removed as possible, such as `>>>`, `...`, tracebacks and other output.
