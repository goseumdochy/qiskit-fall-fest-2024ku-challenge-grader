from typeguard import typechecked
from qff_2024ku_grader.grader.grade import grade

@typechecked
def grade_test_challenge(answer: list) -> None:
    answer[14] = answer[14].qasm()
    grade(answer, "Challenge2")