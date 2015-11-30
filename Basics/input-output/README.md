# input-output

### Example python scripts that can take text input and produces text output.

These scripts can conveniently be used as a starting point of a project that takes text input, manipulates it and sends some text output.

There are three variants of this script:

- `read_from_sources.py`: can read from different sources: interactive input / stdin / command line arguments
- `read_from_prefered.py`: reads from either stdin or command line arguments, stdin takes precedence over arguments
- `read_and_log.py`: like the above and outputs to two different targets: the stdout and different output to log file.

----

## `read_from_sources.py`

This script demonstrates how to read from different inputs:

- from the standard input (stdin)
- from the arguments given on the command line
- from an interactive prompt

To make this script work and actually do something, uncomment the specific line in the main() function.

## `read_from_prefered.py`

This script reads input from two possible sources:

- either from the standard input (stdin)
- or from the arguments given on the command line.

It will only do the latter (read from the command line arguments), if the former (the stdin) is empty.

## `read_and_log.py`

This script does like the previous: it reads from two possible sources: either from the stdin or from command line arguments.

Additionally, – and besides printing output to the standard out (stdout) – this script logs to an external logfile (the `example.log` file in the same directory).

It is useful to have different outputs simultaneously and next to each other, when doing text processing. This allows you to both have a "debug stream", to inspect and monitor the process of your coding, and at the same time produce the result you want as the main purpose of this script: the processed text output.