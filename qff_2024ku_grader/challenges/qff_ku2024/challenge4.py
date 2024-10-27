from typeguard import typechecked
from qff_2024ku_grader.grader.grade import grade
from qiskit import QuantumCircuit

@typechecked
def grade_challenge4a(answer: QuantumCircuit) -> None:
    grade(answer, "4a")
    
@typechecked
def grade_challenge4b(answer: dict) -> None:
    grade(answer, "4b")

@typechecked
def grade_challenge4c(answer: QuantumCircuit) -> None:
    grade(answer, "4c")

@typechecked
def grade_challenge4d(answer: dict) -> None:
    grade(answer, "4d")
    
@typechecked
def grade_challenge4e(answer: QuantumCircuit) -> None:
    grade(answer, "4e")
    
@typechecked
def grade_challenge4f(answer: QuantumCircuit) -> None:
    grade(answer, "4f")
    
@typechecked
def grade_challenge4g(answer: QuantumCircuit) -> None:
    grade(answer, "4g")
    
@typechecked
def grade_challenge4h(answer: dict) -> None:
    grade(answer, "4h")