from typeguard import typechecked
from typing import List, Tuple
from qff_2024ku_grader.grader.grade import grade
from qiskit import QuantumCircuit
from qiskit.primitives import PrimitiveJob
from qiskit.providers import JobStatus
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import StagedPassManager

@typechecked
def grade_challenge3a(answer: dict, username:str) -> None:
    grade(answer, "3a", username)

@typechecked
def grade_challenge3b(answer: StagedPassManager, username:str) -> None:
    grade([len(answer.to_flow_controller().tasks), len(answer.init.to_flow_controller().tasks), len(answer.layout.to_flow_controller().tasks), len(answer.routing.to_flow_controller().tasks)
           ], "3b", username)
  
@typechecked
def grade_challenge3c(answer: StagedPassManager, username:str) -> None:
    grade([len(answer.to_flow_controller().tasks), len(answer.init.to_flow_controller().tasks), len(answer.layout.to_flow_controller().tasks), len(answer.routing.to_flow_controller().tasks)
           ], "3c", username)

@typechecked
def grade_challenge3d(answer: StagedPassManager, username:str) -> None:
    grade([len(answer.to_flow_controller().tasks), len(answer.init.to_flow_controller().tasks), len(answer.layout.to_flow_controller().tasks), len(answer.routing.to_flow_controller().tasks)
           ], "3d", username)
    
@typechecked
def grade_challenge3e(answer: StagedPassManager, username:str) -> None:
    grade([len(answer.to_flow_controller().tasks), len(answer.init.to_flow_controller().tasks), len(answer.layout.to_flow_controller().tasks), len(answer.routing.to_flow_controller().tasks)
           ], "3e", username)
  
@typechecked
def grade_challenge3f(answer: List[dict], username:str) -> None:
    grade(answer, "3f", username)