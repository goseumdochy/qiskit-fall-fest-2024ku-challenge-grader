from typeguard import typechecked
from typing import List, Tuple
from qff_2024ku_grader.grader.grade import grade
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp

@typechecked
def grade_challenge1a(answer, username:str) -> None:
    grade(answer, "1a", username)
    
@typechecked
def grade_challenge1b(answer: QuantumCircuit, username:str) -> None:
    grade(answer, "1b", username)

@typechecked
def grade_challenge1c(answer: List[SparsePauliOp], username:str) -> None:
    grade(answer, "1c", username)

@typechecked
def grade_challenge1d(answer: Tuple[QuantumCircuit, List[SparsePauliOp]], username:str) -> None:
    grade(answer, "1d", username)