[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=20244867&assignment_repo_type=AssignmentRepo)

Assignment is due by September 9, 2025, 11:59:59 PM Central Time. Late penalties as listed in the syllabus apply.

Code must be pushed to Github (your code must be viewable on GitHub.com) for it to be considered submitted.

The Gale-Shapley algorithm can be modified to accommodate many variations on the Stable Matching Problem. Your task is to implement the following two variations in Python. The code is turned in through Github Classroom. 

 You can get feedback on whether your answers are correct through GitHub Classroom. You may make as many modifications as you would like until the code is working correctly. Please write your name(s) as a comment in the first line of code in gs.py.

Note: you are permitted to reuse code from the gs method as appropriate.

## Task A: Forbidden Matches
 
 In this variant of the Stable Matching Problem, in addition to the set of men M and women M , there is a set F ⊆ M × W of forbidden pairs that are not allowed to be matched together. Using the revised definition of stable matching on p. 20 of Algorithm Design, implement `gs_block(men,women,pref,blocked)`, where `blocked` is a set of forbidden pairs, for example, of the form:
`blocked = {('xavier','clare'),('zeus','clare'),('zeus','amy')}`

## Task B: Coping with indifference

In this variant of the Stable Matching Problem, ties are allowed in the preference ordering. They are implemented by turning the preference list into a list of sets, where ties are placed into the same set. Implement `gs_tie(men,women,preftie)`, where `preftie` is a dictionary mapping people to a list of sets, for example, of the form:

```python 
thepreftie = {'xavier': [{'bertha'},{'amy'},{'clare'}], 'yancey': [{'amy','bertha'},{'clare'}],
'zeus': [{'amy'},{'bertha','clare'}],
'amy': [{'zeus','xavier','yancey'}],
'bertha': [{'zeus'},{'xavier'},{'yancey'},], 'clare': [{'xavier','yancey'},{'zeus'}]
}
```
Here, Xavier strictly prefers Bertha to Amy to Clare, Yancey is indifferent between Amy and Bertha, but prefers both to Clare, and so on.
