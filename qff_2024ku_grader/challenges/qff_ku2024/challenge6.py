from typeguard import typechecked
from typing import List
from qff_2024ku_grader.grader.grade import grade
from qiskit import QuantumCircuit

@typechecked
def grade_challenge6a(answer: QuantumCircuit) -> None:
    grade(answer, "6a")
    
@typechecked
def grade_challenge6b(answer: QuantumCircuit) -> None:
    grade(answer, "6b")

@typechecked
def grade_challenge6c(answer: QuantumCircuit) -> None:
    grade(answer, "6c")

@typechecked
def grade_challenge6d(answer: int) -> None:
    grade(answer, "6d")
    
@typechecked
def grade_challenge6e(answer: float) -> None:
    grade(answer, "6e")