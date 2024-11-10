from typeguard import typechecked
from qff_2024ku_grader.grader.grade import grade
from qiskit import QuantumCircuit

@typechecked
def grade_challenge4a(answer: QuantumCircuit, username:str) -> None:
    grade(answer, "4a", username)
    
@typechecked
def grade_challenge4b(answer: dict, username:str) -> None:
    grade(answer, "4b", username)

@typechecked
def grade_challenge4c(answer: QuantumCircuit, username:str) -> None:
    grade(answer, "4c", username)

@typechecked
def grade_challenge4d(answer: dict, username:str) -> None:
    grade(answer, "4d", username)
    
@typechecked
def grade_challenge4e(answer: QuantumCircuit, username:str) -> None:
    grade(answer, "4e", username)
    
@typechecked
def grade_challenge4f(answer: QuantumCircuit, username:str) -> None:
    grade(answer, "4f", username)
    
@typechecked
def grade_challenge4g(answer: QuantumCircuit, username:str) -> None:
    grade(answer, "4g", username)
    
@typechecked
def grade_challenge4h(answer: dict, username:str) -> None:
    grade(answer, "4h", username)