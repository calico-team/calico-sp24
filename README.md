![CALICO Logo](https://calico.berkeley.edu/images/banner/blocks.png)

# calico-sp24
***Note**: This repo is under construction. Check back occasionally for updates! Last Updated: 4/28*

## Editorial Progress
**Published**: 

**Drafted**:  

## Quick Start
This repository contains all contest materials for CALICO Spring '24, including problem statements, templates, tests, executables, solutions, and editorials.

You can explore this repository using GitHub in your browser or download an [archive of all the files](https://github.com/calico-team/calico-sp24/archive/refs/heads/main.zip). If you'd like to see what files participants were given during the contest, you can download the [contest.zip](https://calico.berkeley.edu/files/calico-sp24/contest.zip)!

Although the contest is over, you will be able to submit solutions to the [judge platform](https://calicojudge.com) under the `calico-sp24-archive` contest when it is brought online. Sign in or register if you don't have an account already. Then change the selected contest to `calico-sp24-archive` on the right side of the navigation bar.

## Repository Structure
Subdirectories are named after problem IDs and contain their solutions, editorials, tests, templates, and problem statements.

### Problem Statements
Problem statements describe the problem contestants need to solve, as well as their input and output format. They are named `[problem name].pdf`.

### Templates
Templates provide starter code that handle parsing input in multiple languages, so contestants can jump right into problem solving. They are named `[problem name]_template.[extension]`.

Note that these templates are only guaranteed to apply to the main test set of each problem; completing bonus test sets may require modifying the templates. When this is the case, we make it clear in the problem statement.

### Tests
These are the inputs and outputs we use to test your program for correctness. Input files have the `.in` extension and corresponding output files have the `.ans` extension with the same file name. Test files are categorized as sample (visible to contestants during the contest) and secret (everything else) under the data folder in each problem subdirectory.

### Executables
These are custom scripts used to change the behavior of the judge for nonstandard problems. The `run` script changes how submissions are run, and is modified for interactive problems. The `compare` script changes how outputs are checked for correctness, and is modified for problems with multiple correct answers.

### Submissions (All Problems)
|File|Description|
|---|---|
|`submissions/accepted/*`|These are programs written by us that implement different approaches of varying efficiency in multiple programming languages to solve each problem. As a result, some solutions may pass more test sets than others. Solution files are named `[problem name]_[solution name].[extension]`, where `[solution_name]` is a keyword that describes the solution, and `[extension]` is the extension used by that language's source files (for example, `.cpp`, `.java`, or `.py`).|
|`submissions/runtime_error/*`<br>`submissions/time_limit_exceeded/*`<br>`submissions/wrong_answer/*`<br>`submissions/bad/*`|These are implementations written by us that do not pass for various reasons. They are used for debugging and making sure that flawed submissions are unable to pass.|

### Editorials
Editorials describe and explain several approaches of varying efficiency to solve each problem. They are named `[problem_name]-editorial.pdf`.

### Directory Tree
```
[contest name]
├── [problem name]
│   ├── [problem name].pdf
│   ├── [problem name]-editorial.pdf
│   ├── submissions
│   │   └── accepted
│   │       ├── [problem name]_[solution name].[extension]
│   │       └── ...
│   ├── templates
│   │   ├── [problem name]_template.[extension]
│   │   └── ...
│   └── data
│       ├── sample
│       │   ├── [test name].in
│       │   ├── [test name].ans
│       │   └── ...
│       └── secret
│           ├── [test name].in
│           ├── [test name].ans
│           └── ...
├── [problem name]
│   └── ...
└── ...
```

## Credits

Under construction!
