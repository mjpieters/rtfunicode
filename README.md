# Unicode to RTF command code conversion

This module implements an encoder for unicode to RTF 1.5 command sequences; it
can be used to generate valid RTF output with international characters.

Importing this module adds a new `rtfunicode` codec, allowing you to encode
unicode strings to valid RTF bytecode sequences:

```pycon
>>> import rtfunicode
>>> 'RTF and unicode mix just fine! \u263A'.encode('rtfunicode')
'RTF and unicode mix just fine! \\u9786?'
```

The RTF command code for a unicode character is `\uN?`, where N is a signed
16-bit integer and the ? is a placeholder character for older RTF readers. This
module sets the latter to the '?' literal for simplicity's sake.

## Requirements

* Python 3.3 or newer.


## Development

The project code is hosted on [GitHub][], feel free to report issues,
fork the code and issue pull requests.

[GitHub]: https://github.com/mjpieters/rtfunicode


## License

BSD 2-Clause (simplified), see: [LICENSE.txt](./LICENSE.txt)


## Author

Martijn Pieters <mj@zopatista.com>
