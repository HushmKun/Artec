# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!-- ## [Unreleased]

## [1.1.1] - 2023-03-05

### Added

- Arabic translation (#444).
- v1.1 French translation.

### Fixed

- Improve French translation (#377).
- Improve id-ID translation (#416).

### Changed

- Upgrade dependencies: Ruby 3.2.1, Middleman, etc.

### Removed

- Unused normalize.css file
- Identical links assigned in each translation file -->

## [0.3.0] - 2023-08-05

### Added

- Logging to text file & stdout on `-v` flag. 
- Varying Log levels.
- Initialize a git Repository & Commits the structure. 
- New template : _Flask_ 

### Fixed

- Improved error reporting.

## [0.2.1] - 2023-07-16

### Fixed

- ```-s``` & ```-t``` conflict.
- ('files' or 'file') and ('folders' or 'folder') can now be used in the Json structure.

### Changed

- Various functions to increase performance.
- Unified exceptions interface.
- Added extra data to [LEARN.md](LEARN.md)
- Added extra data to [CONTRIBUTING.md](CONTRIBUTING.md)

## [0.2.0] - 2023-07-08
### Added
- ```-t``` argument now allows Templates to be used (Limited to Python & Node.Js)
- Github actions can publish to Pypi & Test.Pypi
- More improvements to error handling and detection.
### Changed
- We can format the project name in the json by using an empty curly brackets {}
- Tests now is *little bit* better than before.


## [0.1.4] - 2023-06-26
### Changed
-  Improved error reporting 

### Fixed
- Fixed Issue [#8](https://github.com/HushmKun/Artec/issues/8)
- Fixed error building structure if the source starts with a file.

## [0.1.3] - 2023-06-20

### Added
- ```-V ``` argument to print version of Artec. 
- Changelog.md to records changes.

## [0.1.2] - 2023-06-17
### Changed
- Tests directory to the preferred structure.

### Fixed
- Files and folders are not being created according to "structure.json" [#4](https://github.com/HushmKun/Artec/issues/4)

## [0.1.1] - 2023-06-15

### Added
- ```-v``` argument to enforce verbosity.

## [0.1.0] - 2023-06-12
### Added
- Unit tests for each module.  

### Changes
- Ported from Python 2.7 into Python 3
- Refactor the fork to more pip-package architecture.
- Split the project into modules for better code & tests.
