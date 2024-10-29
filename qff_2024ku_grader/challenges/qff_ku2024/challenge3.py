from typeguard import typechecked
from typing import List, Tuple
from qff_2024ku_grader.grader.grade import grade
from qiskit import QuantumCircuit
from qiskit.primitives import PrimitiveJob
from qiskit.providers import JobStatus
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import StagedPassManager

@typechecked
def grade_challenge3a(answer: dict) -> None:
    grade(answer, "3a")

@typechecked
def grade_challenge3b(answer: StagedPassManager) -> None:
    grade([len(answer.to_flow_controller().tasks), len(answer.init.to_flow_controller().tasks), len(answer.layout.to_flow_controller().tasks), len(answer.routing.to_flow_controller().tasks)
           ], "3b")
  
@typechecked
def grade_challenge3c(answer: StagedPassManager) -> None:
    grade([len(answer.to_flow_controller().tasks), len(answer.init.to_flow_controller().tasks), len(answer.layout.to_flow_controller().tasks), len(answer.routing.to_flow_controller().tasks)
           ], "3c")

@typechecked
def grade_challenge3d(answer: StagedPassManager) -> None:
    grade([len(answer.to_flow_controller().tasks), len(answer.init.to_flow_controller().tasks), len(answer.layout.to_flow_controller().tasks), len(answer.routing.to_flow_controller().tasks)
           ], "3d")
    
@typechecked
def grade_challenge3e(answer: StagedPassManager) -> None:
    grade([len(answer.to_flow_controller().tasks), len(answer.init.to_flow_controller().tasks), len(answer.layout.to_flow_controller().tasks), len(answer.routing.to_flow_controller().tasks)
           ], "3e")
  
@typechecked
def grade_challenge3f(answer: List[dict]) -> None:
    grade(answer, "3f")