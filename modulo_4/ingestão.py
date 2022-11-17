import requests
import logging
from abc import ABC, abstractmethod
import datetime

# implementando logs
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# implementando a class
class MercadoBircoinAPI(ABC):

    def __init__(self, coin:str) -> None:
        self.coin = coin
        self.base_endpoint = "https://www.mercadobitcoin.net/api"

    # def _get_endpoint(self) -> str:
    #     return f'{self.base_endpoint}/{self.coin}/day-summary/2021/6/22'

    @abstractmethod         # **kwargs diz que pode ou não receber argumentos
    def _get_endpoint(self, **kwargs) -> str:

        pass

    def get_data(self) -> dict:
        endpoint = self._get_endpoint()
        logging.info(f'Getting data from endpoint: {endpoint}')
        response = requests.get(endpoint)
        response.raise_for_status() # verifica o status do retorno do endpoint
        return response.json()

class DaySumaryApi(MercadoBircoinAPI):

    type = "day-summary"

    def _get_endpoint(self, date: datetime) -> str:
        return f'{self.base_endpoint}/{self.coin}/{self.type}/'
