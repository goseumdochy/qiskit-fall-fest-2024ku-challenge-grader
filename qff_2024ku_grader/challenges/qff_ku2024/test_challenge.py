from typeguard import typechecked
from qff_2024ku_grader.grader.grade import grade
from qiskit import QuantumCircuit

@typechecked
def grade_test_challenge(answer: QuantumCircuit, username:str) -> None:
    grade(answer, "test", username)