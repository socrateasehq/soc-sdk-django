from .settings import SOC_API_HOST
from .helpers import make_soc_request
import logging


def get_assessments_created_by_user(username):
    """Get all assessments from Socratease.

    Returns:
        list: All assessments from Socratease created by user `username` where username is the username used to
        initialize the Socratease SDK.
    """

    url = '{0}/api/v1/assessments/?username={1}'.format(SOC_API_HOST, username)
    assessments_resp = make_soc_request(url, method='GET')
    if assessments_resp.status_code == 200:
        assessments_resp_json = assessments_resp.json()
    else:
        logging.error('Error getting assessments from Socratease because: {0}'.format(assessments_resp.text))
        assessments_resp_json = None

    return assessments_resp_json


def get_all_assessment_progress():
    """Get all assessment_progress records from Socratease which can be used for billing.

    Returns:
        list: All assessment_progress records from Socratease.
    """

    url = '{0}/api/v1/ext/assessment-progress/'.format(SOC_API_HOST)
    assessment_progress_resp = make_soc_request(url, method='GET')
    if assessment_progress_resp.status_code == 200:
        assessment_progress_resp_json = assessment_progress_resp.json()
    else:
        logging.error('Error getting assessment_progress from Socratease because: {0}'.format(
            assessment_progress_resp.text)
            )
        assessment_progress_resp_json = None

    return assessment_progress_resp_json
