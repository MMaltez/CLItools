---
title: Common Command Line Tasks
author: Miguel Maltez
date: 20191104
---

## Find files with a certain string

Return name of file and line with matching string.
```
grep -r "string1"
```
This will go down te current working directory recursively.


Just the name of the files with the matching string.
```
grep -l -r "string1"
```
