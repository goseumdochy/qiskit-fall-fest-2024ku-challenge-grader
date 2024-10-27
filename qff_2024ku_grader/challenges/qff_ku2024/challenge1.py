from typeguard import typechecked
from typing import List, Tuple
from qff_2024ku_grader.grader.grade import grade
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp

@typechecked
def grade_challenge1a(answer: str) -> None:
    grade(answer, "1a")
    
@typechecked
def grade_challenge1b(answer: QuantumCircuit) -> None:
    grade(answer, "1b")

@typechecked
def grade_challenge1c(answer: List[SparsePauliOp]) -> None:
    grade(answer, "1c")

@typechecked
def grade_challenge1d(answer: Tuple[QuantumCircuit, List[SparsePauliOp]]) -> None:
    grade(answer, "1d")