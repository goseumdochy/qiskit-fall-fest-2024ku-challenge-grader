import json

from typing import Any, Callable, Dict, List, Optional, Tuple, Union


from qff_2024ku_grader.custom_encoder import to_json

from .api import (
    get_grading_endpoint,
    send_request
)


def grade(
    answer: Any,
    question: Union[str, int],
    **kwargs: Any
) -> Tuple[bool, Optional[Union[str, int, float]], Optional[Union[str, int, float]]]:
    serialized_answer = to_json(answer, **kwargs)

    endpoint = get_grading_endpoint(question)
    payload = {'answer': serialized_answer}

    if serialized_answer is not None and endpoint:
        print('Grading your answer. Please wait...')

        result = grade_answer(
            payload,
            endpoint
        )

    else:
        handle_grade_response('failed')


def grade_answer(
    payload: Dict[str, str],
    endpoint: str,
) -> Tuple[bool, Optional[Union[str, int, float]], Optional[Union[str, int, float]]]:
    try:
        # access_token = get_access_token()
        # if access_token:
        #     header = {'Authorization': f'Bearer {access_token}'}
        # else:
        #     header = None

        answer_response = send_request(
            endpoint,
            body=payload
        )

        if True: # 점수가 있는 챌린지에서는 분기할 예정
            handle_grade_response(answer_response["grading_validation"])

    except Exception as err:
        print(f'Failed: {err}')
        return False, None, str(err)


def handle_grade_response(
    status: Optional[str], score: Optional[int] = None, cause: Optional[str] = None
) -> None:
    if status == 'Valid' or status is True:
        print('\nCongratulations 🎉! Your answer is correct.')
        if score is not None: # 점수가 있는 챌린지 문제에서 활용
            print(f'Your score is {score}.')
    elif status == 'invalid':
        print(f'\nOops 😕! {"Your answer is incorrect" if cause is None else cause}')
        print('Please review your answer and try again.')
    else:
        print(f'Failed: {cause}')
        print('Unable to grade your answer.')