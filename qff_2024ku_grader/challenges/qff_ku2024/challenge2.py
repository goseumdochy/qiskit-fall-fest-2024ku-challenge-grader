from typeguard import typechecked
from qff_2024ku_grader.grader.grade import grade
from qiskit import QuantumCircuit
from qiskit.primitives import PrimitiveJob
from qiskit.providers import JobStatus

@typechecked
def grade_challenge2a(answer: QuantumCircuit) -> None:
    grade(answer, "2a")
    
@typechecked
def grade_challenge2b(answer: PrimitiveJob) -> None:
    status = answer.status()
    if status != JobStatus.DONE:
        print(f'Please wait for Job to complete succesfully before grading: {status}')
    else:
        r = answer.result()[0]
        grade({
            'metadata': r.metadata,
            'counts': r.data.meas.get_counts()
        }, "2b")

@typechecked
def grade_challenge2c(answer: QuantumCircuit) -> None:
    grade(answer, "2c")

@typechecked
def grade_challenge2d(answer: PrimitiveJob) -> None:
    status = answer.status()
    if status != JobStatus.DONE:
        print(f'Please wait for Job to complete succesfully before grading: {status}')
    else:
        r = answer.result()[0]
        grade({
            'metadata': r.metadata,
            'counts': r.data.meas.get_counts()
        }, "2d")