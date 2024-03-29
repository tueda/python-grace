# Changelog

<a name="0.0.9"></a>
## [0.0.9] (2023-08-15)
### Fixed
- Fix compatibility issue with `click >= 8.1.4`.
  ([1df93b2](https://github.com/tueda/python-grace/commit/1df93b288a5b0c39958133f63165661b3f439f91))


<a name="0.0.8"></a>
## [0.0.8] (2021-11-25)
### Added
- `grace --verbose` option to output verbose messages. `-v` for short. `-vv` is reserved for more verbose messages in debugging.
  ([f439383](https://github.com/tueda/python-grace/commit/f439383a2362176326795f4014f5125a68d06e83))
- Run `ps2pdf` (if available), when `gracefig` generates an EPS file, to produce also a PDF file.
  ([02d4b3b](https://github.com/tueda/python-grace/commit/02d4b3b54956fdc519689bb2dcb7f26b7d04b52f))


<a name="0.0.7"></a>
## [0.0.7] (2021-11-01)
### Fixed
- Bug in `build.py` that caused a build error on macOS.
  ([60df64e](https://github.com/tueda/python-grace/commit/60df64e419415e61ddd86d9611b0d261727aad78))


<a name="0.0.6"></a>
## [0.0.6] (2021-10-30)
### Added
- New raw command `grcext`. For example, `grace grcext` reads `bases.result` and prints computer-readable histogram data to the standard output. See also the help message shown by `grace grcext --help`.
  ([#5](https://github.com/tueda/python-grace/issues/5))
- Handling non-zero exit status codes returned from the raw commands. This makes the error message more understandable.
  ([868cb4b](https://github.com/tueda/python-grace/commit/868cb4b01a18c8839bebad45f5ed212d89ade0e8))


<a name="0.0.5"></a>
## [0.0.5] (2021-09-01)
### Added
- Build also debug-version executables/libraries.
  To link the libraries in the debug build, the right-hand side of the line
  `GRACELDIR = $(GRACEROOT)/lib` in `Makefile` should be modified as
  `$(GRACEROOT)/lib/debug` by hand for now.
  ([ed08931](https://github.com/tueda/python-grace/commit/ed0893163636bfd3af33d99e9ede946f43abb6c8))
- `--debug` option. For now it is used to invoke debug-version executables.
  ([db05610](https://github.com/tueda/python-grace/commit/db056101fc98d2be83443c2d918e34e11148a0c8))
- Shell completion should now work as described in
  [Click's documentation](https://click.palletsprojects.com/en/8.0.x/shell-completion/#enabling-completion).
  For example, in bash, add the following line to `~/.bashrc`:
  ```bash
  eval "$(_GRACE_COMPLETE=bash_source grace)"
  ```
  This was completed by implementing shell completion for `grace template`.
  ([6617d4c](https://github.com/tueda/python-grace/commit/6617d4c9d13cbeb234585ee6d50167320a30f70a))


<a name="0.0.4"></a>
## [0.0.4] (2021-06-02)
### Added
- `grace --version` option to print the version.
  ([1e7f020](https://github.com/tueda/python-grace/commit/1e7f0206de95fa96e4dc2b67a8c4857d4eba9d1c))

### Fixed
- Possible `FileNotFoundError` when `grace grcfort -h`.
  ([c128f12](https://github.com/tueda/python-grace/commit/c128f12d0884891713d03cc2859f7aa1cdd0b83c))


<a name="0.0.3"></a>
## [0.0.3] (2021-04-22)
### Fixed
- `grcfort` generated wrong Fortran code, caused by different versions of GRACE source files.
  ([17e8e64](https://github.com/tueda/python-grace/commit/17e8e6487e017172d91d14a5e7d1add64e9f3a08))


<a name="0.0.2"></a>
## [0.0.2] (2021-02-24)
### Fixed
- Build failure for `gracefig` with gcc 10.
  ([#1](https://github.com/tueda/python-grace/issues/1))
- Build failure on systems without C++ compilers.
  ([#2](https://github.com/tueda/python-grace/issues/2))


<a name="0.0.1"></a>
## 0.0.1 (2021-02-20)
- First release. This version provides GRACE 2.2.1 as it is.


[0.0.9]: https://github.com/tueda/python-grace/compare/0.0.8...0.0.9
[0.0.8]: https://github.com/tueda/python-grace/compare/0.0.7...0.0.8
[0.0.7]: https://github.com/tueda/python-grace/compare/0.0.6...0.0.7
[0.0.6]: https://github.com/tueda/python-grace/compare/0.0.5...0.0.6
[0.0.5]: https://github.com/tueda/python-grace/compare/0.0.4...0.0.5
[0.0.4]: https://github.com/tueda/python-grace/compare/0.0.3...0.0.4
[0.0.3]: https://github.com/tueda/python-grace/compare/0.0.2...0.0.3
[0.0.2]: https://github.com/tueda/python-grace/compare/0.0.1...0.0.2
