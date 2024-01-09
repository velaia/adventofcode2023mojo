#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import numpy as np


# In[ ]:


input_sample = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

input="""??#.????#???.#?# 1,5,1,1,1
?##?##??#? 7,1
??????#???. 1,7
??#?#??#.?#.??#? 5,1,1,2
???????.??? 1,3
?#..##?##??###??#? 2,13
?.????????.???????? 1,5,1,6
?.???#???. 2,2
??#..#???#? 1,1,4
?.?##?????#??? 1,5,2,1
.???#?????##??#.? 3,8
?????????????.#.. 4,3,1
..#???????.? 4,3,1
????#??.?.#??? 7,3
#??#???##??.?? 4,1,3,2
??#?#?##?.???#??. 6,5
???.#??.??###?.#?? 3,1,5,2
?.????##??#?? 6,3
???..?##????.? 2,3,1
?.?#????.??#?#.? 1,2,1,3,1
?.?###.???? 4,2
?#???..??##? 4,3
???#????#?. 1,2,3
#???#???#??#???.? 1,10,1
???????????????????? 1,5,6,3
???????#??? 2,6
??.??.????.?#?????# 1,1,2,1,4,3
???#???.??#? 1,4,1,1
???#???##??##? 3,2,3
????.??????#?.#? 1,1,1,4,2
?.#??#???? 1,1,5
??##???#?.##??..? 4,2,4
??????#.????.# 4,2,1,1
??????#??#?.??? 2,7,1
.????????##.?.?.##? 5,2,1,1,2
.??????????#?#. 3,1,2,1
?????????????. 2,1,5
?##????#?.?????.#??? 2,1,2,3,3
?????????#?.?????#? 1,2,1,3,4,2
..?.#???.?##.? 1,3,2
.??????????????? 10,2
?.?#????#?.??? 1,1,2,2
??????.#??.?.? 1,1,1
#???#?#??#????? 1,2,1,5
???.?.??#????.? 3,6
.#.???###???.#?..??? 1,8,2,2
.???.??#????# 2,4,1
.????#?#?? 3,3,1
?###??#??## 4,2,2
??#?#???#???.??. 3,5,1
???####??##..?#.#.?? 9,2,1,1
??#?#???#.?. 5,1
???#????#???##?# 2,3,3,1
?#???????#???#??? 1,3,3,3,1
#???#????#.##..? 8,1,2
?????.?#?#??? 1,5
.??#.??#?.? 1,1,1
?#?#???#???.??? 1,1,4,1,3
.????#.?.#??? 1,1,2,1
.??#?.??#? 4,2
#????????. 1,4,1
??.#?#????#?...?? 1,8,2
?#.#?#.??##? 2,3,1,2
...??.?#?? 1,1
?.?.????#..? 1,2,1
?##????????.??.?#??? 6,1,1,4
?.??#.??.?.???? 3,2
.????.?????.???.?? 4,1,1,3,1
?????????##???????#? 2,1,1,2,2,2
???.?????.????? 2,3,5
???#??????.??#??.? 1,6,1,1,1
??##??????###??? 12,1
?.??.?????? 1,1,2
??#??????#?.. 2,5
???#####????. 1,8
.?#?##??????#??.???? 6,2,1
?.#??#???????#????? 1,1,12,1
??????????#.?..?##? 1,1,1,1,3,3
???????#???.??## 10,4
.?#????.?.???..? 1,1,2
.???#?#????? 2,2,1
#????#?.????##?#?# 1,5,1,5,1
???.##??????##??#? 1,2,8,2
??#????????????#? 6,7
????.??.#.?#?#? 1,1,1,1,4
??##?#??.#???? 6,1,4
?#?.?#????????#?. 3,2,4,3
..??????##?# 2,1,2,1
?????????.???? 4,1,1,1
.??#?????.?.?. 1,6,1
#.?#?#??????#??# 1,6,2,1,1
.#?.#.##??# 1,1,5
??#?????#?????? 5,4
.#??.?.?.? 2,1
.?#???##.????##?? 7,2
?#?.??????#??????# 1,8,3
?.#??#??.?#.. 4,1,1
?#?#?#??????? 7,1,1
?#???????? 6,1
????#..?#???##? 1,1,2,3
..?????#?###??.? 1,9,1
?##???.???#?# 4,4
??.??#???..??#? 1,2,1,3
#?#??????.??#?? 8,1,3
???#?##?#?? 2,6
.?.???#???.#?????? 1,3,1,5,1
?#.???????# 2,2,1
?.???.??.? 1,1,1
?#?#?#??????#??#??? 1,5,2,4,2
?#??.?#?????.?#. 4,6,2
#???.?#?#??#?.??#? 2,7,1
.??#...???????. 3,1,1
?..???##??. 1,6
??#??#?#??? 2,4
?.?.??.??????#?. 1,7
?.?????????.??. 2,2,2
???.?????? 2,1
???.??????????? 1,3,4,1
?#????#???#??? 10,1
??#???.?????#???# 6,3,1
????.?##??#??# 3,8
?????????????. 1,7,1
?..?????.#???.. 1,4,2
?.???#???#? 1,5,1
#???.????? 2,1,1
?#.??#?.???? 1,1,1,1
????.?#???.???. 1,1,4,2
.?#??#??.??????? 2,4,6
.??.?##.??#?#.??? 2,3,2,1,1
..??????#?.?? 2,2
???#?#??.##. 3,2,2
?..?????????##?#??? 1,13,1
??#?????#?.??#?????? 6,2,5,2
???.???#???# 1,1,3,1
??##????.?. 4,1
??#??#??#?. 3,6
.??????#????#.#.?? 1,1,8,1,1
?#?#?.?.?.###??#???? 5,1,1,3,1,1
???.#?#???.?? 1,1,5,1
?????####??????? 2,5,2,1
????.??#??#? 1,1,2,1
??.?????#?#.????? 2,3,3
?#??#?#?.????.??? 2,3,2,2
?????????#??.??????. 1,6,1,1,1,1
???.##?##??#? 1,6,1
????#?.??.. 4,1
?#??#?#???.????#?# 4,4,6
?????#??#.#? 1,2,2,1
?#?#?#??###??? 1,1,7
.##?.????? 3,3
??#???###????? 1,6
.?###????????##?#?? 7,1,5
..?#????????#? 3,5
#?#???.??? 1,1,1
#???????????#??.??? 10,3,1
???##??#??#?.?????. 10,3
?#?????.???????## 3,2,5,3
??.??#####???. 2,8
???.?????? 1,1,3
???#???????????. 6,4
#???#?????##???.?#? 2,1,1,5,2
?#?..???#??????. 2,7,2
?????##?#? 2,3,2
.#?..????# 2,3
???????#??#.?..??.. 3,1,1,2,1,1
?.#??#????? 1,3,2
???..?.?.? 1,1,1
?#.?#??#???.##.? 1,1,4,2
???#?#.??#??? 4,1
??????#????.???? 6,1,1,1,2
???..??.#???? 1,1,1,2
????????.? 1,1,1
?..#??.??. 3,1
?##.??#??? 2,1,1
?????#?????#?#?? 2,12
?#??????#???.?? 1,6,2,1
#??.???.??##???.#? 2,3,7,2
???????..????#????? 2,1,1,7,1
????#??.?????? 1,2,4
?###?#?##?##??.??. 12,1
?#??#.?.??#?... 3,1,1,1,2
??#??#??#????#? 9,2
???????##????? 1,1,5
?.?#????#?.??.?? 3,3,1,1
???..??????#..??#? 1,1,7,1,1
??.???###???#..? 1,1,5,1,1
??.??.#????#????# 2,1,7,2
??????#?#??????# 1,6,1
#?.?...??.??????? 1,1,1,6
??#?##??#?..## 7,2
?#?###..?.#?##??.?.# 5,6,1
.??.?.???. 2,1,1
?.???..?.?#?.??.???? 1,3
.#?.??????.?.?#??? 2,6,4
???##...??. 3,1
????????????#?????. 4,6
????#.??#? 1,1,1
?.?#.??..??#?????..? 1,2,1,8
?????.??.? 1,2,1
??????##?.?? 1,4
???.????#??? 1,1,5
.??#???.#.#??#??. 6,1,2,1,1
?.????#??##?????? 1,1,1,7
??????##.??? 3,2,1
?.????#?????.?.? 1,4,2,1
?????????????## 1,1,2,4
.?##??#??.??# 4,1,3
??#?##??#?? 2,5,1
?????.###??.?.#??# 1,1,4,1,1,1
.????????##?#? 1,7
??????????.? 7,1
.?????###????..#. 12,1
????.????? 3,1,1
#.??#????#????#????? 1,5,1,7,1
.##??????.??##? 7,3
?..?.???#?????###? 1,1,5,5
??????#???. 1,1,3
??.#???????##????. 1,2,3,6
?.?.?.?.#???????#?. 1,1,1,1,2,7
?????#????????. 1,1,1,4,1
?.??#??#?? 1,1,2
??#???.#.?#?#?? 1,1,1,1,5
?????????.? 4,1
??.?????#?.?.#?? 7,1
??.?#.?????#??. 2,7
?????##..? 1,4
?????????. 4,1
??.?..?#???? 2,3,2
????.####??###? 2,4,4
?####???##??????? 10,1,1
???#?#???# 1,5,1
????###.??.?????#??. 6,1,6
#???????#?. 2,1,4
?#?.???##???????#? 3,1,2,1,6
???#??#?.?.?????? 1,5,1,1,4
?.#???##???.?.## 1,3,2,2
???..##?.?.? 2,2,1
?.#?#?????. 3,1
????.##?#?#??##?? 3,12
#?##???????? 1,3,3,1
???.#?.????##? 1,2,1,4
???.??#???? 1,3
.???###??.???????# 7,5,1
?#.??.?#???##?. 1,1,1,4
.????###????? 2,6
???#???.???????#?? 1,2,1,3,4,1
.?.?????????? 3,5
??#???#?.###????.?? 7,3,1,1,1
#??###??#?#.????? 11,1
#.?????#??#.##???.? 1,1,7,5
??????.????#???? 1,1,4,1,1
?.?#?#?#??###?? 7,4
????#???#?#?###????? 1,2,10,1
????#????? 1,4,2
???.#??#????.?#??.?. 3,2,1,1,4,1
?????.?#??????. 1,2,1,1,1
?#???????#?#?#???.? 2,12
?#??..??.???###?? 4,2,1,5
##????????#.? 5,2
#?#?.?.??###??#?. 4,8
??##?.???? 3,4
?.????##???????? 8,1,1
#????#??#???#?#.??? 15,1
?.?????.#? 4,2
?.##???..?? 1,3,1
#????#??????????#?? 2,7,2,3
???.????#? 1,1,2
??..#?????### 1,3
????????.?? 2,4,1
#??##??#.?????.??? 1,5,2,1,1,1
???#.?#?#?. 3,1,2
?##?#??????#?#.# 3,3,3,1,1
??.#?..??? 1,1,1
?#??.???#? 1,1,3
???#???????.??##?? 8,3
??.#.?#???#??.? 2,1,7
??????.####?.?#?# 4,4,4
??????????? 2,2,1
?#?.??.???.? 2,2
????#?#?## 6,2
.??###??????.? 5,3
.???#.#????? 3,5
?##?#?.?#?#??. 6,2,1,1
#.???.??#?####?..? 1,1,1,8,1
????#???#???# 1,1,2,3
?????.??.#???#? 3,5
?#??..?????????#?. 1,1,3,1,4
#?????????????.?? 6,1,1,1
?#?????..?????#??# 3,1,1,5
???????.???????????? 1,4,1,9
.????????????.. 2,1,6
.?#??????. 2,4
??#??#???#.???#? 1,5,2,1,2
.?.???????.?.#??? 4,1,2
##?.??##?..???. 3,4,3
??..??#??#?. 1,6
??#??????????##???? 2,6,4,1
??..????##?????? 1,5
##????????.??.#??? 2,6,4
?#??#...?????# 2,2,1,2
?..??????.???.?# 1,1,3,1,1
.?###??#???#???? 7,4,1
?#?.?????. 2,2
??..????.?????# 1,1,2,2
??##.#??????.##??#?? 1,2,1,1,1,5
??.##??????#???#??? 4,8
??#?????????. 4,3,2
#????.???? 1,1,1
?..??.?????? 2,3
??????#??###???? 1,1,9,1
?????#?#???????.. 1,6,3
?#??.???#?##. 3,3,2
?..##?#???????#?? 9,1
???.?#?#?#?. 1,5
???##?#???#?# 8,3
?##??#??.??.???????? 2,3,1,6
.??...?????????#.#? 1,6,2,2
????.#??#?#.##?. 1,1,1,3,3
?#?#?????.??????. 5,3
??.????##???. 1,5
????#?.???? 2,1
????..??#???. 4,2,1
???????.?# 2,1
????????????? 1,1,3
???##??????###.?#? 2,2,2,3,1
??????#?#?#?#?## 3,10
?????#??..????????? 8,5
??##???????.??? 6,1,1,2
?.???.????.??? 3,1,1,3
.?.???.??? 1,2
.???###???#??.?? 5,1,1,1
????#?.##?###.# 1,3,2,3,1
.?#???????? 1,4
?#?#?????????### 8,6
?????..???.???? 4,3,1,1
..?#?.?#??? 1,5
.????.??#? 3,3
?##????.?#??????..?? 7,3,3,1
?????##??.?.??...?? 9,2,2
??..#??####??.?.?#? 8,2
??????##????? 1,1,6
??????#??.???#? 7,5
???#..??.????. 4,1,2
.#?.?###??? 1,4
????###?...?#?#? 8,4
?????#???#??????? 1,1,6,1,1
.??#?#?##??????? 7,1,1
.#.?????#.?#### 1,2,1,1,5
?#??..#??.#?? 3,1,1,1
????#??.???. 3,1,3
#.???#???. 1,2
???.???##.???.? 1,1,2,2
?#?#..?#????##?.?. 3,9
.?.??.????? 2,2
??????.?.##?#?.? 5,4
???#???.????? 7,1
??####?????.???#?? 6,3,4
?.?...?#.#?#??? 1,2,5
??.??#??#?#?#??.?? 2,3,7,1
?#?.???????? 1,1,1
????????#?##?#??? 1,2,9,1
#???.???#????.??#??? 3,1,1,1,4,1
.??#?.?.#??? 2,1,2,1
.?##?###.###?#?.??. 6,5,2
.?.???????#????##? 3,10
?.##???..#? 5,2
????????????#??.???? 1,1,10,1
??##??#.??#??#?? 5,3,2,1
?#???#.??????..# 6,4,1,1
????????.? 1,2,2
?????#??#??#????#??? 14,2,1
???#??.???#?#???? 4,7,1
.?.##?.???#??..????? 1,3,4,2
??????#??????? 1,1
..#?##??.????. 5,3
??????????#.? 4,1
#????.???.? 1,1
.?..?#.??? 2,1
?#.??##??.##?.?? 2,4,2,2
??#????#??????? 9,1
.#?.##?##.#???? 1,5,1,1
?#?###???#??#?.??? 11,1,1
???#??..?? 3,1
#?#??????#?????#? 12,2
??#?#?.???.? 2,2,3,1
?#???.?.??#?#???? 5,1,8
.???#?#??#?????. 10,1
??????.?????.? 5,1,1,1
.?.??????????# 3,7
.#?.??..##??.?#..#? 1,1,4,2,1
?##?#??.??###?????# 2,1,1,1,7,1
?##?.???.? 2,1,1
?????#.#?##.?#? 1,1,4,1
?#?.??.?#.#.##.? 2,1,1,1,2
???????.#.??##??.?. 6,1,3,1,1
.?#??#???????#???.#. 3,1,1,2,4,1
?????#?.##??##??.?? 1,2,2,3,2
#??.???????? 1,1,1,1
????#?.##?.?#?#?# 5,2,5
.?.??.#?????????..?# 1,1,6,1,2
???#?#?????. 7,2
???????##??#?.?#?.? 1,8,3
.?..?#?#???? 4,1
??.?#??.????. 1,1,3
????##???##???#??? 12,4
?###?#??..#?.??? 6,1,2,1
##??..##?#????# 3,2,1,1
?????#?##??##???#?? 2,13
#?..???##???##?#???? 2,6,4,1,1
.????.?....#????. 1,3
?.?.??#??#.?# 1,2,1,2
???#??.??#.? 1,1,1,2
.????#?#???#??????? 12,1,1
?..#??#?##??#???? 1,1,2,3,5
.#??##?##??????.?# 2,11,2
.?.#?#?.?#???#.? 1,4,6
?#.##??.????? 2,4,4
???.??????.??. 2,1,1,2
???????.?##.#???.? 1,1,1,2,3,1
??..???????#?.? 5,2
?????#????? 3,2,2
.##????..#??.. 6,2
????.??????.???###? 3,3,1,5
??????#?.???# 1,3,1,1
????#????. 6,1
??.?#????. 1,4
??????#???##???. 6,1,3,1
?.?#.????. 1,1,4
?##??.#?#??.#?? 3,1,1,1,1
?.?#??????. 1,5,1
???????#?. 1,4
???#????#?##?#?????? 2,2,1,1,6,1
??##.?????##??#.? 1,2,7,1
????????.# 4,1
.???#????? 1,1,1
?.?#??.????.?#?? 1,4,2,2,1
.?##?#???.??..?#? 3,3,3
?#??.?.?#??? 1,1,4
????..#????#.?? 1,1,1,3,2
???#?..??? 5,1
?##???##.?. 3,2,1
??#???.???### 2,1,1,3
????.?#??##?. 2,2,2
?#???##??#?????#.??? 2,11,1
???#??..?##??# 5,6
????.??#???.#?#.?#?# 2,5,1,1,1,1
?.??????#??? 2,3,2
#.#???..????????. 1,1,2,6,1
?.?..?.#??????##?? 1,1,1,1,3,5
.??.?.???? 1,1,4
#??#.?#?#???#??????# 1,1,2,1,1,8
?????.?#..#. 3,1,1
????##???.?????.. 5,3
.????#???????? 1,5,1,1
##?..#.???#?????? 3,1,1,2,1
#??##???????????. 1,11,1
????????#. 2,1,2
.#?#?????????. 1,4,2,1
#??#??.????????????. 5,5,2
..?#?#???#???????.?. 9,1,1,1
?#?.?????????... 1,6
??###??#?#?.? 5,2,1,1
.?????????.??... 6,1
?.?.#??#??????#?#. 1,2,7
??.?#?.#??.??. 1,2,2,2
?##?#.?#?. 3,1,1
??.??####???... 2,6
.?????#????..?..??## 7,1,3
.#?##???.? 5,1
?.?.???#.???. 1,1,2,1
?????.???## 1,3,2
.????#??.??.?. 5,1
.?#??.???? 2,4
??#?.??#?? 2,2
?.??.??????.?????? 1,1,2,1,1,5
?????#??????.??? 1,5,2
#..?#??.?# 1,2,1
???????#???#?#???.? 5,8
??.?#??#?? 1,2
????#.#??#? 3,1,1
#?#?..?..?????#??? 4,1,2
??????.?##?##.??? 1,4,6,1
?.????###??? 1,8
??##???????##?????. 8,4,1
?#.?#.?.?????? 1,1,1,6
???#?.?.#??##???##? 2,10
.?????#?.?##????#?# 1,3,2,5
#?.?.?#?..???#? 2,1,1,2,2
..???#??.??#?? 5,3
.????##??? 7,1
??#?###???# 7,1
?????????????????. 10,5
??#?#?????????###?? 3,1,1,1,4,1
????##???.#??? 1,6,1,1
.##??????##?..??#?## 11,2,2
?#.????????? 2,1,1,2
??????#?.??#??..???. 3,1,5,3
.?##??????????#???? 3,1,1,1,2,1
?#?...?#?????#?.? 2,8
###?#.#?#?????.#???? 5,1,2,2,4
?.???#?#.?????#?.? 6,5
#????#???#???#?#? 2,2,3,3
??#??.??#.?#? 2,1,1,2
##.?...????????#?#? 2,9
??#?#???#???? 4,1,1,1
.???#?.?????.?#?.#. 4,1,1,1,1
??#.?????#?????##? 1,1,1,7
#???????#?????#? 1,1,8
????##?#?#??##???#?. 1,8,6
#.???.?????.#?? 1,1,2,3
##?????#??.????#? 2,1,3,6
#???###?##.? 1,4,2
#..??????#???.. 1,10
?????#???.?#?#??# 7,7
???.#????#?????.#? 1,1,1,6,1,1
??.#?#?????????.?# 1,4,2,2,1
?#?#?..?#? 1,2,2
?.?##.???###?? 3,5
.?#????#??..?? 2,5
???#.#??.?.????..#?? 2,3,4,1,1
???#..?????.? 1,1,5,1
?##?#??????##? 4,1,5
??#.#?###?##?????#? 1,1,8,1,1
.#?#??#.#?.? 1,1,1,1
????????#?#?##??# 5,1,1,5
.??#?.?#?????.?????? 3,7,4
?#?????#.?#? 2,5,2
????.?#????#?????#? 1,9,2
?#????#???.??.??.. 7,2,2
?#.##???????.?#.? 2,5,1,2,1
?.##?#?.????#?#??. 2,1,6
?###??#.#????##.?? 5,1,1,1,3,1
.??#?????#???#?.# 3,1,2,2,1
?.????.??.#?????? 1,3,1,5,1
????##?##?? 6,3
.?#???.?.????? 2,1,4
?????...??.. 1,1
??#????..??# 1,2,2,3
?###.?????#.???#? 4,3,1,2
???##????.?#.?#??? 1,2,2,2,5
?#.?????.?###?##??.? 2,5,6,1,1
.????.??.?????????? 3,10
??.?#?#.#..??? 1,3,1,1
?.?#?#??.?. 5,1
???#.?????##???#??? 2,13
??#???#.#???#???#?? 2,2,11
?#???????? 4,1
??????##???##????# 2,10,1
???#????#?? 3,1
##????#.?.? 3,2
.????#?????? 6,1
?.??.????#? 1,4
?????????.? 1,4
#?#??#?##????#????#? 14,3
#..#????#??? 1,1,4,1
.?.##????.?? 1,2,1,2
???.#??#?#?.?????? 1,1,7,1,1,1
..?#????.#???##????? 3,2,7
?????.??.? 3,1
.?#??#?#..?#?.?##.?? 2,4,2,3,1
???#?????.# 8,1
????..##?.??#? 1,2,3
.?????.?#? 1,1,1
??#?.#?#?#?.###?. 1,5,4
???.#????##.???##? 1,3,3,5
?????????#?#?????? 7,2,1,1,1
#.?##.???.?#?..?.#. 1,2,1,2,1,1
???#.???.?? 1,1,3
??.?.??###??.????.? 1,1,7,1,1,1
.?.#.?#?##?.???# 1,1,5,1,1
???###?#???# 8,2
?.????.#..##??? 1,1,2,1,4
??#????####???#?. 3,8
#..?#????##?#?. 1,3,3,2
###.??.##.? 3,1,2
???##?.????#?#??? 4,5
?.??.?.?.??? 1,1,1,1
.#???##??#???##???? 1,1,5,4,1,1
?..##..??#...?.?.?? 2,1
?#..#???.?.??# 2,2,1,1
????#?.#??.? 1,3,1,1
?#?????#???.????? 3,3,1,2
#.????###???.?#???? 1,7,2,2,2
?????.?????? 3,1
.??#???????. 3,1
?.?#??.?#???##?#?? 1,1,1,11
?#????#?#. 4,1,1
..#?###???#.??? 1,7,2
#....????? 1,1,1
?.????????.? 4,1
##?.??????.#??? 3,2,1,1,1
?????.?#.?????#??.. 2,3
?#??##?#?#?.??##? 7,2,3
.?.?????##.??? 1,2
.#?##?##?.?????.?#.. 7,1,1,2
???..???#?. 1,1,2
...?.???#?#? 1,4
?????#????#.? 7,2
??#????##???##. 3,2,4
???.???????. 2,1,1,1
###?..?????.. 3,4
.???????????..?. 4,2,1
?.?.#??.?? 1,1,1
?????????????#?? 6,6
..#?????.??? 4,1
???#??#?##.?#?.?? 7,3
#???###??????#?? 1,1,3,2,3
?##??.??#??????#???# 3,9,1
???#??#??.??????#??? 7,3,1
.???###??##?#.?.??? 6,2,1,2
?.?#?#?.?.?#? 3,2
.??#.?###???##?? 2,5,3
????.?????#??###?? 3,12
?#?##?#..#??#?? 5,1,1,2
??#??...???#?#???. 1,7
???##???.???#.?. 7,3
??.#???#.# 1,5,1
??###???????????# 5,4,3
#??..#??##.?????.? 1,1,5,2,1,1
????#.???#????.. 3,4
#?????.#??? 3,2,3
?#?.???????. 2,2,2
?.?????????## 1,1,4,3
#????????..#?#????? 3,1,1,3,4
???#??#??????????.. 7,1,1,2
?##.??###???#?#??# 2,1,3,1,3,1
?#?.???#?#?#?.??# 3,5,2
??#????.??#?#? 3,3,4
###?##???#?#??.?.# 8,3,1,1
.??.?#???#??? 2,1,3
.???#??###?? 1,6
???????.???????? 7,1,2,1
.??###?.??#.? 5,3
?#???#???????#?#???? 2,5,1,4,2
????.?????#?????? 1,1,7
.??.?.?#?##?#???#?? 1,11
?????#???? 5,2
?.??.???.#?? 1,1,3
????#???????? 5,3,1
#?##????#???#?.?#.# 4,3,1,1,1
??#??????#?? 1,1,1,4
.????.#?????#?? 1,2,1,1,3
????????????????? 1,4,3,2
????.#?.##?##?#?#?? 3,1,5,3
??#?###??? 1,3,1
????#???....? 8,1
.????.???.???..???. 2,3
?????.??#? 4,2
#??.#.????#.???###? 2,1,1,1,1,4
.???????.??????# 6,5,1
??#??#?????.??#. 1,4,1,2
??#?.??.??????#?#??? 4,1,3,1,5
?#??#???????#..??? 4,7,1
???#?##?????.?? 5,2,1
.?###?????#?##??. 6,7
#??#..??????#?? 1,1,7
.??#?#??????# 4,1,2
.###??####????#???# 4,13
????#?????.?. 6,1
#?##???#????? 5,1,2
??#?.##??????????? 4,4,5,1
.????#???? 2,1,3
?.?#.???????#?.????. 2,4,1,1,3
?.?#?????##??????? 2,10,2
?????..???##? 2,3
?#.#.???#???.? 1,1,1,4
.?##???##?????###??? 15,2
?#.#?.????.??.?#?.? 1,2,3,1,1,1
????#??????. 5,1
?.#.????##??.?. 1,7
??.?#?..??#?????.? 2,6
???##?.#?.?#? 3,2,2
?#?.???.?? 1,2
?????????..?#??? 1,1,2,2,1
?#.??..??? 1,1,2
??.????##???? 1,1,3,1
??####??????#.?.??? 5,1,1,1,1,1
.??#????.?# 2,1,2
..#?#???##???.?.??# 1,1,4,1,3
??.##..??. 1,2,2
?#???#?????? 2,5
????##?#?.???.? 5,1
.?#?..????#??.??? 1,4,1
.#####??????#??. 7,5
???.?.?.##?#???. 1,5
????###??.????#?? 8,5
?????#.???#?.?.?# 4,4,1,1
????????.?###????#? 1,3,4,1,3
?.?????.?#?????# 1,3,1,2,1
??.??????????? 1,3,1,1
???.?????#??? 1,6
?##???#?#????#????#. 3,3,3,2
??#?.?.???### 2,1,3
#??..?##??????.??? 1,1,3,1,1,1
???#??.?.#???#? 6,1,2
?#?..????? 3,2
?##??#???? 5,2
??.??????.?#? 1,4,2
.#?##???.???#??????? 7,4,1
?.#???..????? 4,3
.???..?#??##?? 1,7
.#???????.??? 1,1,1,2
?#?#???????##. 6,3
#.?.#?????#??#?#???. 1,1,1,6,4,1
.???????.?#?#??????? 2,5
??.?.?????? 2,3
???.????..#? 1,1,1,2
??#??.?#?..???##??## 2,3,8
#??.?.?#??#?. 2,5
?.????.????????? 1,2,3,1,1
???.??.??????????#. 1,1,1,3,3
???????.??? 1,1
##??#????????.?????# 2,2,6,1,3
??.?????##????## 2,1,1,8
???.??#?????#??.. 1,3,6
??#?#??#???????.? 7,1
.?#.????#??#? 2,4,2
?????.??#.??? 1,2,2,1
??##???.????????. 6,6
..???..?.?.? 3,1
??#?.??????.. 2,1
???????##?????. 1,1,4,2,1
??##..??#???. 2,4
?????#??????#? 1,2,4
..??#???#?????#?? 3,2,5
???.??#??.???#?#??? 2,5,6,1
?#?#.??##.?. 3,3
#??#.?????.?? 4,2,1
?#???.?#???#???.. 4,9
????.??????#?#??# 2,7
??#.??????????????? 3,7,5
??#????###? 1,4
???#????#.#.??.. 1,3,2,1,1
???#?.???? 1,2
?.??.?#??? 1,3
??.????#??#.?.? 1,2,1,1,1
..??????.?? 4,1
??#?.???.???? 3,1,1,2
?.????#????#? 4,3
?#?????????????? 5,4,1,1
?..?????#? 1,1,1
?.?#???.?? 4,1
#??#.????? 4,4
#??.?????????????? 2,1,1,3,2,2
.???#????.?? 1,1,2,1
??.?##?.??#??#?#??.. 4,10
????##????#???#.???? 2,3,2,1,1,1
????????.??###?????? 7,5,2
????.?.#??? 2,1,1
.#?..?#????#???## 1,12
#???##??.???????? 1,5,2,1,3
???#???#?.#??..? 7,1
?#????.???.?#? 6,2,1
.#?????????#???. 6,1,3
???###????????#?#?#? 8,2,1,4
?#?#..??#???. 4,1,3
.???##?#.??? 1,4,1
??????????? 5,1,1
??.#?#.???? 1,3,3
.#.###??????.#? 1,4,1,1,1
???#??.?.????? 1,3,4
?#.#????????????# 1,1,1,8,1
.??????###? 3,3
.#???????#???? 3,1,4,1
??#??.?#???#...? 3,6
?#???????.?#???.???? 9,4,1,2
???#.??#??? 4,3
??#????#?#.??.?# 1,3,4,2
????#?##?.??????? 6,1,2
.??##?#?###..#??.?? 3,5,2
??###???##?#?.??. 12,1
?..#?????#????#?# 2,1,2,4
????###?.?#??#??#. 8,6,1
????##?#????# 10,1
#?##?..?##?? 5,3
?#.?#??#???????? 1,7,2,2
.#?..?#?#??#. 2,6
#??#????.??#?#. 7,3,1
.?.??.????. 1,1,3
?????.???#?#??.?? 1,3,4,1,2
????????????#??#?? 4,8
????####?#? 1,7
?.#????.????#?.?? 1,6
?#?????#?##?? 3,4
?#????#????# 9,1
?##?#?????.??? 6,1,1,1
???..?##?..?????? 2,2,3
#.??.??????? 1,1,2,1
?##???##.?###? 3,2,4
#?##????#.? 6,1,1
.????.??###???#? 1,2,5,2
?.#??.??#???? 1,3,4
??##????#???#?#??? 4,7
?#?.???#??##???#?? 1,1,2,8
???.?#?##????.? 1,7
#.?##?#?.#.????# 1,5,1,1,3
#???..??#????#????? 4,5,2,1,1
???????.???????#? 1,3,1,2,1
##???????? 3,1
?#..?.???? 1,1,1
..??.#???##???#. 1,10
.?????##?????#????. 7,4,1
??..#?..#.#.#?. 1,2,1,1,2
????.?###?#??. 2,8
????.#?????? 3,6
??#??#????#.?.?#.??. 10,2,2
???#??????????? 8,2
???.????#??..?. 1,5
.?.??..?#. 1,1,1
#??###..???#???? 6,1,1
???###?..#?#??????? 5,7,1
????#??#??#?#?.??#? 1,1,2,5,3
????#??.?.?#???#. 7,1,1,1,1
?##?#?#?.??#?. 6,1
???????#?#???.# 1,4,1,1,1
???????##.?# 9,1
.?????#.???. 1,2,1,2
#.?#.??#?? 1,1,1
?##?#?????? 5,4
?.?##??.#? 4,1
?????##???.#?.##? 1,5,1,2
??????.??? 1,1,2
?.??.?#?#?#.?##??#?? 6,8
??#???????????.?? 8,1
#????????###??#??#? 1,2,8,1,2
#.#???#?#?#.?????#? 1,9,1,1,1
#.??#???##? 1,7
?????##?????????#??? 6,1,2,4
????#?##??????#?#?# 2,4,3,3
?#?.##????#???? 1,3,2,1
?.?.??#?.? 1,1,1
???????#?#???..??? 1,4
???.?#??##?#?##.#? 2,10,2
??#?#???..???.??.? 7,1,1
?????????.#.??????.? 6,2,1,1,3,1
?#???##????# 2,6,1
#?###?#??.#??..#.? 7,1,3,1,1
???.???#???#?? 1,5,1
??????#??????.???#? 7,4
#?????#??.???#.? 3,3,1,1
?.?..??.?##????.? 1,1,3,3
?##????.???? 7,1,1
?.?##.?#?#?????? 3,3,2
?.??.?.??? 2,3
?##?..????? 3,5
??####?..?? 4,2
???.???????????????. 1,7,6
#???####???.# 8,1,1
.#.???#?.????.? 1,2,3
????????????#?????? 2,3,9,1
#?#??#????????? 1,5,1,1,1
.?.????.?#.?. 2,1
????..#??? 1,1,1
??##?????#???? 4,7
?##?????.?#? 5,2
???????###????##?# 3,1,6,2,1
##?????.???. 4,2,2
??#??.??#?..# 1,3,1
????.#???????#?.. 1,10
####??###????#.???. 5,3,3,3
?#.?#???.?#? 1,4,3
#.?#?#???#.#??????? 1,4,2,1,1,1
??#????#?###???#?# 5,11
??.???#???#????????? 1,5,3,1,2
.??????#???####?.#?? 13,3
.??????#?#?.??.?#? 10,1,2
??..??##?#??????.??? 10,3
????#???#####?????.. 10,2
????#?#??#???###? 3,7
????.#?.?????#.? 1,2,6
???????????..? 1,4
?.???#?????.? 1,2,1,1
#??#??#?#???#?#.?? 1,8,3,2
?????###????.???? 1,5,3
???###?#?##????.??.? 1,9,1,1
.?#?##???#????##??.. 9,3
.?.?.?#????????##?. 1,1,1,1,1,4
?.??.??#????##??##?? 3,6
??????#?????.#?? 6,1,3
?#?#???????.?#?.???. 11,3,1,1
?.?#..#??????.??. 1,1,6,1
??????#???### 3,8
???#?#??.??##????#?? 8,1,8
.#?.??.??#? 1,3
?????.??????#?????. 2,1,1,10
??.#????#.? 1,2,1
???#?????????#?#?? 4,8
..??..?????.### 1,2,3
??.???#???.??# 1,7,1,1
?###??..?.??#??#???? 5,4
????????#?..?? 2,5,1
???##?#?????#### 2,2,1,7
?????#???#? 5,1,1
??#.?#???####??#??.? 1,11,1
?#?????##?#?? 5,5
??.??.?####?. 1,6
.???????#?????. 1,6,1
????#.?????.??.?#? 1,1,1,2,1,2
???.?#?????#.?#?.??? 1,4,1,1,2,3
.#??????.#?? 1,1,1,1
..#?.??????????? 2,5
.??##???????. 3,4
??#????#??????????.. 1,4,9
.??#??.#.?# 2,1,1
??.??????.?#????? 1,4
#.?#??#???##? 1,2,7
?###??.#.??. 4,1,1
???#???#???. 7,1
?????????#??? 4,4
???.???????#.? 1,3,2
?#??????##? 4,1,3
?#.??.??#?.# 2,2,2,1
?.#?????.????? 2,1,5
?.#???#.?#?## 1,1,2,5
#?#.?##???????#??.# 3,3,1,2,1
#?#???.?.#.#??# 5,1,1,1,2
??##?.##?????? 2,7
.??###?#??#???? 5,1,6
?.???#?????.?#??? 1,6,2
??.?.?#??.???.???? 1,1,1,1,3,1
???.???.###?##???## 1,1,1,6,3
#???#??##??# 6,2,1
??##??.##????? 3,7
?#?#?#?.???##???.?#? 4,1,7,2
.??#?#????.?##.? 8,2
.???#???.. 1,1,1
.????#??.#?#?. 2,4
#?.?????????..?? 1,1,1,4,1
?#???#??.? 1,2,1
#???????????.???.? 4,3,1,1
????#?#???#???#.?. 12,1
???.??#.?#???#? 2,1,7
??#?.#??.?#?. 1,1,2,1
??#.???#.?? 2,2
?????#??.????? 7,4
?#?????????###?????. 1,1,1,1,5,2
.?#?.#???? 2,3
???###?#?..??.#?# 2,6,1,1,1
..#?.???#?#???#??? 1,12
????##.???? 3,2
?#?????##?????? 1,2,5,1
??????#???# 3,1,3
.##??.???.? 3,1
???##????...??..??? 6,2
???????#???. 1,4,1
?#??#???##?.??.# 10,2,1
?.?.???#??? 1,1,3
?#?#?#??..?? 8,1
??#?.???????#?? 1,10
?.#???#?#??????? 1,2,4,1,3
#?#?.?##?????. 4,6
#?#??.???#? 3,4
?.?????#?#??. 1,8
?.?.?.#.??.??#? 1,1,1,1,3
?#???##??????##???.? 9,4,1
?#???????????.? 5,1,1
#???.??#?#????#?#? 2,1,11
??#???????#???????? 6,1,7,1
?#???#???????#?. 1,4,1,2
????#??.???#.?? 6,2,1,1
???.?#????.# 2,2,1,1
#???#..??#?#????.? 5,7
##?#..???.??.#?# 4,1,1,3
.?..???????.????.?.. 2,3
.???????.?? 4,1,1
.?####??#?? 4,1
??????#????#???? 1,1,6,3
??#???#.????#??. 6,2,4
?????????.#?? 5,2,2
??#??..??????? 3,3
.#?.??????#???. 1,2,1,1,1
????????.?#????? 1,1,1,2,2
?.??.??#??#?? 1,5
.???#??????# 1,1,5
?#?????.#?#?????? 2,1,1,3,5
???#????#????#??#?## 1,1,4,2,5
?.??.#.????..? 1,3
??????#?#??? 8,1
??#??.????#??.? 3,5
?????#.?????#?#???.. 2,2,6
????#.???. 1,1,1
???#?.???#????# 1,2,9
??#?#???###????#? 1,3,1,8
#.???##??##? 1,1,2,2
????#?????.#?.. 5,2
..????.?????? 3,4
????.??????? 2,1,2
.?#??????????.? 7,2
???#??????#?? 2,2,4,1
???##?????#??#?. 1,9,2
#????????.#??.? 1,3,1,1,1
.??.#???#?##??.?? 1,2,2,4,2
???.?????#. 1,2,2
????#????.??? 5,1,1
.????.??#?#?#???.? 3,5,3,1
??????##??#.??? 1,2,5,1
??????##.??.????.? 8,2,1
?.?.?.?#?#?.????#?. 4,6
..?????.?#??? 1,1,5
???#?????????# 1,6,4"""


# In[ ]:


current_input = input_sample

sample_row = "??????##??#.??? 1,2,5,1"


# In[ ]:


def arrangement_to_checksum(arrangement: str) -> str:
    beg = 0
    result = []
    while m := re.search("#+", arrangement[beg:]):
        span = m.span()
        beg += span[1]
        result.append(str(span[1] - span[0]))

    return ",".join(result)

assert arrangement_to_checksum(".#...###..##...") == "1,3,2"


# In[ ]:


def num_damaged_from_checksum(checksum: str) -> int:
    return sum([int(val) for val in checksum.split(',')])

assert 9 == num_damaged_from_checksum(sample_row.split()[1])


# In[ ]:


np_sample_row = np.array([i for i in sample_row.split()[0]])
damaged_known = len(np.where(np_sample_row == "#")[0])
damaged_this_line_target = num_damaged_from_checksum(sample_row.split()[1])
unknown_this_line = len(np.where(np_sample_row == "?")[0])
unknown_this_line


# In[ ]:


def possible_combinations(damaged_missing_pos: int, unknown_this_line: int):
    for i in range(0, 2**unknown_this_line):
        if i.bit_count() == damaged_missing_pos:
            yield bin(i)[2:].zfill(unknown_this_line)

def get_possible_arangement_checksum(row, possibility) -> str:
    questionmark_counter = 0
    checksum = []

    counting_active = False
    counter = 0
    for char in row:
        if char == "?":
            if possibility[questionmark_counter] == "0":
                char = "."
            else:
                char = "#"
            questionmark_counter += 1

        if char == "#":
            counter += 1
            counting_active = True
        else:
            if counting_active:
                checksum.append(str(counter))
                counting_active = False
                counter = 0
    if counter > 0:
        checksum.append(str(counter))
    
    return ",".join(checksum)
            

def get_possible_arangement(row, possibility) -> str:
    new_row = []

    questionmark_counter = 0
    for char in row:
        if char == "?":
            append = None
            if possibility[questionmark_counter] == "0":
                append = "."
            else:
                append = "#"
            new_row.append(append)
            questionmark_counter += 1
        else:
            new_row.append(char)
    
    return "".join(new_row)

sample_row_checksum = sample_row.split()[1]

def get_num_different_arangements(row: str) -> int:
    row_arrangement, row_checksum = row.split()
    np_row = np.array([i for i in row_arrangement])
    damaged_known = len(np.where(np_row == "#")[0])
    damaged_this_line_target = num_damaged_from_checksum(row_checksum)
    unknown_this_line = len(np.where(np_row == "?")[0])
    row_checksum = row_checksum

    counter = 0
    for possibility in possible_combinations(damaged_this_line_target - damaged_known, unknown_this_line):
        possible_arangement_checksum = get_possible_arangement_checksum(row_arrangement, possibility)
        if row_checksum == possible_arangement_checksum:
            counter +=1
    
    print(f"{row} has {counter} possible arrangements")
    return counter
    


# In[ ]:


def calculate_distinct_arrangements(input) -> int:
    sum_arrangements = 0
    for row in input.split('\n'):
        sum_arrangements += get_num_different_arangements(row)
    return sum_arrangements

# current_input = input
# print(calculate_distinct_arrangements(current_input))


# In[ ]:


# Part 2
# ???.### 1,1,3   ->    ???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3 (5x joined by ?)
def calculate_distinct_arrangements(input) -> int:
    sum_arrangements = 0
    max_rows = 2
    for i, row in enumerate(input.split('\n')):
        if i < max_rows:
            row_arrangement, row_checksum = row.split()
            print(f"{row_arrangement}, {row_checksum}")
            row_arrangement = "?".join([row_arrangement for i in range(5)])
            row_checksum = ",".join([row_checksum for i in range(5)])
            print(f"{row_arrangement}, {row_checksum}")
            row = row_arrangement + " " + row_checksum
            sum_arrangements += get_num_different_arangements(row)
    return sum_arrangements

# current_input = input_sample
# print(calculate_distinct_arrangements(current_input))


# In[ ]:

# for i, row in enumerate(input.split('\n')):
#     arr, chksum = row.split()
#     groups = [int(part) for part in chksum.split(",")]
#     groups_fixed_len = sum(groups) + len(groups) - 1
#     resulting_diff = len(arr) - groups_fixed_len
#     num_points = sum([1 for i in arr if i == "."])
#     print(f"{arr}    {chksum}     {len(arr)=}, {groups_fixed_len=}, {(resulting_diff - num_points)=}")



# %%

import functools

# trying with recursion
sample_row = "????.######..#####.?????.######..#####.?????.######..#####.?????.######..#####.?????.######..#####."
sample_chk = "1,6,5,1,6,5,1,6,5,1,6,5,1,6,5"

@functools.cache  # 1000x+ speedup
def arrangements(config, group):
    
    # Base cases
    if (len(group) == 0):
        a = int(sum(c == "#" for c in config) == 0)
        return a
    if (sum(group) + len(group) - 1)  > len(config):
        return 0
    
    # One case for .
    if config[0] == ".":
        a = arrangements(config[1:], group)
        return a

    no1, no2 = 0, 0
    # possibility to start next tile
    if config[0] == "?":
        no2 = arrangements(config[1:], group)

    # possibility to start here
    if all(c != 0 for c in config[:group[0]]) \
        and (config[group[0]] if len(config) > group[0] else ".") != "#":
        no1 = arrangements(config[(group[0] + 1):], group[1:])
    
    return no1 + no2

group = tuple([int(i) for i in sample_chk.split(",")])
assert arrangements(sample_row, group) == 2500


# %%
