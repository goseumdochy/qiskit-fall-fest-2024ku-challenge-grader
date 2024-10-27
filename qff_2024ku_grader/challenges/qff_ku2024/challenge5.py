from typeguard import typechecked
from typing import List
from qff_2024ku_grader.grader.grade import grade
from qiskit import QuantumCircuit

@typechecked
def grade_challenge5a(answer: QuantumCircuit) -> None:
    grade(answer, "5a")
    
@typechecked
def grade_challenge5b(answer: List[QuantumCircuit]) -> None:
    grade(answer, "5b")

@typechecked
def grade_challenge5c(answer: QuantumCircuit) -> None:
    grade(answer, "5c")

@typechecked
def grade_challenge5d(answer: dict) -> None:
    grade(answer, "5d")