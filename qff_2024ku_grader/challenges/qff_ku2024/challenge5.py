from typeguard import typechecked
from typing import List
from qff_2024ku_grader.grader.grade import grade
from qiskit import QuantumCircuit

@typechecked
def grade_challenge5a(answer: QuantumCircuit, username:str) -> None:
    grade(answer, "5a", username)
    
@typechecked
def grade_challenge5b(answer: List[QuantumCircuit], username:str) -> None:
    grade(answer, "5b", username)

@typechecked
def grade_challenge5c(answer: QuantumCircuit, username:str) -> None:
    grade(answer, "5c", username)

@typechecked
def grade_challenge5d(answer: dict, username:str) -> None:
    grade(answer, "5d", username)