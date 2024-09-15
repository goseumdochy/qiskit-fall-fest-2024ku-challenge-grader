import os
import requests

from urllib.parse import urljoin

from typing import Dict, List, Mapping, Optional, Union

from qff_2024ku_grader import __version__
from qff_2024ku_grader.grader.common import normalize_slash
from qiskit_ibm_runtime import QiskitRuntimeService



is_staging: bool = 'auth-dev' in os.getenv('QXAuthURL', 'auth')

# possible challenge grading endpoints: https://qac-grading-dev.quantum.ibm.com
grading_endpoints: List[str] = [
    'http://127.0.0.1:8000', # 여기에 추후 서버 ip 추가하면 될 듯
    f'https://qac-grading{"-dev" if is_staging else ""}.quantum.ibm.com'
]

_api_grade_url: Optional[str] = os.getenv('QC_GRADING_ENDPOINT')

class MaxContentError(BaseException):
    def __init__(self, content_length: int, max_content_length: int) -> None:
        self.message = f'Max content length ({max_content_length}) exceeded: {content_length}'

    def __str__(self) -> str:
        return self.message

def get_grading_endpoint(
    question_id: Union[str, int]
) -> Optional[str]:
    # https://qac-grading-dev.quantum.ibm.com
    global _api_grade_url
    if not _api_grade_url:
        for endpoint in grading_endpoints:
            try:
                response = requests.get(url=endpoint)
                response.raise_for_status()
                if response.ok:
                    _api_grade_url = endpoint
                    break
            except Exception as err:
                pass

    if not _api_grade_url:
        print('Could not find a valid grading server or '
              'the grading servers are down right now.')
        return None

    return f'{normalize_slash(_api_grade_url)}answers/{question_id}'

def send_request(
    endpoint: str,
    body: Optional[Dict[str, str]] = None,
) -> Dict[str, str]:

    response = requests.post(
        url=endpoint,
        json=body
    )

    if response.status_code != 200:
        if response.status_code == 403:
            result = f'Unable to access service ({response.reason})'
        else:
            try:
                result = response.json()
                if 'error' in result:
                    result = result['error']
                if 'message' in result:
                    result = result['message']
            except Exception:
                result = f' Not successful - {response.reason}'
        raise Exception(result)

    return response.json()