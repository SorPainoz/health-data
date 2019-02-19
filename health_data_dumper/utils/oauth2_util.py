from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow

FITNESS_SERVICE_ACCOUNT_FILE = 'client_secret_390786955669-gm252phdg8edftlq66j8j79u0klke3c6.apps.googleusercontent.com.json'
FITNESS_SCOPE = ('https://www.googleapis.com/auth/fitness.body.read',
                 'https://www.googleapis.com/auth/fitness.activity.read')
DEFAULT_STORAGE_FILE = 'credentials.storage'


def authorize_credentials(storage=Storage(DEFAULT_STORAGE_FILE), service_account_file=FITNESS_SERVICE_ACCOUNT_FILE,
                          scope=FITNESS_SCOPE):
    """
    Start the OAuth flow to retrieve credentials

    :param storage:
    :param service_account_file:
    :param scope:
    :return:
    """
    credentials = storage.get()

    if credentials is None or credentials.invalid or credentials.access_token_expired:
        flow = flow_from_clientsecrets(service_account_file, scope=scope)
        credentials = run_flow(flow, storage)

    return credentials


def get_fitness_token():
    credentials = authorize_credentials()

    return credentials.access_token


def get_fitness_authorized_header():
    return {'content-type': 'application/json', 'Authorization': f'Bearer {get_fitness_token()}'}


if __name__ == '__main__':
    get_fitness_authorized_header()
