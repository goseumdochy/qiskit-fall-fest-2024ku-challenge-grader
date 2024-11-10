from typeguard import typechecked
from typing import List
from qff_2024ku_grader.grader.grade import grade
from qiskit import QuantumCircuit

@typechecked
def grade_challenge6a(answer: QuantumCircuit, username:str) -> None:
    grade(answer, "6a", username)
    
@typechecked
def grade_challenge6b(answer: QuantumCircuit, username:str) -> None:
    grade(answer, "6b", username)

@typechecked
def grade_challenge6c(answer: QuantumCircuit, username:str) -> None:
    grade(answer, "6c", username)

@typechecked
def grade_challenge6d(answer: int, username:str) -> None:
    grade(answer, "6d", username)
    
@typechecked
def grade_challenge6e(answer: float, username:str) -> None:
    grade(answer, "6e", username)