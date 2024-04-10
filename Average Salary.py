class Solution:
    def average(self, salary: List[int]) -> float:
        max_sal = max(salary)
        min_sal = min(salary)
        exclude = []
        for ele in salary:
            if ele == max_sal or ele == min_sal:
                continue
            else:
                exclude.append(ele)
        if len(exclude) == 1:
            return exclude[0]
        return sum(exclude) / len(exclude)