# ECE444 Lab 6 - Test Driven Development
## Completed by Jay Bihola

Note, this repo is based off of https://github.com/mjhea0/flaskr-tdd

## Pros and Cons of TDD

### Pros
Test Driven Development is excellent in terms of scalability and collaboration. TDD forces you to write code that is modular in order to make it easily testable. As a result, using the TDD framework allows for more reusable code. In addition, TDD allows for more comprehensive documentation of the code. Not only do the unit tests capture the intent of the original designer, they are updated as needed so the "documentation" remains up to date. By reading the unit tests, a new designer can understand what the code is supposed to do.

TDD also ensures that changes that a developer makes does not interfere or break the code of another developer working on the same project. TDD also makes regression testing much easier.

### Cons
Even with so many pros, TDD has some downsides that must be thoroughly considered. First and foremost, TDD requires a new style of thinking that many developers may not be used to. In addition, TDD also increases development time as creating so many tests and constantly updating them takes development time (i.e., test maintainance is a lengthy process). For large scale applications, there may be a significant amount of unit tests so later on, when new builds are generated, the testing time may be quite long. 
