# ReleaseNoteAutomation
It is a self-project to generate release-note automatically.
When I search how to generate release-note, I see that the release-note is generated in many of big project by automatically. If you wanna generate release-note easier. You have to follow some steps. 

# My Road Map
## 1) Commit Message
You have to declare an annotation list and each developer have to obey it.(not necessarily for all changes/commits). 

I will follow the annotations writen in the [1] link.

[1]

|Annotation|Description|Example|
| ------------ | ------------ | ------------ |
|[INTERNAL]|used for internal stuff|git commit -m “[INTERNAL] my internal change”|
|[FIX]|contains a bugfix|git commit -m “[FEATURE] my new feature”|
|[FEATURE]|contains a new feature|git commit -m “[FEATURE] my new feature”|
|DOC|contains documentation|git commit -m “[DOC] my documentation change”|


## 2) Version Control and Script Working
If you maintain many version in a same project, you need to get git log in different date and branch. 

Example: I have two project. I wanna use one script for generating release-note. 
1) Obtain Commit ID, where to start relese not. [From Spring 1: Commit ID to Today]
2) Declare the branch.
 [This information should be store in a xml file.]


| Version |Branch   |Commit ID   |
| ------------ | ------------ | ------------ |
|Community| generate_rn   |  sha1  |
|Enterprise   | generate_rn_en   |  sha1 |

Expected working:

generte_rn.py branch=generate_rn commit_id=3k9e3
Generating Release Note:
Start From 3k9e3 Commit ID to today's last commit i09id3
Release-Note
Version 1.0
Issues: 2 issue fixed.
Features: 1 feature added.

Bug
- #23234 Permisson problems solved.
- #43632 Incorrect translation corrected.

Feature
- #REQ1 GUI interface adapted
- #REQ2 Real time monitoring is enabed.





Reference:

[1]https://blogs.sap.com/2018/06/22/generating-release-notes-from-git-commit-messages-using-basic-shell-commands-gitgrep/

https://glamanate.com/blog/creating-better-drupal-module-release-notes

