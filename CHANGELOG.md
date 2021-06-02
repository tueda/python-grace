# Changelog


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


[0.0.4]: https://github.com/tueda/python-grace/compare/0.0.3...0.0.4
[0.0.3]: https://github.com/tueda/python-grace/compare/0.0.2...0.0.3
[0.0.2]: https://github.com/tueda/python-grace/compare/0.0.1...0.0.2
