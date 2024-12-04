# Better Compiler Output (bco)

## Usage
Depending on the build system you are using, you can pipe the output of the build system to `bco` to get a better output.
Tested with ninja and make, bot with GCC and Clang.

### Ninja
```bash
$ ninja | bco
```

### Make
```bash
$ make | bco
```
